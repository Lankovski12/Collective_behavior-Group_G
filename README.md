## Members

- Lana Tkalčič
    - [Lankovski12](https://github.com/Lankovski12)
    - lt80473@student.uni-lj.si
- Matjaž Kranjčec
    - [matjazi-k](https://github.com/matjazi-k)
    - DODAJ

## Project description

We build an agent-based simulation of how a group reacts when one of its members speaks out, for example in a political discussion. Each agent has a personality profile (boldness, conformity, tolerance towards differing opinions), and the speaker expresses an opinion that differs in position and style (moderate and close to the group's views vs. extreme and confrontational). We study how the group's reaction (agreement, rejection, opinion shifts) depends on the personalities in the group, what and how the speaker expresses, and how the personality composition of the group affects collective outcomes such as consensus or the speaker being ignored.

## Starting point

Our main starting point is [Couzin et al. (2005)](https://doi.org/10.1038/nature03236), *Effective leadership and decision-making in animal groups on the move* (Nature), where a small number of informed individuals steer the group. We treat the person speaking out as the informed individual and extend the model with:
- heterogeneous personalities, inspired by animal personality research (shy–bold axis, e.g. [Jolles et al., 2017](https://doi.org/10.1016/j.cub.2017.08.004)) and the Big Five model,
- a bounded confidence mechanism ([Deffuant et al., 2000](https://doi.org/10.1142/S0219525900000078); [Hegselmann & Krause, 2002](https://jasss.soc.surrey.ac.uk/5/3/2.html)), so that agents are only influenced by opinions that are not too far from their own.

[Xie et al. (2011)](https://doi.org/10.1103/PhysRevE.84.011130) and [Centola et al. (2018)](https://doi.org/10.1126/science.aas8827) on committed minorities and tipping points serve as a reference for validating our results.

## Plan and milestones

Progress is tracked via the [GitHub milestones](https://github.com/Lankovski12/Collective_behavior-Group-G/milestones).