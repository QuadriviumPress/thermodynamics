---
title: "7. The Second Law"
short_title: "Chapter 7"
label: ch-07-the-second-law
---

:::{figure} ../images/art-p184-1.svg
:alt: Chapter opening illustration
:::

# 7. The Second Law

(ch-7)=

The Second Law

*Engineer Carnot’s Troubling Discovery*

:::{admonition} Executive summary
:class: tip
Heat only moves towards a body at a lower temperature. This poses a fundamental limit on the efficiency of work-heat transformations. This limit depends on the maximum and minimum temperatures at which a machine operates, and is usually very low. Carnot described an engine of maximum efficiency.
:::

## Introduction

In chapter 6 (*thermodynamic cycles*), we studied the nature of different cycles for converting heat and work. We now aim to study, explain, and quantify theirverylimits. Thischapter7(*thesecondlaw*)aims to answer two questions:

• Why do all heat engines always have an efficiency less than $100\%$?

• How can the efficiency of a heat machine be maximized?

(sec-7-1)=
## 7.1 The Second Law

### 7.1.1 Statement

The *second law of thermodynamics* is expressed as follows:

Heat spontaneously moves only towards a lower temperature.

This statement can be made more specific: heat can transfer to a higher temperature only when energy is supplied.

We will see that this simple observation has multiple, profound consequences for engineers. In particular, it determines the maximum efficiency of all engines and refrigeration machines!

(sec-7-1-2)=
### 7.1.2 The evidence of the second law

The statement above seems so obvious that it is almost ofefnding. Two remarks are necessary here.

• The second law can be stated in multiple ways. It is more striking to talk about “increase in entropy” than the spontaneous behavior of heat; yet these different statements, which we will gradually address, are all equivalent.

• The apparent manifest evidence of the postulate – of course no one has ever seen, at room temperature, a cup of hot tea spontaneously heat up, or a cold drink spontaneously cool down – crumbles as soon as one studies phenomena at the microscopic level.

Indeed, if temperature is only the level of agitation of particles, then there is *a priori* nothing preventing it from locally increasing even if the ambient temperature is lower. It took half a century of arduous work by thermodynamicists to provide a satisfactory answer to this (curious students will learn of *Maxwell’s demon* to their delight). The application of probabilities to thermodynamics, and in particular the work of Ludwig

Boltzmann (§8.5.3), would reconcile it with the Newtonian mechanistic view of the world during the 20th century. This is not a trivial problem.

In our study and from our engineering point of view, we will accept the above postulate as obvious, without seeking to justify it or explain it.

(sec-7-1-3)=
### 7.1.3 Zeroth law and third law

The *zeroth law* of thermodynamics states that if two bodies are in thermal equilibrium with a third, then all three are in equilibrium with each other. The *third law* states that the entropy (a property that we will study in the next chapter) of a crystal at zero temperature is zero. Neither of these laws is of any importance to the engineer.

(sec-7-2)=
## 7.2 The Second Law and Thermal Machines

## Machines

(sec-7-2-1)=
### 7.2.1 All engines reject heat

Let’s imagine that we want to generate work by taking heat from a “hot” object, that is, at a high temperature: for example, $100^{\circ}C (212 ^{\circ} F)$, as shown in figure 7.1. We connect a cylinder filled with a fluid to this object, and let the fluid push on a piston as it receives heat.

:::{figure} ../images/fig-7-1.jpg
:label: fig-7-1
:enumerator: 7.1
:alt: Production of work with heat from a body at 100 ◦C. The heat transfer allows work to be done, but also causes an increase in the fluid’s temperature.

Production of work with heat from a body at $100^{\circ}C$. The heat transfer allows work to be done, but also causes an increase in the fluid’s temperature.
:::

*Diagram* CC-0 *Olivier Cleynen*

Once it has done some work (at B in figure 7.1), the fluid has increased in volume. If we want to continue converting heat into work and do not want the engine to “infalte” indefinitely, we need to cool this gas to return it to its initial volume.

Unfortunately, *the only way* to extract heat from the gas is to put it in contact with a “cooler” body, as shown in figure 7.2. In particular, it is impossible to return the accumulated heat in the gas to the “hot” body – for that to happen, the gas temperature would need to be higher than this body. This accumulated energy is therefore irretrievably lost.

:::{aside}
« According to this principle, it is not sufficient, in order to give rise to motive power, to produce heat: one must also procure cold; without it, heat would be useless. And indeed, if one were to find only bodies around them as hot as our furnaces, how would one succeed in condensing the steam? Where would one place it once it had come into existence? One must not believe that it could be simply discharged into the atmosphere, as is done in certain machines: the atmosphere would not receive it. It receives it, in the present state of things, only because it serves the function of a vast condenser, because it is at a colder temperature: otherwise it would soon be filled with it, or rather, it would already be saturated with it. »

Sadi Carnot, 1824 [[4](#ref-4)]
:::

:::{figure} ../images/fig-7-2.jpg
:label: fig-7-2
:enumerator: 7.2
:alt: The inevitable cooling of the engine. The only way to return the fluid to its initial state (A) in the experiment in figure 7.1 is by extracting heat from it, which can only be done with a “heat sink” at a lower temperature. The heat and work transfers here are smaller than on the outward journey, but both are non-zero.

The inevitable cooling of the engine. The only way to return the fluid to its initial state (A) in the experiment in figure 7.1 is by extracting heat from it, which can only be done with a “heat sink” at a lower temperature. The heat and work transfers here are smaller than on the outward journey, but both are non-zero.
:::

*Diagram* CC-0 *Olivier Cleynen*

Thus, for an engine to operate continuously, it must, in addition to a high-temperature source from which to capture heat, have a “sink” at low temperature to reject the heat that it can no longer make use of.

This reasoning applies in the same way to refrigerators, air conditioners, and heat pumps, which are designed to absorb heat at a *low* temperature. Once the heat has been absorbed into the low-temperature fluid, the only way to reject it at a higher temperature is to increase the temperature of the fluid. This requires a non-zero compression work. Thus, for a refrigerator to operate continuously, it must receive energy in the form of work.

(sec-7-2-2)=
### 7.2.2 Limits of thermal machines

In order to study heat and work transformations more rigorously, we will use the following notation to describe thermal machines:

• $T_{H}$ and $T_{L}$ will represent the high and low temperatures respectively;

• We will always call$\dot{Q}_{TH}$ the power in the form of heat transferred at high temperature, and$\dot{Q}_{TL}$ its equivalent at low temperature (each can be positive or negative).

Thus, the thermal machine in its most general representation looks like figure 7.3.

Regardless of the operation mode and efficiency of the machine, it cannot create or destroy energy (§1.1.2); and we will always have:

:::{math}
:label: eq-7-1
:enumerator: 7/1
\dot{Q}_{TH}+\dot{Q}_{TL}+\dot{W}_{\mathrm{net}}= 0
:::

:::{figure} ../images/fig-7-3.jpg
:label: fig-7-3
:enumerator: 7.3
:alt: A thermal machine transforming work and heat in its most general representation.

A thermal machine transforming work and heat in its most general representation.
:::

*Diagram* CC-0 *Olivier Cleynen*

The second law has particular consequences for each of the two main types of thermal machines:

**An engine** takes heat from a high-temperature source $(Q\dot{} _{TH}> 0)$ and produces work $(W\dot{} _{\mathrm{net}}< 0$, figure 7.4). We have just seen that if we want to carry out this transformation continuously, we have no choice but to reject heat into a low-temperature reservoir $(Q\dot{} _{TL}< 0)$.

:::{figure} ../images/fig-7-4.jpg
:label: fig-7-4
:enumerator: 7.4
:alt: An example of energy transfers to a thermal engine.

An example of energy transfers to a thermal engine.
:::

*Diagram* CC-0 *Olivier Cleynen*

In power plants, the two temperature zones are easily identifiable: the steam takes heat from the core of the plant (nuclear reactor, gas boiler, or coal boiler) and releases heat through the large cooling chimneys.

Automotive and aeronautical engines, on the other hand, must discharge the air that serves as their working fluid because of the combustion products that prevent its reuse. For this reason, cooling takes place in the atmosphere, outside the engine casing. Their “cooling zone” is not easily distinguishable.

Applied to the engine, the second law states that no engine can continuously convert heat into work from a single heat source. Every engine rejects heat at a lower temperature, so continuous operation requires two reservoirs at different temperatures.

Purists will express this corollary, called the *Kelvin-Planck corollary*, with the following inequality:

:::{math}
:label: eq-7-2
:enumerator: 7/2
\dot{Q}_{TH}> -\dot{W}_{\mathrm{net}}
:::

for any thermal engine.

**A refrigerator, an air conditioner, or a heat pump** operates in the opposite way to engines. These machines extract heat from a low-temperature source $(\dot{Q}_{TL}> 0)$ to reject it into a reservoir at a higher temperature $(\dot{Q}_{TH}< 0$, figure 7.5). An inevitable consequence is that they must receive work for this $(W\dot{} _{\mathrm{net}}> 0)$.

:::{figure} ../images/fig-7-5.jpg
:label: fig-7-5
:enumerator: 7.5
:alt: An example of energy transfers in a refrigerator, air conditioner, or heat pump in operation.

An example of energy transfers in a refrigerator, air conditioner, or heat pump in operation.
:::

*Diagram* CC-0 *Olivier Cleynen*

Applied to a refrigerator, the second law states that any machine that transfers heat to a higher-temperature body receives work.

Purists will enjoy translating this corollary, called the *Clausius corollary*, as follows:

:::{math}
:label: eq-7-3
:enumerator: 7/3
W_{\mathrm{net}}> 0
:::

for any refrigerator, air conditioner, or heat pump.

(sec-7-3)=
## 7.3 The Carnot Cycle

(sec-7-3-1)=
### 7.3.1 Some context

:::{aside}
« To consider in all its generality the principle of the production of motion by heat, one must conceive of it independently of any mechanism, of any particular agent; one must establish reasoning applicable not only to steam engines, but to any imaginable heat engine, regardless of the substance employed and regardless of the manner in which it is acted upon. »

Sadi Carnot, 1824 [[4](#ref-4)]
:::

At the beginning of the 19th century, a young Parisian *Polytechnique* engineer named Sadi Carnot became interested in the operation of thermal engines, which were booming at the time. Carnot sought to predict *the maximum amount of work* that can be generated from a given amount of coal.

Carnot’s approach is interesting in that he completely abstracted the technological aspect to investigate the underlying principles of engine operation. This is even more challenging because at that time, engines operated by vaporizing and condensing steam, and the concepts of a cycle or of energy conservation were not yet established. This abstraction and the clarity of his writing established his only work, *Reflections on the Motive Power of Fire and on Machines Fitted to Develop that Power*, 1824 [[4](#ref-4)], in the history of physics.

Carnot died shortly after his publication and before his work could be recognized; his conception of heat was fundamentally incorrect;[^ch7-fn1] yet the theoretical engine he described, an essential passage for engineering students, serves as a reference in the design offices of all engine manufacturers today.

(sec-7-3-2)=
### 7.3.2 Concept of reversible machine

Carnot sought the theoretical engine whose efficiency would be the maximum possible. He imagined a unique way to transform heat into work and work into heat. His machine can operate in both directions: as an engine or as a refrigerator.

In thermodynamic terms, the machine he conceptualized is not only *bidirectional*, meaning that the direction of fluid flow can be changed to change its function (like many domestic heat pump / ac systems on the market today), but it is also *reversible*: by reversing its operation, all heat flows become exactly opposite. In this way, if Carnot’s refrigerator is powered by Carnot’s engine, then the flows will be exactly compensated, as depicted in figure 7.6.

[^ch7-fn1]: Carnot figured out the second law correctly, but not the first law: he still used Antoine Lavoisier’s *caloric theory*, which was to be dismantled by James Prescott Joule twenty years later.

:::{figure} ../images/fig-7-6.jpg
:label: fig-7-6
:enumerator: 7.6
:alt: Two Carnot machines, an engine (left) and a refrigerator (right). The first powers the second, and since they are reversible (in the thermodynamic sense of the word), the heat flows are balanced.

Two Carnot machines, an engine (left) and a refrigerator (right). The first powers the second, and since they are reversible (in the thermodynamic sense of the word), the heat flows are balanced.
:::

*Diagram* CC-0 *Olivier Cleynen*

Why would such a machine be the most efficient one that can be designed? It can be proven by contradiction that an engine with *higher* efficiency than a reversible engine cannot exist (figure 7.7). The work supplied by this hypothetical machine could be used to power a reversible refrigerator. These two machines together would then receive no net work, but would still create a heat flow from the cold reservoir to the hot reservoir. According to Carnot, and based on the second law whose validity we have accepted, this is impossible: such a machine cannot exist.

:::{aside}
« This maximum [of work] has the property, that, by its *consumption*, a quantity of heat may be carried from the cold body B to the warm one A equal to that which passed from A to B during its *production*. »

Rudolf Clausius, 1850 [[10](#ref-10), [11](#ref-11), [21](#ref-21)]
:::

:::{figure} ../images/fig-7-7.jpg
:label: fig-7-7
:enumerator: 7.7
:alt: Proof by contradiction that the best possible engine is reversible. A hypothetical engine (on the left) with higher efficiency than a reversible refrigerator (on the right) could simply power the latter. Thus, we would obtain a spontaneous net heat flow (here of $100 W)$ from the cold source to the hot source, without a net input of work: according to the second law, this is impossible.

Proof by contradiction that the best possible engine is reversible. A hypothetical engine (on the left) with higher efficiency than a reversible refrigerator (on the right) could simply power the latter. Thus, we would obtain a spontaneous net heat flow (here of $100 W)$ from the cold source to the hot source, without a net input of work: according to the second law, this is impossible.
:::

*Diagram* CC-0 *Olivier Cleynen*

This method of reasoning by combining hypothetical and theoretical machines, even if it can be initially confusing, is an excellent way to approach the theory of heat machines. The student is strongly encouraged to experiment in this way, for example by answering the following questions:

• Why does the best possible refrigerator operate reversibly?

• Why can’t we improve the efficiency of an engine by redirecting its heat rejection towards the hot source by use of a reversible heat pump?

(sec-7-3-3)=
### 7.3.3 Development of the Carnot cycle

:::{aside}
« But in order to draw truly advantageous results from high-pressure machines, it is necessary that the fall of the caloric in them be utilized as effectively as possible. It is not enough for the steam to originate at a high temperature: it must also be that by the expansion of its volume it reach a sufficiently low temperature. The mark of a good steam engine must therefore be not only to employ steam under a high pressure, but *to employ it under successive pressures that are highly-variable, greatly-different from one another, and progressively decreasing*. »

Sadi Carnot, 1824 [[4](#ref-4)]
:::

We have now seen that the maximum efficiency of a machine is reached when its operation is reversible. From this observation, Carnot reasoned as follows:

1. All thermal machines operate by the expansion and contraction of a substance alternately subjected to two temperatures;

2. For them to be reversible, namely, to ensure they can be carried out in the reverse direction, all heat transfers must be done with infinitesimal temperature differences: these processes will then be *isothermal*;

3. For them to be reversible, the phases where the substance changes temperature (in order to move from one heat reservoir to another) must occur without heat transfer: these processes will then be *adiabatic*.

4. In order to allow each process to be run backwards, they must all be *reversible* (infinitely slow).

The essentials are here. Carnot outlined a theoretical thermodynamic cycle which consists of two isothermal and two adiabatic processes. He did not need to quantify any transfer; and did not yet concern himself with any technological detail. However, it is certain that the thermodynamic cycle that he described is the most efficient –the least inefficient!– that can be realized.

(sec-7-3-4)=
### 7.3.4 The four stages of the Carnot engine

We can describe the *Carnot cycle* with a fixed amount of mass maintained inside a cylinder undergoing four processes (figure 7.8). It commutes between temperatures $T_{H}$ (“hot” source at high temperature) and $T_{L}$ (“cold” source at low temperature), in order to to produce a net work:

:::{figure} ../images/art-p183-1.svg
:alt: Illustration from the original text
:::

**Reversible adiabatic compression from 1 to 2**

In this stage, we aim to raise the temperature of the fluid to a high level without adding any heat to it.

The cycle starts at 1, when the fluid is in the cylinder at the low temperature $T_{L}$. In order to raise it to a high temperature (thus enabling a reversible heat transfer in the following phase $2 \rightarrow 3)$, the fluid is reversibly adiabatically compressed (§4.4.5 & §5.4.5). The fluid’s temperature increases from $T_{L}$ to $T_{H}$.

This phase requires work *input* $(W_{1\rightarrow 2}> 0)$.

**Isothermal heating from 2 to 3** In this stage, we aim to absorb a quantity $Q_{TH}$ of heat from the high-temperature source.

At 2, the fluid has been compressed in the piston at temperature $T_{H}$. The cylinder is brought into contact with the hot source (temperature $T_{H})$ and heat is supplied with an infinitesimal temperature difference: this is an isothermal expansion (§4.4.4 & §5.4.4). The fluid’s temperature remains constant at $T_{H}$.

This phase generates work output $(W_{2\rightarrow 3}< 0)$.

:::{figure} ../images/art-p184-2.svg
:alt: Illustration from the original text
:::

**Reversible adiabatic expansion from 3 to 4** In this stage, we aim to decrease the temperature of the fluid to that of the cold source $(T_{L})$.

At 3, the fluid is still at temperature $T_{H}$. The cylinder is then thermally isolated and the fluid is expanded in order to have the fluid do work and reduce its temperature without heat transfer: this is a reversible adiabatic expansion. The piston continues its slow retreat, and the fluid’s temperature decreases down to $T_{L}$.

This phase generates work output $(W_{3\rightarrow 4}< 0)$.

:::{figure} ../images/art-p184-3.svg
:alt: Illustration from the original text
:::

**Isothermal cooling from 4 to 1** In this final stage,

we aim to reject a quantity $Q_{TL}$ of heat into the low-temperature sink.

At 4, the fluid is at low temperature $T_{L}$. In order to bring it back to its initial volume, heat must be removed. We proceed with an isothermal cooling: the piston is gradually advanced, and the fluid’s temperature is kept constant at $T_{L}$.

This phase requires work input $(W_{4\rightarrow 1}> 0)$.

This quantity of work $W_{\mathrm{net}}$ represents the maximum that can be obtained from a quantity of heat $Q_{TH}$ between two given temperatures $T_{L}$ and $T_{H}$.

*Diagram* CC-0 *Olivier Cleynen*

:::{figure} ../images/fig-7-8.jpg
:label: fig-7-8
:enumerator: 7.8
:alt: The four stages of the Carnot engine, executed with a fixed mass quantity by separating them in time. The cycle is such that when the stages are performed in reverse order $(1 \rightarrow 4 \rightarrow 3 \rightarrow 2 \rightarrow 1)$, the transfers are exactly opposite.

The four stages of the Carnot engine, executed with a fixed mass quantity by separating them in time. The cycle is such that when the stages are performed in reverse order $(1 \rightarrow 4 \rightarrow 3 \rightarrow 2 \rightarrow 1)$, the transfers are exactly opposite.
:::

*Diagram* CC-0 *Olivier Cleynen*

:::{figure} ../images/fig-7-9.jpg
:label: fig-7-9
:enumerator: 7.9
:alt: The four stages of the Carnot engine, executed with a constant mass flow by separating them in space. Here too, the cycle is such that when the flow direction is reversed (becoming $1 \rightarrow 4 \rightarrow 3 \rightarrow 2 \rightarrow 1)$, the transfers are exactly opposite.

The four stages of the Carnot engine, executed with a constant mass flow by separating them in space. Here too, the cycle is such that when the flow direction is reversed (becoming $1 \rightarrow 4 \rightarrow 3 \rightarrow 2 \rightarrow 1)$, the transfers are exactly opposite.
:::

*Diagram* CC-by-sa *Olivier Cleynen*

The Carnot engine cycle can be plotted on a pressure-volume diagram (for example in figure 7.10 with a perfect gas). It can be observed that the compression phases occur at lower pressure and volume than the expansion phases: the cycle is work-producing. Since all processes are reversible, the area enclosed in the path 1-2-3-4-1 represents the net work quantity $W_{\mathrm{net}}$ produced.

:::{figure} ../images/fig-7-10.jpg
:label: fig-7-10
:enumerator: 7.10
:alt: Pressure-volume diagram of the Carnot engine performed with a perfect gas. The processes $2 \rightarrow 3$ and $4 \rightarrow 1$ are done at $T_{H}$ and $T_{L}$, respectively.

Pressure-volume diagram of the Carnot engine performed with a perfect gas. The processes $2 \rightarrow 3$ and $4 \rightarrow 1$ are done at $T_{H}$ and $T_{L}$, respectively.
:::

*Diagram* CC-0 *Olivier Cleynen*

:::{aside}
« To fully utilize the motive power that can be made available, the expansion would have to be carried out until the temperature of the steam was reduced to that of the condenser; but practical considerations, derived from the manner in which the motive power of heat is employed in the arts, prevent this limit from being reached. »

Émile Clapeyron, 1834 [[5](#ref-5)]
:::

The perceptive student will have observed that in order for all these phases to be reversible, the piston movement must be infinitely slow, and thus the fluid completes the cycle in an infinite amount of time. The Carnot engine therefore reaches maximum efficiency with infinitely low power.

````{prf:example}
:label: ex-7-1
:enumerator: 7.1

Perform a Carnot cycle between temperatures of $600^{\circ}C (1112 ^{\circ} F)$ and $100^{\circ}C (212 ^{\circ} F)$. Use $100 g (0.22 lb)$ of air trapped in a cylinder at a pressure of 1 bar. What amount of work must be invested? What is the work that will be recovered? What is the efficiency?

We start by raising the temperature to $600^{\circ}C$ with a reversible adiabatic process $(1 \rightarrow 2)$. The energetic cost for this will be $w_{1\rightarrow 2}= c_{v}\Delta T = 718\times (600-100) = +359 kJ kg^{-1}$ (equation 4/32) and $q_{1\rightarrow 2}= 0$. Equation 4/37 provides the final pressure: $p_{2}= p_{1}\left(\frac{T_{2}}{T_{1}}\right)^{\frac{\gamma}{\gamma -1}}= 1\times \left(\frac{600+273.15}{100+273.15}\right)^{\frac{1.4}{1.4-1}}= 19.6\,\mathrm{bar} = 284\,\mathrm{psi}$.

This phase’s sole purpose is to raise the temperature so that we can later absorb heat reversibly, which would be impossible if the gas temperature were below $600^{\circ}C$.

````

````{prf:example}

We can now absorb heat at constant temperature $(2 \rightarrow 3)$. We choose to expand the gas to $p_{3}= 4 bar$. Thus the heat transfer is $q_{2\rightarrow 3}= -R T_{2}\ln (\frac{p_{3}}{p_{2}} ) =$

$-287 \times (600 + 273.15) \times \ln ( \frac{4}{19.6}) = +398.2 kJ kg^{-1}$ (4/27, received by the gas) and the work is $w_{2\rightarrow 3}= -q_{2\rightarrow 3}= -398.2 kJ kg^{-1}$ (4/28, supplied by the gas).

A promise has been kept: we had studied isothermal processes in sections §4.4.4 and §5.4.4 precisely in order to be able to use them here…

The choice of the pressure $p_{3}$ or its corresponding volume $v_{3}$

is entirely arbitrary and does not affect any of the results obtained here.

We proceed with the expansion of the gas, aiming to recover as much work as possible and to reduce its temperature $(3 \rightarrow 4)$. The process is adiabatic, therefore $w_{3\rightarrow 4}= c_{v}\Delta T = -w_{1\rightarrow 2}= -359 J kg^{-1}$ and $q_{3\rightarrow 4}= 0$. Using equation 4/37 we obtain the final pressure: $p_{4}=$

:::{math}
\gamma
:::

$p_{3}(\frac{T_{4}}{T_{3}} )^{\gamma -1}= 0.2 bar = 2.9 psi$.

The work recovered from 3 to 4 is exactly opposite to the one invested from 1 to 2. In a Carnot cycle, it is during the heat transfers that the work leads to the production of a net work.

Finally, to bring the fluid back to its initial state (§6.2.1), we need to cool the gas $(4 \rightarrow 1)$. This cooling is done at constant temperature, so $q_{4\rightarrow 1}= -R T_{4}\ln (\frac{p_{1}}{p_{4}} ) = -170.2 kJ kg^{-1}$ (4/27, supplied by the gas) and the work is $w_{4\rightarrow 1}= -q_{4\rightarrow 1}= +170.2 kJ kg^{-1}$ (4/28, received by the gas).

It is a complex process for such an inglorious step: the rejection of unusable heat! Not only do we need to proceed infinitely slowly with significant volume fluctuations, but we also need to *invest* considerable work to return to 1.

What is the cycle’s balance? The compression phases required $w_{\mathrm{compression}}= w_{1\rightarrow 2}+ w_{4\rightarrow 1}= +529.2 kJ kg^{-1}$. In the expansion, we recovered $w_{\mathrm{expansion}}= w_{2\rightarrow 3}+ w_{3\rightarrow 4}= -757.2 kJ kg^{-1}$. The net work is $w_{\mathrm{net}}= w_{\mathrm{compression}}+ w_{\mathrm{expansion}}= -228 kJ kg^{-1}$; $W_{\mathrm{net}}= m w_{\mathrm{net}}= -22.8 kJ$.

We included the gas mass as late as possible. If we had studied a cycle carried out continuously as depicted in figure 7.9, we would only need to replace $m$ with$\dot{m}$ to obtain the sought powers in watts.

Compared to the recovered quantity, a substantial amount of work must be invested, an undesirable characteristic that will be quantified in chapter 10 (*air-based power cycles*) under the name of *work ratio* (10/1).

Although the cycle is already impracticable in reality, this meager efficiency is the greatest that can physically be attained between temperatures of $600^{\circ}C$ and $100^{\circ}C$.

We could also have carried out these calculations using a liquid/vapor instead of air: this would not have altered the final results.

````

(sec-7-3-5)=
### 7.3.5 Four stages or four strokes?

Piston engines are often classified according to their mode of operation. *Two-stroke engines* perform one expansion per crankshaft revolution (every two piston movements); whereas *four-stroke engines* (figure 6.14) perform one expansion every two revolutions. The distinction lies in the mode of exhaust gas removal and its replacement with fresh air (see §6.4 p. 163).

The transposition of the Carnot engine to reality, where eventually the fluid will need to be drained or transferred to a separate cylinder for cooling, can be done with either two or four strokes at the engineer’s discretion. Thus, the Carnot cycle, although it is indeed made up of four *stages*, cannot be specifically associated with either of these two modes of operation.

(sec-7-3-6)=
### 7.3.6 Carnot refrigerator

By reversing the operating direction of the engine described above, we create a refrigerator, air conditioner, or heat pump of the same efficiency. The fluid then passes through the same states, but by following the reverse path (1-4-3-2-1) as shown in figure 7.11. The heat $Q_{TL}> 0$ is *captured* from the cold source, the work $W_{\mathrm{net}}> 0$ is *received* by the machine, and the heat $Q_{TH}< 0$ is rejected by the machine towards the high-temperature source.

This cycle allows obtaining the maximum efficiency (the “least bad” ef-fi ciency, since it is not infinite) of an air conditioning system or a heat pump operating between two given temperatures $T_{H}$ and $T_{L}$.

:::{figure} ../images/fig-7-11.jpg
:label: fig-7-11
:enumerator: 7.11
:alt: Pressure-volume diagram for a reversed Carnot cycle, namely, in refrigeration mode (refrigerator or heat pump), with a perfect gas.

Pressure-volume diagram for a reversed Carnot cycle, namely, in refrigeration mode (refrigerator or heat pump), with a perfect gas.
:::

*Diagram* CC-0 *Olivier Cleynen*

(sec-7-4)=
## 7.4 Thermodynamic Temperature Scale

(sec-7-4-1)=
### 7.4.1 In a nutshell, for the impatient student

Kelvin defines a temperature scale, called *absolute temperature*. Within a Carnot engine, the ratio of the maximum temperature $T_{H}$ and minimum temperature $T_{L}$ is defined to be equal to the ratio of the heat transfer rates, that is:

:::{math}
:label: eq-7-4
:enumerator: 7/4
\left|\frac{\dot{Q}_{TH}}{\dot{Q}_{TL}}\right| \equiv \frac{T_{H}}{T_{L}}
:::

by definition, in a Carnot engine, where$\dot{Q}_{TH}$ is the heat transfer rate absorbed or rejected at high temperature $(\dot{Q}_{TL}$, at low temperature), and where the temperatures are absolute (measured in $K)$.

This equation 7/4 is a definition. Therefore, we can determine the temperature of a body without needing to use a specific fluid. Kelvin calibrates his scale such that $0^{\circ}C = 273.15 K$.

The rest of this section §7.4 details the path that led to this definition. It is intended for curious readers, and can be safely skimmed by busy students or engineers.

(sec-7-4-2)=
### 7.4.2 What is a scale in physics?

In order to quantify a property in physics (for example, quantify “mass” or “color”), three things must have been defined:

**A zero point** which defines what corresponds to zero property (zero mass, zero pressure, etc.);

**A standard** which serves as a reference gauge (for example, an object of one pound mass, one meter length);

**A scale** which allows to *define* the property between the zero point and the standard (for example, what is “twice as much” or “half as much” mass, light, etc.).

(sec-7-4-3)=
### 7.4.3 The limits of the Celsius and Fahrenheit

### thermometers

At the beginning of the 19th century, the two temperature scales that we use today in everyday life, those of the Swedish Anders Celsius and the German Daniel Gabriel Fahrenheit, were already in use. How are these scales defined from a physical point of view?

• The zero point is rather easy to define e (it is the point where bodies are completely frozen, unable to supply heat) but neither Fahrenheit nor Celsius could accurately locate it with certainty;

• The standards of Celsius and Fahrenheit differ significantly. Celsius chose the freezing point of pure water, Fahrenheit of saltwater, at atmospheric pressure, and each assigned it the relative “zero” graduation.

• However, the scales of Celsius and Fahrenheit are strictly identical. In fact, to *measure* temperatures around their standards, both scientists measured the contraction and expansion of a liquid in a tube. Between his relative zero point and the boiling point of water at atmospheric pressure, Celsius drew 100 graduations; Fahrenheit, 212 graduations. As always, the history of thermodynamics is full of trivia: Celsius initially used a reversed scale, going from $100$ at freezing to $0$ at boiling! As for Fahrenheit, he likely chose 212 graduations in order to easily realign with his *first* graduation, calibrated on the freezing point of pure water (32) and the temperature of the human body (96), standards that were quite difficult to reproduce. We must not let ourselves be distracted: in a physical sense, these are only graduations and not a scale, which was already determined by using a liquid thermometer.

The main problem with these two scales is that the temperature is well defined only in the range of existence of liquid thermometers. Whatever fluid is used (mercury, alcohol, water), it always ends up freezing or boiling at some point; and the graduations then no longer provide useful information. For example, Celsius could not *define e* or even describe what allows recognizing a temperature of $1200^{\circ}C$.

In addition to this, neither scale is intuitive in the negative range. If one were to admit, for example, that $40^{\circ}C$ could be “twice as much temperature” as $20^{\circ}C$, then what temperature would be twice as much as $-10^{\circ}C$? This amounts to asking the question: can we write $\frac{40^{\circ}C}{20^{\circ}C}$ and is it equal to $\frac{80^{\circ}C}{40^{\circ}C}$? As an inquisitive Scott would soon explain, the modern answer to this question is no.

(sec-7-4-4)=
### 7.4.4 William Thomson’s thermometer

Scottish physicist and engineer William Thomson understood these limitations very well. He proposed a temperature scale that does not depend on the behavior of a fluid in a tube.

Thomson took a keen interest in the Carnot cycle and reasoned as follows: the only characteristic that gives maximum efficiency to the Carnot engine is the fact that it is reversible. In other words, all machines based on this cycle and operating between two given temperatures will have the same efficiency — regardless of their fuel, displacement, configuration, or power. One could therefore use the efficiency of a Carnot engine as a measure of temperature.

:::{aside}
« …the absolute values of two temperatures are to one another in the proportion of the heat taken to the heat rejected in a perfect thermo-dynamic engine working with a source and refrigerator at the higher and lower of the temperatures respectively. »

William Thomson, 1854 [[15](#ref-15)]
:::

Thomson’s proposition is as follows: consider a body at a temperature $T_{1}$ (for example, a thousand units, as shown in figure 7.12). A Carnot engine is attached to it, which will supply work and reject heat at a lower temperature $T_{2}$. This temperature $T_{2}$ is half of $T_{1}$ if the engine rejects half of the heat it receives; it is one-fourth when it rejects one fourth, and so on. In mathematical terms, Thomson proposed:[^ch7-fn2]

:::{math}
\left|\frac{\dot{Q}_{TH}}{\dot{Q}_{TL}}\right| \equiv \frac{T_{H}}{T_{L}}
:::

[^ch7-fn2]: In fact, the records are again not that simple. Thomson initially proposed (in 1848 [[9](#ref-9)]) a scale in which $\frac{\dot{Q}_{TH}}{\dot{Q}_{TL}}$ is proportional to the *difference* of temperatures; making it a logarithmic scale from our current perspective. He revised this with the help of James Prescott Joule to arrive at proposition 7/4 six years later [[14](#ref-14)].

in a Carnot engine (actually, for any machine performing a reversible transformation), where$\dot{Q}_{TH}$ is the heat transfer rate absorbed or rejected at high temperature $(\dot{Q}_{TL}$, at low temperature), and where the temperatures are *absolute* (measured in $K)$.

:::{figure} ../images/fig-7-12.jpg
:label: fig-7-12
:enumerator: 7.12
:alt: Experiment illustrating the absolute temperature scale proposed by William Thomson. A Carnot engine operating between 1000 K and 500 K rejects 500 = 50 % of the heat it receives. If the low temperature is four times lower, this rejection is four times lower ( 1000 250 ) than the heat received.

Experiment illustrating the absolute temperature scale proposed by William Thomson. A Carnot engine operating between $1000 K$ and $500 K$ rejects
:::

$\frac{1000}{500} = 50 \%$ of the heat it receives. If the low temperature is four times lower, this rejection is four times lower ( $\frac{1000}{250}$ ) than the heat received. *Diagram* CC-0 *Olivier Cleynen*

By manipulating equations 7/4 and 7/1, we can reformulate Kelvin’s definition: a Carnot engine operating between reservoirs separated by one degree and supplied with one unit of heat defines the hot-source temperature as the inverse of the work it produces.

The temperatures in this scale, called the *absolute temperature* scale or *thermodynamic temperature* scale, are always positive and vary from zero to infinity.

(sec-7-4-5)=
### 7.4.5 Absolute zero and synchronization of scales

Thomson therefore had a *scale* — a method of defining a temperature as “twice as high”.

The zero of this scale corresponds well to the zero temperature point, since with the experiment in figure 7.12 one then has an “abyss” of zero temperature that allows gases to be infinitely expanded down to zero temperature (thus converting all the internal energy of a fluid into work).

There remained the choice of a standard. Thomson returned to Celsius’s thermometer and took the same reference point (the freezing point of pure water at atmospheric pressure). Observing that the contraction and expansion of fluids remain proportional to the change in their absolute temperature, he assigned a value to this reference point that allows maintaining the same thermometric scale as Celsius. For this, the temperatures $100^{\circ}C$ and $0^{\circ}C$, which are known to allow a maximum efficiency of $26.8 \%$, must correspond to temperatures in $K$ spaced by 100 units. The calculation is simple – the student is encouraged to reproduce it – and Thomson obtained the relation:

:::{aside}
« The particular convention is, that the difference of temperatures between the freezing- and boiling-points of water under standard atmospheric pressure shall be called 100 degrees. »

William Thomson, 1854 [[15](#ref-15)]
:::

:::{math}
:label: eq-7-5
:enumerator: 7/5
0^{\circ}C = 273.15 K
:::

William Thomson, already embarked on a stunning scientific career, was thirty years old when he published his temperature scale in 1854. In 1892, he was ennobled as *First Baron Kelvin* (he even ought to write *The Right Honourable First Lord Kelvin of Largs, of the Order of Merit, the Royal Victorian Order, and of Her Majesty’s Most Honourable Privy Council*!); it is under this name that he is known today. The *Kelvin* unit $(K)$ was officially assigned to absolute temperature in 1948.

Kelvin’s work thus definitively separated the concept of temperature from real or imaginary fluids as previously done with the boiling point of water or the volume of perfect gases (§1.4.1 & §4.1.1); from here on it would be linked to a specific and quantitative physical experience.

````{prf:example}
:label: ex-7-2
:enumerator: 7.2

In order to illustrate the nature of the Kelvin scale, we carry out the following conceptual experiment. We have a Carnot engine and a standard: a solid titanium block that we know melts at $1668^{\circ}C$. We operate the machine between the standard temperature and an object whose temperature we want to measure. The machine absorbs $200 W$ and produces $45 W$ as work. What is the temperature of the object?

$T_{B}= -\frac{Q_{\mathrm{out}}}{\dot{Q}_{\mathrm{in}}} T_{H}= -\frac{-155}{200} (1668 + 273.15) = 1504.4 K = 1231.2^{\circ}C$.

````

````{prf:example}

Here we see that Kelvin used the Carnot engine as a thermometer. In order to construct the scale, he carried out this experiment between the two standards of $100^{\circ}C$ and $0^{\circ}C$, and ensured they were separated by one hundred intervals in absolute units.

````

(sec-7-5)=
## 7.5 Maximum Efficiency of Machines

The final definition of temperature in 7/4 allows us to return to thermal machines and provide a simple answer to the questions raised by Carnot.

(sec-7-5-1)=
### 7.5.1 Efficiency of the Carnot engine

In the previous chapter (§6.3.2), we saw that the efficiency of an engine was the ratio between the work produced (useful transfer,$\dot{W}_{\mathrm{net}})$ and the heat received (energy expenditure,$\dot{Q}_{\mathrm{in}})$. We had transformed this expression into another that was perhaps less demonstrative:

:::{math}
\eta _{\mathrm{engine}}= 1 - \left|\frac{\dot{Q}_{TL}}{\dot{Q}_{TH}}\right|
:::

for any thermal engine.

In the case of a Carnot engine, with relation 7/4, this expression makes sense by becoming:

:::{math}
:label: eq-7-6
:enumerator: 7/6
\eta _{\mathrm{Carnot} \mathrm{engine}}= 1 - \frac{T_{L}}{T_{H}}
:::

for a reversible thermal engine, and where the temperatures are absolute $(K)$.

This expression 7/6 is so remarkable that we must pause for a moment.

The answer to the question Carnot was asking, “what is the maximum amount of work, in theory, that can be obtained from the combustion of a given amount of coal?” is here – and it is astonishing: **it depends only on the high and low temperatures of the engine**!

Two important remarks are necessary here.

• First, this efficiency is not $100 \%$. Yet, we are discussing machines here without friction or leaks, and with infinitely slow movements. By contrast, if we can ignore all practicalities, nothing is there to prevent an electric motor or an alternator from reaching an efficiency of $100 \%$.

Therefore, even before addressing the inevitable technological difficulties associated with designing a real-world machine, the engine designer is limited by the fundamental nature of heat in what he or she can obtain from their machine. In the following chapters, we will address the irreversibilities observed in real engines, which will further reduce the efficiency calculated above.

• Secondly, this equation is a strong argument for increasing the combustion temperature in engines.

In practice, the low temperature $T_{L}$ is limited by the ambient air temperature. The only remaining parameter to increase the efficiency of an ideal engine is the temperature $T_{H}$. This relationship explains the surprising efforts made by engine designers to use high temperatures (and correspondingly, high pressures), even though real engines are far from reversible.

:::{aside}
« Thus we are led to establish the following general proposition: *The motive power of heat is independent of the agents employed to produce it; its quantity is determined solely by the temperatures of the bodies between which, as the final result, the transport of caloric takes place.* »

Sadi Carnot, 1824 [[4](#ref-4)]
:::

:::{aside}
« …our aim must always be *to raise the temperatures and pressures to the highest working limit*. »

Rudolf Diesel, 1893 [[23](#ref-23), [24](#ref-24)]
:::

In summary, we can answer Carnot’s question as follows: heat loss from the engine (wasted energy) is fundamentally inevitable. The losses are minimized, but not avoided, when the temperature at which the coal is burned is high, and the ambient temperature is low.

````{prf:example}
:label: ex-7-3
:enumerator: 7.3

The maximum achievable temperature in an engine is $600^{\circ}C (1112 ^{\circ} F)$, and the temperature at which exhaust gases are discharged is $100^{\circ}C (212 ^{\circ} F)$. What is the maximum efficiency achievable by the engine?

In order to achieve the most efficient conversion, the engine must be reversible. Thus, with equation 7/6: $\eta _{\mathrm{engine}}= \eta _{\mathrm{Carnot} \mathrm{engine}}= 1 - \frac{T_{L}}{T_{H}} = 1 - \frac{100+273.15}{600+273.15}= 57.3 \%$.

Make sure to use absolute temperatures here – at this point, using $degrees Celsius$ or $Fahrenheit$ in the calculation would be unforgivable.

The technological specifics of the engine (displacement, injection method, etc.) may possibly bring it close to $57.3 \%$, but will never bring it beyond that value.

We have indeed found the result obtained previously in example 7.1 p. 188, with a much simpler calculation.

````

(sec-7-5-2)=
### 7.5.2 Efficiency of the Carnot refrigerator

We saw in §6.3.3 that the efficiency of a refrigerator is the comparison between the heat extracted from the cold source (useful transfer,$\dot{Q}_{\mathrm{in}})$ and the work input (energy expenditure,$\dot{W}_{\mathrm{net}})$. We had expressed this efficiency with the obscure expression:

:::{math}
:enumerator: 6/7
\eta _{\mathrm{refrigerator}}= \frac{1}{\left|\dfrac{\dot{Q}_{TH}}{\dot{Q}_{TL}}\right| - 1}
:::

for all refrigerators.

When it comes to a Carnot refrigerator, this efficiency is a function of temperature only (7/4) and thus we have:

:::{math}
:label: eq-7-7
:enumerator: 7/7
\eta _{\mathrm{Carnot\ refrigerator}}= \frac{1}{\dfrac{T_{H}}{T_{L}} - 1}
:::

for a reversible refrigerator, where temperatures are absolute $(K)$.

The same remarks as above apply here: firstly, the efficiency of a refrigerator or an air conditioner never reaches infinity (an infinite cop refrigerator would operate without any work input). Secondly, this efficiency reduces when the refrigeration temperature $T_{L}$ is reduced. In other words, when cooling an object with an ideal refrigerator, selecting a lower temperature is more expensive, not merely because more heat needs to be extracted from the object, but also because the efficiency of the extraction decreases.

````{prf:example}
:label: ex-7-4
:enumerator: 7.4

A refrigerator must bring the cold chamber to $5 ^{\circ} F (-15^{\circ}C)$ in a room at $77 ^{\circ} F (25^{\circ}C)$. What is the maximum achievable efficiency?

The maximum efficiency would be achieved with a reversible refrigerator, allowing us to obtain, with equation 7/7, $\eta _{\mathrm{refrigerator}}= \eta _{\mathrm{Carnot\ refrigerator}}= \dfrac{1}{\dfrac{T_{H}}{T_{L}}-1} = \dfrac{1}{\dfrac{25+273.15}{-15+273.15}-1} = 6.45$.

By carrying out the same calculation between temperatures of

$365 ^{\circ} F$ and $437 ^{\circ} F (185^{\circ}C$ and $225^{\circ}C)$, we obtain an efficiency of $11.45$: this depends not only on the temperature difference but also on their absolute values.

````

(sec-7-5-3)=
### 7.5.3 Efficiency of the Carnot heat pump

We saw in §6.3.4 that the efficiency (or Coefficient of Performance, cop) of a heat pump is defined as the ratio of the heat supplied at high temperature to the work input (6/8). We had then transformed this definition with the expression:

:::{math}
:enumerator: 6/9
\eta _{\mathrm{heat\ pump}}= \frac{1}{1 - \left|\dfrac{\dot{Q}_{TL}}{\dot{Q}_{TH}}\right|}
:::

for all heat pumps.

Using relation 7/4, when the machine is reversible, we can express this efficiency solely based on the high and low temperatures:

:::{math}
:label: eq-7-8
:enumerator: 7/8
\eta _{\mathrm{Carnot\ heat\ pump}}= \frac{1}{1 - \dfrac{T_{L}}{T_{H}}}
:::

for a reversible heat pump, where temperatures are absolute $(K)$.

As with a refrigerator, the cop of a heat pump cannot be infinite: it is bounded by the extreme temperatures reached in the cycle. The higher the temperature at which heat $Q_{\mathrm{out}}$ is delivered, and the lower the efficiency that can be achieved.

````{prf:example}
:label: ex-7-5
:enumerator: 7.5

A heat pump is used to heat water to $120^{\circ}C (248 ^{\circ} F)$ in an environment at $-5^{\circ}C (23 ^{\circ} F)$. What is the maximum achievable efficiency?

The maximum efficiency would be achieved with a reversible heat pump, allowing us to obtain, with equation 7/8, $\eta _{\mathrm{heat} \mathrm{pump}}= \eta _{\mathrm{Carnot} \mathrm{heat} \mathrm{pump}}= \frac{1}{1- T_{L}/T_{H}} = \frac{1}{1-\frac{-5+273.15}{120+273.15}}= 3.15$.

````

::::{admonition} A Bit of History
:class: note
:label: hist-7-11

**Rudolf Diesel's Dream**

This is the story of an engine born in the margin of thermodynamics lecture notes. “*Kann man Dampfmaschinen konstruieren, welche den vollkommenen Kreisprozess ausführen, ohne zu sehr kompliziert zu sein?*”: can we build steam engines that can perform the ideal cycle without being too very complex? The student Rudolf Diesel asked himself this question in the margin of his notes in 1878 in Munich, realizing that the engine cycle followed by the steam engines of his time inevitably condemned them to mediocre efficiencies.

In this way, the concept of a *rational heat engine* would mature over the years, an engine whose characteristics were finally published in 1893 [[23](#ref-23), [24](#ref-24)]. Rudolf Diesel is unequivocal: “an examination of their operating theory will show that gas and air engines operate on a defective principle, and no improvement will produce better results as long as this principle is retained”. He was no kinder to the designers of steam engines. The main features of the proposed engine strictly stemmed from physical precepts: it was about getting as close as possible to the Carnot cycle, by “*producing the highest temperature of the cycle (the combustion temperature) not through and during combustion, but before and independently of it, entirely through the compression of ordinary air*”. This was followed by combustion at constant temperature, controlled by progressive fuel injection. Only the exhaust and intake (done at constant pressure with a four-stroke cycle) deviated from the Carnot cycle.

The characteristics announced on paper give food for thought: the maximum compression pressure must be at least $p_{2}= p_{1}(\frac{T_{\mathrm{combustion}}}{T_{\mathrm{initial}}} )^{\gamma -1}$ (equation 4/37), which lead Rudolf Diesel to $300 bar (4350 psi)$ – twenty times more than existing engines! The concept of direct injection, which is made necessary by the high temperatures reached during compression to avoid premature combustion, is convincing. However, many details were lacking on how to handle coal dust – the fuel chosen by Rudolf Diesel for its abundance and low cost – so as to allow its direct injection into the cylinders in practice.

:::{figure} ../images/fig-7-13.jpg
:label: fig-7-13
:enumerator: 7.13
:alt: Rudolf Diesel in 1883.

Rudolf Diesel in 1883.
:::

*Photo by unknown author (public domain)*

Despite everything, Rudolf Diesel, after a promising start in the design of refrigeration systems, managed to convince the *Maschinenfabrik Augsburg-Nürnberg* company, known today as man, to finance his research. They would be challenging: the transition from theory to practice took four years. Many ambitions were scaled back: the maximum pressure decreased to $90$ and then $40 bar (580 psi)$, the coal dust was abandoned in favor of a crude oil for easier handling. Since the structural limits of the engine constrained the cycle, the isothermal combustion was replaced by isobaric at maximum pressure. The second prototype, a single-cylinder engine nearly three meters tall (figure 7.14), was the first to operate autonomously: eight minutes in February 1894. The performance of the third prototype (figure 7.15) was independently measured in 1897: $17 hp$ at $154 rpm$, and an efficiency of $26.2 \%$.

This efficiency was twice that of its contemporaries with internal combustion, and four times that of the best steam engines!

Man quickly started sales of the *rational engine*, renamed as *Diesel engine*, which gradually met success in Europe. Its operational regularity, reliability, and especially its low fuel consumption justified its significant purchase cost: due to the materials and precision manufacturing it required, its price per watt of power was about three times higher than its competitors. The patents filed by Rudolf Diesel brought him a significant income.

The numerous documents left behind make Diesel a compelling figure: cultivated, diligent, and intelligent (he excelled in all his studies), he had a very keen perception of the economic and social upheavals caused by the rapid mechanization of industry and transportation at the end of the 19th century [[33](#ref-33), [34](#ref-34), [41](#ref-41)]. After a harsh and miserable childhood, expelled from France and then England, he nurtured a strong social ideal that lead him to write *Solidarismus* (“*the rational and economic salvation of humanity*”, 1903 [[25](#ref-25)]). For him, the decentralization of mechanical power production, for small businesses or collectives, for example, would constitute a decisive social advancement.

Despite the remarkable success achieved in fifteen years, Rudolf Diesel struggled to find fulfillment. He was constantly the target of legal disputes, since his critics and competitors argued – not entirely without merit – that the engines he commercialized were ultimately very different from the machine described in his patent. The nationalist tensions leading up to the outbreak of World War I shook him. A poor financial manager, he made multiple unreasonable expenses and ruinous investments, and, to top it all, he was plagued by severe migraines and medical problems. In 1913, the man seemed tormented by his own ethical and philosophical questions. His engines exclusively produced power in factories and power plants: did they ultimately contribute to the emancipation or the servitude of the working classes? He ended his life in September.

The tragic disappearance of its creator would not suffice to slow down the progression of the Diesel engine. The technological obstacles to its adoption in transportation, in particular the delicate fuel injection system, were overcome one by one.

:::{figure} ../images/fig-7-14.jpg
:label: fig-7-14
:enumerator: 7.14
:alt: The second prototype developed at man by Rudolf Diesel, and the first to operate independently, in February 1894. It has only one cylinder with a diameter of $22 cm$, and the direct fuel injection is done by a compressed air circuit. The engine is now exhibited at the headquarters of the man company.

The second prototype developed at man by Rudolf Diesel, and the first to operate independently, in February 1894. It has only one cylinder with a diameter of $22 cm$, and the direct fuel injection is done by a compressed air circuit. The engine is now exhibited at the headquarters of the man company.
:::

*Photo* CC-by-sa *MAN SE*

:::{figure} ../images/fig-7-15.jpg
:label: fig-7-15
:enumerator: 7.15
:alt: Diesel's third prototype, and his first operational engine. The cylinder diameter was $25 cm$ and the stroke reached $40 cm$. It would be tested at the technical university of Munich where it achieved $26.2 \%$ efficiency in 1897. It is exhibited at the *Deutsches Museum*.

Diesel's third prototype, and his first operational engine. The cylinder diameter was $25 cm$ and the stroke reached $40 cm$. It would be tested at the technical university of Munich where it achieved $26.2 \%$ efficiency in 1897. It is exhibited at the *Deutsches Museum*.
:::

*Photo* CC-by-sa *Olivier Cleynen*

:::{figure} ../images/fig-7-16.jpg
:label: fig-7-16
:enumerator: 7.16
:alt: A nine-cylinder Sulzer RTA76 Diesel engine producing $25 MW$ of power at $95 rpm$. This unit is installed here in a factory but the model is commonly used to propel merchant ships.

A nine-cylinder *Sulzer RTA76* Diesel engine producing $25 MW$ of power at $95 rpm$. This unit is installed here in a factory but the model is commonly used to propel merchant ships.
:::

*Photo* CC-by-sa *by de:Wikipedia User:Sleipnir*

Today, it is used wherever constraints of economy and durability take precedence over lightness and responsiveness. In merchant ships, Diesel engines several stories high operate on highly turbocharged two-stroke cycles. In these engines exceeding 2000 tons and $18 000 hp$ (figure 7.16), the cylinders move slowly on strokes of over two meters, allowing for nearly isothermal combustion at $80 rpm$ and an efficiency exceeding $50 \%$.

At the other end of the spectrum, Diesels powering the smallest utility vehicles benefit from numerous systems to increase their responsiveness and extend their power and torque ranges. In these tiny machines of $80 hp$ rotating beyond $2000 rpm$, electronic control systems perform up to four fuel injections at 2000 bar directly into the cylinder for each combustion, optimizing combustion based on the demanded power [[46](#ref-46)].

Ultimately, there is probably not a product in today's industry that we manufacture whose materials or components have not been extracted, assembled, and transported without the contribution of power from a Diesel engine. A great achievement for a curious student!

::::

## Problems

The properties of water are tabulated in Steam Tables 1, 2, and 3 (see Appendix A1 p. 305)

Air is considered an ideal gas.

$c_{v (\mathrm{air})}= 718 J kg^{-1}K^{-1} \qquad R_{\mathrm{air}}= 287 J kg^{-1}K^{-1}$

$c_{p (\mathrm{air})}= 1005 J kg^{-1}K^{-1} \qquad \gamma _{\mathrm{air}}= 1.4$

We assume that for a reversible adiabatic process (without heat transfer and infinitely slow), the properties of air are linked according to the following three relationships:

:::{math}
\left(\frac{T_{1}}{T_{2}}\right) = \left(\frac{v_{2}}{v_{1}}\right)^{\gamma -1} \qquad (4/36)
:::

:::{math}
\left(\frac{T_{1}}{T_{2}}\right) = \left(\frac{p_{1}}{p_{2}}\right)^{\frac{\gamma -1}{\gamma}} \qquad (4/37)
:::

:::{math}
\left(\frac{p_{1}}{p_{2}}\right) = \left(\frac{v_{2}}{v_{1}}\right)^{\gamma} \qquad (4/38)
:::

We also assume that during a reversible isothermal process (at constant temperature and infinitely slow) of an ideal gas, the work done in an open or closed system is:

:::{math}
w_{1\rightarrow 2}= RT_{\mathrm{cst}.}\ln \left(\frac{p_{2}}{p_{1}}\right) = RT_{\mathrm{cst}.}\ln \left(\frac{v_{1}}{v_{2}}\right) \qquad (4/29)
:::

Finally, we assume that the efficiencies of thermal machines based on a Carnot cycle are expressed as a function of the absolute temperatures as follows:

:::{math}
\eta _{\mathrm{Carnot\ engine}}= 1 - \frac{T_{L}}{T_{H}} \qquad (7/6)
:::

:::{math}
\eta _{\mathrm{Carnot\ refrigerator}}= \frac{1}{\dfrac{T_{H}}{T_{L}} - 1} \qquad (7/7)
:::

:::{math}
\eta _{\mathrm{Carnot\ heat\ pump}}= \frac{1}{1 - \dfrac{T_{L}}{T_{H}}} \qquad (7/8)
:::

```{exercise}
:label: prob-7-1
:enumerator: 7.1

**Maximum Efficiency of an Engine** What is the maximum efficiency that a steam power plant can reach when operating in the atmosphere at room temperature $(15^{\circ}C$ or $59^{\circ} F)$, with a maximum temperature of $800^{\circ}C (1472^{\circ} F)$?

:::{admonition} Answer
:class: dropdown

$\eta _{\max.}= 73.1\%$ (eq. 7/6, see example 7.3 p. 196).

:::
```

```{exercise}
:label: prob-7-2
:enumerator: 7.2

**Maximum Efficiency of a Refrigerator** What is the theoretical maximum efficiency that a household freezer could reach when operating between temperatures of $-6^{\circ}C$ and $20^{\circ}C (21.2^{\circ} F$ and $68^{\circ} F)$? For what reason(s) is the cop reached by conventional freezers (around $3)$ lower than this value?

:::{admonition} Answer
:class: dropdown

1) $\mathrm{cop}_{\max.}= 10.3$ (eq. 7/7, see example 7.4 p. 197);
2) Non-reversible compressions and expansions (thus $w_{4\rightarrow 3}+ w_{2\rightarrow 1}> 0$), especially if a valve is used (§6.2.3); Non-isothermal heat transfers.

:::
```

```{exercise}
:label: prob-7-3
:enumerator: 7.3

**Maximum Efficiency of a Heat Pump** A person wants to install a heat pump to heat their home with a power of $10 kW$. 1. Explain briefly why the performance of a heat pump is expressed as:

:::{math}
:enumerator: 7/9
\eta _{\mathrm{heat\ pump}}= \left|\frac{\dot{Q}_{\mathrm{out}}}{\dot{W}_{\mathrm{net}}}\right|
:::

2. Estimate the theoretical minimum consumption of the pump on a very cold evening $(T_{\mathrm{ext}.}= -12^{\circ}C = 10.4 ^{\circ} F$; $T_{\mathrm{int}.}= 20^{\circ}C = 68 ^{\circ} F)$. 3. What will be the minimum consumption of the heat pump when the internal and external temperatures are $17^{\circ}C$ and $16^{\circ}C$ respectively? 4. What will be the theoretical minimum consumption of the heat pump in the case where the internal and external temperatures are identical? What happens in theory if the external temperature is higher than inside?**

:::{admonition} Answer
:class: dropdown

1) see §6.3.4;
2) $\dot{W}_{\mathrm{net}}= \frac{\dot{Q}_{\mathrm{out}}}{\eta _{\max.}} = +1.09 kW$;
3) $\dot{W}_{\mathrm{net}}= +34.5 W$ (!), $\dot{W}_{\mathrm{net}}= 0 W$; and when $T_{\mathrm{ext}.}> T_{\mathrm{int}.},\dot{W}_{\mathrm{net}}$ becomes negative: the heat pump operates as an engine…

:::
```

```{exercise}
:label: prob-7-4
:enumerator: 7.4

**Carnot Cycle** Since this cycle plays a central role in thermodynamics, it is useful to be able to describe it precisely: 1. Describe briefly the four phases of a Carnot engine cycle, describing the direction of heat transfers. 2. Why are heat transfers isothermal? 3. Is it preferable to use a perfect gas or a liquid-vapor mixture to perform this cycle? 4. What practical problems does the Carnot cycle pose?

:::{admonition} Answer
:class: dropdown

1) see §7.3.4, especially figures 7.8 and 7.9;
2) see §7.3.3;
3) It doesn't matter at all!
4) Its volume and its power ratio are very large, and its power is infinitely small…

:::
```

```{exercise}
:label: prob-7-5
:enumerator: 7.5

**Carnot Steam Engine An attempt is made to set up a steam power plant based on the Carnot cycle to generate electricity (figure 7.17). The boiler operates at a maximum temperature of $527 ^{\circ} F (275^{\circ}C)$ and admits water in the state of saturated liquid. When the water leaves the boiler and enters the turbine, it is in the state of saturated vapor. 1. Draw the processes undergone by the water during one cycle on a pressure-volume diagram, qualitatively (that is, without showing numerical values). 2. At what pressure would the water need to be cooled to achieve an efficiency of $40 \%$? 3. What would be the power supplied by the plant if its mass flow rate was $9 kg s^{-1}(19.8 lb/s)$? 4. What would the cycle and the machine look like if the steam were to be further heated at a constant temperature of $527 ^{\circ} F$ at the outlet of the boiler? How would the efficiency of the engine vary then? *Diagram* CC-by-sa *Olivier Cleynen***

:::{admonition} Answer
:class: dropdown

We see that when performed under the saturation curve, the Carnot cycle is already easier to perform in practice, since heat transfers occur at constant pressure (and thus do not require a moving part);
2) $T_{B}= (1 - \eta)T_{H}= 55.74^{\circ}C$; thus by interpolation between $55$ and $60^{\circ}C$ we get $p_{\mathrm{sat}. 55.74^{\circ}C}= 0.1285 bar$. The condenser is thus depressurized;
3) $q_{\mathrm{in}}= h_{\mathrm{LV} 275^{\circ}C}= +1574.3 kJ kg^{-1}$: we obtain $\dot{W}_{\mathrm{net}}= -\dot{m}\eta q_{\mathrm{in}}= -566.7 kW$;
4) The power ratio and the complexity of the machine will increase, but the efficiency will remain unchanged!

:::
```

   :::{figure} ../images/fig-7-17.jpg
   :label: fig-7-17
   :enumerator: 7.17
   :alt: Schematic representation of a steam power plant operating with the Carnot cycle.
   
   Schematic representation of a steam power plant operating with the Carnot cycle.
   :::

```{exercise}
:label: prob-7-6
:enumerator: 7.6

**Reversibility of Machines** Briefly show that it is impossible to design a heat pump with efficiency higher than that achieved by a reversible machine, for example in the same way we did with an engine in fig. 7.7 p. 183.

:::{admonition} Answer
:class: dropdown

A heat pump like this could be powered by a Carnot engine; together, they would form a machine capable of carrying heat from $T_{L}$ to $T_{H}$ without the need for external work (with the arbitrary values shown here, $\dot{Q}_{\mathrm{out\ together}}= -40 W$).

:::
```

```{exercise}
:label: prob-7-7
:enumerator: 7.7

**Ideal Turbine Engine A group of engineers in an engineering company is working on an air engine concept, operating in a steady-flow state using turbines and compressors. The engineers are using the Carnot cycle as a starting point. They plan to be able to supply heat at a temperature of $600^{\circ}C$ and reject heat at a temperature of $20^{\circ}C$. The pressure is 1 bar at the inlet of the adiabatic compressor and 30 bar at the inlet of the adiabatic turbine. These characteristics give the engine a specific net power of $70 kJ kg^{-1}$. 1. Represent schematically the general arrangement of this hypothetical engine, showing the path followed by the air, and all heat and work transfers. 2. Starting from the definition of the efficiency of an engine, show that the efficiency of a reversible engine can be quantified by the equation $\eta _{\mathrm{Carnot\,engine}}= 1 - \dfrac{T_{L}}{T_{H}}$ (equation 7/6) 3. What power will need to be supplied to the engine in the form of heat? 4. What will be the power rejected in the form of heat? Of course, the Carnot cycle is impractical in an industrial application and the group of engineers immediately adopts a modification. In order to be able to supply heat by internal combustion, it is necessary to later vent the air from the engine. Thus, in the modified engine, the expansion in the adiabatic turbine is interrupted when the pressure reaches 1 bar, and the “used” air is then rejected into the atmosphere. The rest of the engine is not affected. 5. Draw the new engine cycle on a pressure-volume diagram, qualitatively, comparing it to that of the Carnot cycle. 6. What is the temperature of the air when it is rejected from the engine? 7. What is the reduction in power of the adiabatic turbine compared to the ideal engine? 8. What amount of power is saved by removing the compressor that was rejecting heat? 9. What is now the efficiency of the engine?**

:::{admonition} Answer
:class: dropdown

1) This is the arrangement shown in fig. 7.9 p. 187;
2) By starting from the definition 6/4: $\eta _{\mathrm{engine}}\equiv \left|\frac{\dot{W}_{\mathrm{net}}}{\dot{Q}_{\mathrm{in}}}\right| = -\frac{\dot{W}_{\mathrm{net}}}{\dot{Q}_{\mathrm{in}}} = -\frac{-\dot{Q}_{\mathrm{in}}-\dot{Q}_{\mathrm{out}}}{\dot{Q}_{\mathrm{in}}} = 1+\frac{\dot{Q}_{\mathrm{out}}}{\dot{Q}_{\mathrm{in}}} = 1-\left|\frac{\dot{Q}_{\mathrm{out}}}{\dot{Q}_{\mathrm{in}}}\right| = 1-\left|\frac{\dot{Q}_{TH}}{\dot{Q}_{TL}}\right|$; with definition eq. 7/4 p. 192 we arrive at the requested equation 7/6;
3) $q_{\mathrm{in}}= -\frac{w_{\mathrm{net}}}{\eta _{\mathrm{engine}}} = +105.4 kJ kg^{-1}$;
4) $q_{\mathrm{out}}= -w_{\mathrm{net}}- q_{\mathrm{in}}= -35.4 kJ kg^{-1}$;
6) The isothermal compressor is removed, the adiabatic turbine is truncated. $T_{E}= T_{C}(\frac{p_{E}}{p_{C}} )^{\frac{\gamma -1}{\gamma}} = 330.4 K = 57.3^{\circ}C$ (eq. 4/37);
7) $w_{\mathrm{lost}}= w_{\mathrm{isentropic} \mathrm{turbine} 1}- w_{\mathrm{isentropic} \mathrm{turbine} 2}= -37.54 kJ kg^{-1}$;
8) $w_{\mathrm{saved}}= w_{\mathrm{isentropic} \mathrm{compressor}}= +35.4 kJ kg^{-1}$;
9) $\eta _{\mathrm{engine} 2}= 64.4 \%$, which is a -2 point change,
very honorable given the considerable simplification of the machine!

:::
```

```{exercise}
:label: prob-7-8
:enumerator: 7.8

**Irreversibilities in a Refrigerator We propose to study the operation of a refrigerator starting from a theoretical cycle allowing for maximum efficiency. The refrigerator operates strictly on a Carnot cycle, in a steady-flow state, with a liquid-vapor mixture. 1. Represent the refrigeration cycle on a pressure-volume diagram, indicating the direction of heat and work transfers. Of course, in practice, adiabatic compression and expansion cannot be carried out reversibly. 2. Represent the irreversible cycle on the pressure-volume diagram. 3. How will each of the heat and work transfers vary compared to the theoretical case? 4. Briefly show that these changes lead to a decrease in the efficiency (the cop) of the refrigerator.**

:::{admonition} Answer
:class: dropdown

3) $w_{1\rightarrow 4}$ decreases, $w_{4\rightarrow 3}$ and $w_{3\rightarrow 2}$ increase, $w_{2\rightarrow 1}$
decreases; $q_{3\rightarrow 2}$ increases and $q_{1\rightarrow 4}$ decreases;
4) Since $w_{\mathrm{net}}$ increases and $q_{\mathrm{in}}= q_{1\rightarrow 4}$ decreases,
the cop $= \frac{q_{\mathrm{in}}}{w_{\mathrm{net}}}$ necessarily decreases.

:::
```

```{exercise}
:label: prob-7-9
:enumerator: 7.9

**Refrigeration in Stages A chemical plant uses a refrigeration system to control the temperature of hazardous products. We aim to study the least inefficient refrigeration system to equip it, here based on the Carnot cycle with a perfect gas. The minimum refrigeration temperature is $-50^{\circ}C$ and the heat is rejected at $40^{\circ}C$. While studying the characteristics of the Carnot cycle, a beginner engineer observes that the efficiency of the refrigerator increases if the heat rejection temperature is lowered (eq. 7/7 p. 196). S/he proposes to configure the refrigerator in such a way that it rejects heat at only $10^{\circ}C$. This heat at $10^{\circ}C$ would then be captured by a heat pump which would in turn bring it to $40^{\circ}C$. 1. Show that if the refrigerator operates on a reversible cycle, the proposed modification can only increase (or at best, keep the same) the total consumption of the refrigeration system. 2. Draw the cycle of the refrigerator and of the heat pump as proposed by the engineer on the same pressure-volume diagram, qualitatively. 3. Draw, on a pressure-volume diagram, the cycles that would be followed in the two machines if their expansion phases were adiabatic (without heat transfer), but non-reversible.**

:::{admonition} Answer
:class: dropdown

Let’s bet that the student did better than the beginner engineer in the problem: with two reversible systems in series pumping a quantity
$q_{\mathrm{in}}$ of heat at temperature $T_{1}= -50^{\circ}C$, with exchange temperature $T_{2}= 10^{\circ}C$ and final high temperature $T_{3}= 40^{\circ}C$, the necessary work
is $w_{\mathrm{total}}= w_{\mathrm{net}1}+ w_{\mathrm{net}2}= \eta _{1}q_{\mathrm{in}}+ \eta _{2}(q_{\mathrm{in}}+ w_{\mathrm{net}1})= \left(\frac{T_{2}}{T_{1}} - 1\right)q_{\mathrm{in}}+ \left(\frac{T_{3}}{T_{2}} - 1\right)\left(q_{\mathrm{in}}+ \left(\frac{T_{2}}{T_{1}} - 1\right)q_{\mathrm{in}}\right)= \left(\frac{T_{3}}{T_{1}} - 1\right)q_{\mathrm{in}}$, which is the work (and thus the ineffi
ciency of a single reversible machine operating between $T_{1}$ and $T_{3}$. Stacking two machines in series therefore brings no theoretical advantage.

:::
```

```{exercise}
:label: prob-7-10
:enumerator: 7.10

**Gasoline Engine Based on a Carnot Cycle We aim to quantify the minimum gasoline consumption that could result from a piston-cylinder automotive engine generating $100 kW$ of power (about $130 hp)$, given some practical constraints imposed by the limited available volume and weight limits: • The compression ratio (namely, the ratio $\frac{v_{\max.}}{v_{\min.}}$ ) is $12$ during the adiabatic phases (to limit mechanical constraints); • The maximum temperature is $1300 K$ (imposed by material resistance); • The engine has four cylinders, each performing $400$ cycles per minute. The engine is fueled by gasoline with a specific heat of combustion of $40 MJ kg^{-1}$. If we consider the best engine that can be designed: 1. At what temperature would the heat be rejected? 2. What would be the efficiency of the engine? 3. What would be the amount of heat to be supplied for each combustion, and the corresponding fuel mass? 4. What would be the hourly gasoline consumption?**

:::{admonition} Answer
:class: dropdown

1) At the outlet, $T_{1}= 208^{\circ}C$ (eq. 4/37);
2) $\eta _{\mathrm{engine}}= 63 \%$;
$3)\dot{Q}_{\mathrm{in}}= 158.8 kW$ so $Q_{\mathrm{combustion} \mathrm{one} \mathrm{cylinder}}= 5.955kJ \mathrm{at} \mathrm{each} \mathrm{combustion.a} \mathrm{cylinder}, m_{\mathrm{fuel} \mathrm{combustion}}= \frac{Q_{\mathrm{combustion} \mathrm{one} \mathrm{cylinder}}\mathrm{We} \mathrm{obtain},}{q_{\mathrm{fuel}}} \mathrm{for}= 0.149 g$;
$4)\dot{m}_{\mathrm{fuel}}= 14.3 kg/h = 31.5 lb/h$.

:::
```
