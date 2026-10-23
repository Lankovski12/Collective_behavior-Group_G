# Speaking Out: Critical Mass in Group Discussions

## Project description

We want to study how many people have to speak out in a group discussion before the majority comes to accept it as their opinion. We will recreate a fairly recent agent-based model of critical mass in social conventions, in which a committed minority can overturn an established norm, and then extend it so that agents differ in personality. 

Instead of identical agents, each agent gets parameters for: 
- boldness (how likely they are to speak out), 
- conformity (how readily it gives up its current view) and 
- tolerance (how much disagreement it accepts).
  
We will also model how strongly agents hold their belief. Our central question is **how the share of speakers needed for a majority shift changes with these traits and with group size.** The idea being that we parameterise the agents with real-world personality and political-attitude survey data.
 
## Team

| Name              | GitHub account  | Email                     |
| ----------------- | --------------- | ------------------------- |
| _Lana Tkalčič_    | _@Lanakovski12_ | lt80473@student.uni-lj.si |
| _Matjaž Kranjčec_ | _@matjazi-k_    | mk92169@student.uni-lj.si |

## Starting point

Iacopini, I., Petri, G., Baronchelli, A. & Barrat, A. (2022). _Group interactions modulate critical mass dynamics in social convention._ Communications Physics 5, 64. [https://doi.org/10.1038/s42005-022-00845-y](https://doi.org/10.1038/s42005-022-00845-y)

**Further reference points**: 
- Centola et al. (2018), _Experimental evidence for tipping points in social convention_, Science 360, 1116–1119; 
- Vilone & Polizzi (2023), _Modelling opinion misperception and the emergence of silence in online social system_, arXiv:2307.04475.

___
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

| Date           | Update                                    |
| -------------- | ----------------------------------------- |
| _23. 10. 2026_ | Repository created, project plan written. |
