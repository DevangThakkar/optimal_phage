# Lysogenic Propensity in Stressed Environments as a function of Muliplicity of Infection

Description: Research project, undertaken with [Supreet Saini](www.che.iitb.ac.in/online/faculty/supreet-saini), [IIT Bombay](www.iitb.ac.in)

## Introduction

We are trying to understand the impact of environmental stresses on the coexistence of phage-bacteria systems. A phage-bacteria system can be characterized with the following parameters: 

* phage and bacterial populations (jointly expressed using multiplicity of infection (MoI))
* bacterial growth rate: (*r*)
* phage burst rate: (*a*)
* bacterial degradation rate: (*lambda<sub>b</sub>*)
* phage degradation rate: (*lambda<sub>p</sub>*)

Some of the pertinent literature in this area covers:

* the impact of the phage degradation rate on coexistence ([Heilmann et al., (2010)](http://doi.org/10.1128/JVI.02326-09))
* a bet-hedging approach to ensure survival in case of sporadic spikes of degradation rates ([Maslov and Sneppen, (2015)](http://doi.org/10.1038/srep10523))
* the stochasticity in the lysogeny-lysis decision at a higher MoI ([Avlund et al., (2009)](http://doi.org/10.1128/JVI.01057-09))
* a game theoretic approach to investigate the lysogenic propensity for different MoI ([Sinha et al., (2017)](http://doi.org/10.3389/fmicb.2017.01386))

We are working on expanding the domain of exploration to include a range of environmental conditions. One possible use case is to simulate the effect of antibiotics on the coexistence of the populations - how the optimal propensity of lysogeny should change in different stress conditions.

## Methods

We consider two additional parameters to describe the environment:

* Probability of good environment for phages: (*p<sub>1</sub>*)
* Probability of good environment for bacteria: (*p<sub>2</sub>*)

Our first approach was to observe the result of running Gillespie simulations on fixed curves of Probability of Lysogeny **P(lyso)** versus Multiplicity of Infection **MoI** for individual values of *p<sub>1</sub>* and *p<sub>2</sub>*.
