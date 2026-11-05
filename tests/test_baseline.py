from speaking_out import NamingGameModel


def test_no_committed_stays_all_B():
    m = NamingGameModel(n=200, p=0.0, beta=0.5, seed=1)
    for _ in range(20):
        m.step()
    assert m.fraction(2) == 1.0  # nobody ever hears A


def test_committed_never_change():
    m = NamingGameModel(n=200, p=0.05, beta=0.5, seed=1)
    for _ in range(50):
        m.step()
    assert all(a.vocab == 1 for a in m.agents if a.committed)


def test_intermediate_beta_minority_takeover():
    # paper: for intermediate beta a small committed minority can win (p=3%)
    wins = 0
    for s in range(5):
        m = NamingGameModel(n=500, k=3, beta=0.4, p=0.03, seed=s)
        m.run_until_absorbed(max_interactions=3_000_000)
        wins += m.fraction(1) == 1.0
    assert wins >= 3


def test_beta_one_minority_loses():
    m = NamingGameModel(n=500, k=3, beta=1.0, p=0.03, seed=0)
    m.run_until_absorbed(max_interactions=2_000_000)
    assert m.fraction(1) < 1.0