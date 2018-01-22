# Lysogenic Propensity in Stressed Environments as a function of Muliplicity of Infection

Description: Research project, undertaken with [Supreet Saini](http://www.che.iitb.ac.in/online/faculty/supreet-saini), [IIT Bombay](http://www.iitb.ac.in)

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

Our first approach was to observe the result of running Gillespie simulations on fixed curves of Probability of Lysogeny **P(lyso)** versus Multiplicity of Infection **MoI** for individual values of *p<sub>1</sub>* and *p<sub>2</sub>*. The code for this iteration is included in [Run1](../master/Run1/). This approach validated our proposition that for the chosen values, the time for which the phage and the bacteria coexist increases with higher lysogeni propensity.

[Our next approach](../master/Run4) was a slightly novel one - instead of running the entire Gillespie simulation till one of the species went extinct, we chose a novel single echelon method. The idea behind this approach is that the coexistence of the two-species system may be best assured by choosing an action which leads to an MoI closest to 1. We run this simulation for all values of *p<sub>1</sub>* and *p<sub>2</sub>* each in the range [0.1,0.2,...,1.0] for five different cases:

* [alt_run](../master/Run4/output.zip): *lambda<sub>p</sub>* = 1, *lambda<sub>b</sub>* = 0.1
* [alt_run2](../master/Run4/output.zip): *lambda<sub>p</sub>* = 2, *lambda<sub>b</sub>* = 0.1
* [alt_run3](../master/Run4/output.zip): *lambda<sub>p</sub>* = 2, *lambda<sub>b</sub>* = 1.0
* [alt_run4](../master/Run4/output.zip): *lambda<sub>p</sub>* = 3, *lambda<sub>b</sub>* = 0.1
* [alt_run5](../master/Run4/output.zip): *lambda<sub>p</sub>* = 2, *lambda<sub>b</sub>* = 2.0

The table below recapitulates the parameters used along with their description and range of values:

| Parameter | Description | Value(s) |
|:---------:|:----------- |:--------:|
| *MoI*       | The ratio of total phages to bacteria in the system | [0.01,0.02,...,2.0] |
| *lambda<sub>p</sub>* | The rate of degradation of phages during bad environment | [1,2,3] |
| *lambda<sub>b</sub>* | The rate of degradation of bacteria during bad environment | [0.1,1,2] |
| *r* | bacterial rate of growth | [1,2,5] |
| *a* | burst factor (phage amplification factor) | [10] |
| *p<sub>1</sub>* | probability of occurence of a good environment period for phages | [0.1,0.2,...,1.0] |
| *p<sub>2</sub>* | probability of occurence of a good environment period for bacteria | [0.1,0.2,...,1.0] |

The resulting graphical results have been added [here](../master/Run4/facet_plot) and [here](../master/Run4/shaded_plot).

## Current work: 
* Visualising the overall trends in a better manner
* Selecting more appropriate values of the parameters and widening the range chosen
* Explaining this phenomenon better through the genetic pathway regulation
