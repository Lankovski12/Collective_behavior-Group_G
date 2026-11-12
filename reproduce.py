"""Reproduce the k=3 results of Iacopini et al. (2022) with our baseline model.

    python reproduce.py           # full run (10 runs per point, takes a while)
    python reproduce.py --quick   # short test run

Outputs (in figures/):
    abm.csv            final n_A+p of every simulation run
    critical_mass.csv  mean-field critical mass p_c for each beta
    fig1.pdf / .png    (a) n_A+p vs p, mean field (lines) and simulations (dots)
                       (b) mean-field phase diagram of n_A+p in the (beta, p) plane
"""
import sys
from multiprocessing import Pool
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp

from speaking_out import NamingGameModel

N = 1000           # number of agents
T_MAX = 1000       # max time, in units of N interactions
N_RUNS = 10        # independent runs per (beta, p)
BETAS = [0.3, 0.4, 0.7, 1.0]
PS = np.round(np.arange(0, 0.201, 0.01), 2)
COLORS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]
OUT = Path("figures")


# ---- mean field (Eqs. 1-2 in the report) ------------------------------------
def mf_rhs(t, y, beta, p):
    n_a, n_b = y
    n_ab = 1 - n_a - n_b - p
    P_a, P_b = n_a + p + n_ab / 2, n_b + n_ab / 2   # speaker says A / B
    q_a, q_b = 1 - n_b, 1 - n_a - p                 # listener knows A / B
    dn_a = beta * n_ab * (0.5 * q_a**2 + 2 * P_a * q_a) - 2 * P_b * n_a
    dn_b = beta * n_ab * (0.5 * q_b**2 + 2 * P_b * q_b) - 2 * P_a * n_b
    return [dn_a, dn_b]


def mf_stationary(beta, p, t_max=2000):
    """Stationary n_A + p, starting from everybody (non-committed) holding B."""
    sol = solve_ivp(mf_rhs, (0, t_max), [0.0, 1 - p], args=(beta, p),
                    rtol=1e-8, atol=1e-10)
    return sol.y[0, -1] + p


def critical_mass(beta, tol=1e-4):
    """Smallest p with stationary n_A + p > 1/2 (bisection)."""
    lo, hi = 0.0, 0.3
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if mf_stationary(beta, mid) > 0.5:
            hi = mid
        else:
            lo = mid
    return hi


# ---- agent-based simulations --------------------------------------------------
def run_abm(args):
    beta, p, seed = args
    model = NamingGameModel(n=N, k=3, beta=beta, p=p,
                            interactions_per_step=N, seed=seed)
    model.run_until_absorbed(max_interactions=T_MAX * N)
    n_a = model.datacollector.get_model_vars_dataframe()["n_A"]  # includes committed
    # consensus: final value; otherwise average over the last 100 time units
    value = n_a.iloc[-1] if model.absorbed else n_a.iloc[-100:].mean()
    return beta, p, seed, value


if __name__ == "__main__":
    quick = "--quick" in sys.argv
    n_runs = 2 if quick else N_RUNS
    ps = PS[::2] if quick else PS
    OUT.mkdir(exist_ok=True)

    # simulations (in parallel on all cores)
    tasks = [(b, p, s) for b in BETAS for p in ps for s in range(n_runs)]
    print(f"Running {len(tasks)} simulations ...")
    with Pool() as pool:
        rows = pool.map(run_abm, tasks)
    abm = pd.DataFrame(rows, columns=["beta", "p", "seed", "nA_plus_p"])
    abm.to_csv(OUT / "abm.csv", index=False)

    # mean-field critical mass
    pc = pd.DataFrame({"beta": BETAS, "p_c": [critical_mass(b) for b in BETAS]})
    pc.to_csv(OUT / "critical_mass.csv", index=False)
    print(pc.to_string(index=False))

    # figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    p_fine = np.linspace(0, 0.2, 201)
    for beta, color in zip(BETAS, COLORS):
        ax1.plot(p_fine, [mf_stationary(beta, p) for p in p_fine],
                 color=color, lw=2, label=rf"$\beta={beta}$")
        g = abm[abm.beta == beta].groupby("p")["nA_plus_p"]
        ax1.errorbar(g.mean().index, g.mean(), yerr=g.std(), fmt="o",
                     ms=5, color=color, mec="white", mew=1)
    ax1.set_xlabel("committed fraction $p$")
    ax1.set_ylabel("stationary $n_A+p$")
    ax1.set_title("(a) mean field (lines) vs. simulations (dots)", loc="left")
    ax1.legend(frameon=False)
    ax1.grid(alpha=0.3)

    n_grid = 25 if quick else 80
    beta_grid = np.linspace(0.01, 1, n_grid)
    p_grid = np.linspace(0.001, 0.15, n_grid)
    Z = [[mf_stationary(b, p) for b in beta_grid] for p in p_grid]
    im = ax2.pcolormesh(beta_grid, p_grid, Z, cmap="Blues", vmin=0, vmax=1)
    fig.colorbar(im, ax=ax2, label="stationary $n_A+p$")
    ax2.set_xlabel(r"$\beta$")
    ax2.set_ylabel("$p$")
    ax2.set_title("(b) mean-field phase diagram", loc="left")

    fig.tight_layout()
    fig.savefig(OUT / "fig1.pdf")
    fig.savefig(OUT / "fig1.png", dpi=200)
    print(f"Saved results to {OUT.resolve()}")
