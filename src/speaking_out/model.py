"""Baseline: higher-order Naming Game with a committed minority.

Reimplementation of Iacopini, Petri, Baronchelli & Barrat (2022),
Commun. Phys. 5, 64, doi:10.1038/s42005-022-00845-y
Original code: https://github.com/iaciac/higher-order-NG

Vocabulary of an agent is a bitmask: A=1, B=2, AB=3 (knows both names).

One call to ``NamingGameModel.step()`` performs ``interactions_per_step``
group interactions (the paper's "time step" is ONE group interaction).
"""
from __future__ import annotations

import mesa

A, B, AB = 1, 2, 3


class NamingGameAgent(mesa.Agent):
    def __init__(self, model, vocab: int, committed: bool = False):
        super().__init__(model)
        self.vocab = vocab
        self.committed = committed
        # Hooks for the extension (boldness / conformity / tolerance / belief
        # strength) go here. In the baseline all agents are identical and the
        # only heterogeneity is committed vs. non-committed.

    def speak(self) -> int:
        """Pick a name from the own vocabulary uniformly at random."""
        if self.vocab == AB:
            return A if self.model.random.random() < 0.5 else B
        return self.vocab

    def knows(self, name: int) -> bool:
        return bool(self.vocab & name)


class NamingGameModel(mesa.Model):
    """Naming game on a homogeneously mixed population, groups of size k.

    Parameters
    ----------
    n : number of agents
    k : group size (k=2 is the classic pairwise naming game)
    beta : probability that a *possible* agreement actually converts the group
    p : fraction of committed agents (always hold name A)
    rule : "unanimity" (all hearers must know the name) or "union" (at least one)
    interactions_per_step : group interactions executed per model step
    """

    def __init__(self, n=1000, k=3, beta=0.5, p=0.05, rule="unanimity",
                 interactions_per_step=100, seed=None):
        super().__init__(rng=seed)
        assert rule in ("unanimity", "union")
        self.n, self.k, self.beta, self.p, self.rule = n, k, beta, p, rule
        self.interactions_per_step = interactions_per_step
        self.interactions = 0

        n_committed = int(round(p * n))
        for i in range(n):
            if i < n_committed:
                NamingGameAgent(self, vocab=A, committed=True)
            else:
                NamingGameAgent(self, vocab=B)
        self._agents_list = list(self.agents)

        self.datacollector = mesa.DataCollector(
            model_reporters={
                "n_A": lambda m: m.fraction(A),
                "n_B": lambda m: m.fraction(B),
                "n_AB": lambda m: m.fraction(AB),
                "interactions": lambda m: m.interactions,
            }
        )
        self.datacollector.collect(self)

    # ---- observables -------------------------------------------------
    def fraction(self, vocab: int) -> float:
        """Fraction of agents with exactly this vocabulary (committed count as A)."""
        return sum(1 for a in self._agents_list if a.vocab == vocab) / self.n

    @property
    def absorbed(self) -> bool:
        v = self._agents_list[0].vocab
        return all(a.vocab == v for a in self._agents_list)

    # ---- dynamics ----------------------------------------------------
    def interact(self):
        group = self.random.sample(self._agents_list, self.k)
        speaker, hearers = group[0], group[1:]
        name = speaker.speak()

        if self.rule == "unanimity":
            agreement = all(h.knows(name) for h in hearers)
        else:
            agreement = any(h.knows(name) for h in hearers)

        converge = agreement and self.random.random() < self.beta
        for a in group:
            if a.committed:
                continue  # committed agents never update
            if converge:
                a.vocab = name
            elif not a.knows(name):
                a.vocab |= name
        self.interactions += 1

    def step(self):
        for _ in range(self.interactions_per_step):
            self.interact()
        self.datacollector.collect(self)

    def run_until_absorbed(self, max_interactions=5_000_000):
        while not self.absorbed and self.interactions < max_interactions:
            self.step()
        return self.absorbed