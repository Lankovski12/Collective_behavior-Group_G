# Speaking Out: Critical Mass in Group Discussions

How many people have to *speak out* in a group discussion before the majority
adopts their view? We reimplement an agent-based model of critical mass in
social conventions and extend it with agents that **differ in personality**.

## Project description

We want to study how many people have to *speak out* in a group discussion
before the majority comes to accept their opinion. We recreate a recent
agent-based model of critical mass in social conventions, in which a committed
minority can overturn an established norm, and then extend it so that agents
*differ in personality*.

Instead of identical agents, each agent gets parameters for:

- **boldness**: how likely it is to speak out,
- **conformity**: how readily it gives up its current view,
- **tolerance**: how much disagreement it accepts,
- **belief strength**: how strongly it holds its belief.

Our central question is **how the share of speakers needed for a majority
shift changes with these traits and with group size.** We plan to parameterise
the agents with real-world personality and political-attitude survey data.

### Starting point

Iacopini, I., Petri, G., Baronchelli, A. & Barrat, A. (2022). _Group interactions modulate critical mass dynamics in social convention._ Communications Physics 5, 64. [doi:10.1038/s42005-022-00845-y](https://doi.org/10.1038/s42005-022-00845-y)

Further reference points:

- Centola et al. (2018), _Experimental evidence for tipping points in social convention_, Science 360, 1116–1119.
- Vilone & Polizzi (2023), _Modelling opinion misperception and the emergence of silence in online social system_, arXiv:2307.04475.

## Team

| Name             | GitHub          | Email                     |
| ---------------- | --------------- | ------------------------- |
| Lana Tkalčič     | @Lankovski12    | lt80473@student.uni-lj.si |
| Matjaž Kranjčec  | @matjazi-k      | mk92169@student.uni-lj.si |


## Repository structure

```
├── reports/              compiled PDF reports (one per milestone)
├── paper/                LaTeX source of the report (PNAS template)
│   ├── main.tex
│   ├── references.bib
│   └── figures/          figures included in the report
├── src/speaking_out/     the model package
│   ├── model.py          higher-order naming game (Mesa model)
│   └── viz.py            visualisation components for the app
├── tests/                pytest tests of the baseline model
├── figures/              outputs of reproduce.py (CSV data + figures)
├── app.py                interactive Solara app
├── reproduce.py          reproduces the figures in the report
└── pyproject.toml        package and dependencies
```

## Setup and usage

Requires Python 3.10 or newer. From the repository root, create and activate a
virtual environment, then install the project:

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

**Windows (cmd)**

```powershell
py -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e .
```

This installs the model together with Mesa, Solara, NumPy, SciPy, pandas,
Matplotlib and NetworkX.

### Interactive app

```bash
solara run app.py
```

Open the URL printed by Solara (usually <http://localhost:8765>). Stop with
`Ctrl+C`; leave the environment with `deactivate`.

### Reproduce the figures

```bash
python reproduce.py --quick   # short test run
python reproduce.py           # full reproduction (takes a while)
```

CSV files and figures are written to `figures/`.

### Tests

```bash
python -m pip install pytest
python -m pytest
```

### Build the report

```bash
cd paper
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

Copy the resulting `main.pdf` to `reports/report_N.pdf` when a milestone is
submitted.

---

## Report

**[Read the latest report (PDF)](reports/report_1.pdf)**: *Speaking Out: Critical Mass in Group Discussions with Heterogeneous Agents* 

The LaTeX source is in [`paper/`](paper/).

---

## Plan and milestones

### Milestone 1: first report

- Review the relevant concepts and existing models (naming game, committed minorities and critical mass, bounded confidence, spiral of silence).
- Give a general overview of the problem and outline our approach.
- Set up the repository and a first working baseline of the starting-point model.

### Milestone 2: second report

- Polish the first report according to the comments received.
- Describe the methods in detail: the baseline model and our personality extensions (boldness-weighted speaking, per-agent conformity, tolerance-based agreement rule, belief strength).
- Define the verification methodology: reproduce the key results of the starting-point paper, compare with its mean-field equations.
- Choose the survey dataset for parameterising agents.

### Milestone 3: final report

- Polish the previous reports according to the comments received.
- A concise introduction that builds a narrative towards our contribution, supported by relevant research.
- Methods detailed enough that the work can be reimplemented, including the evaluation methodology.
- Results that include a comparison with previous research.
- A discussion in view of previous research, with ideas for future work.
- Individual contributions listed in the Acknowledgements and a link to this repository in the paper.

## Progress log

| Date        | Update                                            |
| ----------- | ------------------------------------------------- |
| 23. 10. 2026 | Repository created, project plan written.        |
| 13. 11. 2026 | Reimplementation completed, first report written. |
