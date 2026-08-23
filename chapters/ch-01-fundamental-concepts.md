---
title: "1. Fundamental Concepts"
short_title: "Chapter 1"
label: ch-01-fundamental-concepts
---

# 1. Fundamental Concepts

(ch-1)=

:::{figure} ../images/art-p009-1.svg
:alt: Illustration from the original text
:::

:::{admonition} Executive summary
:class: tip
The first law states that energy is constant and indestructible: we transform it from one form to another. Work is a transfer involving a force and a displacement. Heat is a chaotic transfer associated with a potential, temperature.
:::

## Introduction

We are presenting here the essential concepts that we will use in the following chapters, attempting to answer two questions:

• What does energy represent?

• Which forms of energy are manipulated in a machine?

(sec-1-1)=
## 1.1 Concept of Energy

(sec-1-1-1)=
### 1.1.1 Energy

We immediately tackle one of the most difficult concepts in all of physics: *energy*.

We observe that in all phenomena, during all the transformations that we can observe in the universe, there exists a quantity that does not vary. This quantity is a measure for an abstract property (energy comes from the Greek ἐνέργεια or *energeia*, meaning “activity”, “operation”) that can take on multiple forms.

We have learned to quantify the amount of energy present in any arbitrary volume, and we strive to control its transformation from one form to another. For example, the electrical energy stored in a battery can be transformed into work in an electric motor, which can be used to operate an elevator, which can lift a load. During all these processes, the total amount of energy remains the same (figure 1.1), a fact that allows us, for example, to quantify the minimum size of battery required to lift a given load.

:::{figure} ../images/fig-1-1.jpg
:label: fig-1-1
:enumerator: 1.1
:alt: The chemical energy stored in the fuel that has been burned is exactly equal to the energy rejected by the exhaust pipe, plus the energy dissipated by friction, plus the kinetic energy of the moving car. All this energy is transformed into heat, *but never destroyed*, once the car is stopped (whichever the means!).

The chemical energy stored in the fuel that has been burned is exactly equal to the energy rejected by the exhaust pipe, plus the energy dissipated by friction, plus the kinetic energy of the moving car. All this energy is transformed into heat, *but never destroyed*, once the car is stopped (whichever the means!).
:::

*Photo* CC-by-sa *by Tommi Nummelin (cropped)*

Thus, energy is primarily a concept that we use to describe the transformations we observe in the world: we could say that it is “what does not change when things change.” For the engineer, it represents above all the ability of one body to set another in motion, in a unified way (for example, with a displacement) or in a disordered way (for example, with chaotic excitation).

We measure energy in joules (J).

(sec-1-1-2)=
### 1.1.2 The first law

The *first law of thermodynamics* simply states:

Energy is indestructible.

:::{aside}
« It is important to realize that in physics today, we have no knowledge of what energy *is*. We do not have a picture that energy comes in little blobs of a definite amount. It is not that way. However, there are formulas for calculating some numerical quantity, and when we add it all together it gives “28”—always the same number. It is an abstract thing in that it does not tell us the mechanism or the *reasons* for the various formulas. »

Richard Feynman, 1963 [[30](#ref-30), [35](#ref-35)]

*The Feynman Lectures on Physics*
:::

One can also state that “the energy of the universe is constant”, or “energy is always conserved”: it can neither be created nor destroyed. In other words, when an object receives a joule of energy, it can either store it or deliver it back to the surroundings; but in no case can it destroy it.

There are only two important laws in thermodynamics; the second one (to which we devote chapters 7 and 8) also deals with the nature of energy. Their implications are enormous and they are the result of deep and laborious intellectual work, spanning several centuries. There is no proof or demonstration of their truth, but all our observations and experiments corroborate them, so they are now universally accepted.

We will express the first law quantitatively in two different ways, one for a closed system (in chapter 2, equation 2/2) and the other for an open system (in chapter 3, equation 3/15).

(sec-1-1-3)=
### 1.1.3 Forms of energy

The different forms of energy that we usually identify have been revealed one by one throughout the history of physics.

*Kinetic energy* is possessed by a body due to its velocity (see §1.2 below). It is the easiest form of energy to identify. It has long been called *vis viva* (“living force”).

*Potential energy* is stored due to the interaction between two objects linked by a conservative force.[^ch1-fn1] On a macroscopic scale, its most palpable form is the potential energy of altitude, resulting from the work done on a mass against its weight (it is this work that makes climbing stairs more tiring than going down, for example). By compressing a spring, potential energy of compression is stored, which can be recovered by letting it expand again.

*Chemical energy* is a combination of potential energy and kinetic energy *between atoms*. Human metabolism, as well as the combustion of hydrocarbons with atmospheric oxygen used in almost all our vehicles, are both based on chemical energy transfers.

In the 20th century, it was discovered that mass, at the sub-atomic level, was also a form of energy (hence the famous $E = mc^{2}$ relates mass and energy). Radiant (electromagnetic) energy is also identifiable at the sub-atomic level. These forms of energy are not relevant in this book.

In thermodynamics, we will focus on three forms of energy, identifiable at the macroscopic scale:

[^ch1-fn1]: A force is called *conservative* when it remains the same in one direction as in the other. For example, gravity is conservative (it is the same whether going up or down) but friction is not (it always opposes the motion).

**Internal energy** denoted $U$, a concept that we use to group together all of the kinetic and potential energy of all of the molecules of a body. It represents the total amount of mechanical energy stored at the microscopic level within an object;

**Heat** denoted $Q$, which is a transfer of the kinetic energy of molecules in a chaotic manner from one body to another;

**Work** denoted $W$, which is a transfer of energy in a coherent manner from one body to another.

In general, the thermodynamic engineer wishes to capture heat from bodies that s/he wants to cool, or supply work to bodies that s/he wants to move. We will therefore study these transfers in detail.

(sec-1-1-4)=
### 1.1.4 Power

*Power* represents a flow of energy in time. Its SI unit is the joule per second, which we name the watt (W):

:::{math}
1 W \equiv 1 J s^{-1} (1/1)
:::

Other units are often used, such as the horsepower. One horsepower is approximately the power that a strong horse can deliver as work in full effort (the story in §5.5 p. 141 reveals the name of the creator of this unit). Note that several definitions for horsepower exist (see Appendix A5 p. 317); here we refer to the din 66036 standard used in the automotive industry:

:::{math}
1 hp = 735.5 W (1/2)
:::

We will denote power by placing a dot above the symbol for energy; thus we write$\dot{E}$ as a power (for example, mechanical) delivering an amount of energy $E$ every second.

In everyday language, the term “power” is used to quantify *the maximum useful power* of a system. For example, when we say that a car has “100 horsepower”, it means has an engine capable of providing it with a power of$\dot{W}_{\mathrm{mech}.}= 100 hp$ for a few moments—but for this, the engine receives about$\dot{Q}_{\mathrm{combustion}}= 300 hp$ in the form of heat. Furthermore, on the road, the average mechanical power supplied by the engine probably does not exceed $20 hp$.

:::{figure} ../images/fig-1-2.svg
:label: fig-1-2
:enumerator: 1.2
:alt: A trailer, with zero power $(\dot{Q} = 0 W)$ but capable of delivering a lot of energy. The combustion of $20 t$ of kerosene releases about $Q = 800 GJ$ as heat; A *Trent 900* turbofan engine, with very high power (able to supply$\dot{W} = 14 MW$ to a commercial aircraft) but devoid of energy $(0 J)$.

A trailer, with zero power $(\dot{Q} = 0 W)$ but capable of delivering a lot of energy. The combustion of $20 t$ of kerosene releases about $Q = 800 GJ$ as heat; A *Trent 900* turbofan engine, with very high power (able to supply$\dot{W} = 14 MW$ to a commercial aircraft) but devoid of energy $(0 J)$.
:::

*Turbofan engine photo derived from a photo* CC-0 *by Commons User:Dr Brains Trailer photo derived from a photo* CC-by *by Thomas R Machnitzki*

(sec-1-1-5)=
### 1.1.5 Specific energy and specific power

In many thermodynamic applications, it is interesting to quantify energy transfers independently of the amount of mass inside the machine. For example, if we want to compare the *operation* of the engines of a motorcycle and of a truck, it will be wise to divide each of the energy transfers (during compression, combustion, expansion) by the quantity of air in the cylinders, to eliminate the scale effects. To this end, we use quantities called *specific* (sometimes called *mass-specific*); and we denote them in lowercase.

**Specific energy** (sometimes called mass-specific energy), is measured in joules per kilogram ($J kg^{-1}$):

:::{math}
:label: eq-1-3
:enumerator: 1/3
e \equiv \frac{E}{m}
:::

where $e$ is the specific energy $(J kg^{-1})$, $E$ is the energy $(J)$,

and $m$ is the mass of the system under consideration $(kg)$.

````{prf:example}
:label: ex-1-1
:enumerator: 1.1

A fuel injector in a car engine must supply a specific heat $q_{\mathrm{comb}.}= 300 kJ kg^{-1}$ regardless of the quantity of air in the cylinder. What will be the energy supplied when $m_{\mathrm{air}}= 0.5 kg$ and when $m_{\mathrm{air}}= 1 kg$?

The heat required will be $Q_{\mathrm{comb}.1}= m_{1}q_{\mathrm{comb}.}= 0.5 \times 300 \times 10^{3}= 150 \times 10^{3}J = 150 kJ$ in the first case, and $Q_{\mathrm{comb}.2}= m_{2}q_{\mathrm{comb}.}= 300 kJ$ in the second case.

````

**Specific power** (sometimes also called mass-specific power), has the same units as specific energy: we divide watts (joules per second) by a mass flow rate (kilos per second).

:::{math}
:label: eq-1-4
:enumerator: 1/4
e \equiv \frac{\dot{E}}{\dot{m}}
:::

where $e$ is the specific power $(J kg^{-1})$, $\dot{E}$ is the power $(W)$, and $\dot{m}$ is the mass flow rate through the system $(kg s^{-1})$.

````{prf:example}
:label: ex-1-2
:enumerator: 1.2

A combustion chamber in a jet engine must supply a specific power $q_{\mathrm{comb}.}= 300 kJ kg^{-1}$ regardless of the air flow rate through the engine. What will be the power supplied when $m_{\mathrm{air}}= 0.5 kg s^{-1}$ and when$\dot{m}_{\mathrm{air}}= 1 kg s^{-1}$?

A power$\dot{Q}_{\mathrm{comb}.1}=\dot{m}_{1}q_{\mathrm{comb}.}= 0.5 \times 300 \times 10^{3}= 150 \times 10^{3}W = 150 kW$ will be required in the first case, and$\dot{Q}_{\mathrm{comb}.2}=\dot{m}_{2}q_{\mathrm{comb}.}= 300 kW$ in the second case.

````

````{prf:example}

Power$\dot{Q}$ and mass flow$\dot{m}$ are written with a dot (flow in time) but not the specific power as heat $q$, which is measured in $J kg^{-1}$ just like specific heat.

Thanks to the concepts of specific energy and specific power, we can compare the same physical process (air heated up by combustion) in this example with the previous one, in two very different machines.

````

It should be noted that in practice, the adjectives “specific” or “mass-specific” are often simply omitted, and that the lowercase notation is not systematically used in scientific literature.

(sec-1-2)=
## 1.2 Mechanical Energy

The student will have no difficulty quantifying *kinetic energy*:

:::{math}
:label: eq-1-5
:enumerator: 1/5
E_{k}= \frac{1}{2} m C^{2}
:::

where $E_{k}$ is the kinetic energy $(J)$, $m$ is the mass of the body $(kg)$, and $C$ is the velocity $(m s^{-1}$, see Appendix A6 p. 319 for other units).

Of course, we also define *specific kinetic energy* correspondingly:

:::{math}
:label: eq-1-6
:enumerator: 1/6
e_{k}\equiv \frac{E_{k}}{m} = \frac{1}{2} C^{2}
:::

In thermodynamics, we are mainly interested in the changes in the energy of fluids within machines. The kinetic energy of gases varies negligibly in piston/cylinder engines, but it plays a major role in jet engines, as we will see in chapter 10 (*air-based power cycles*).

The expression for *potential energy due to altitude* should also not cause any concern for the student:

:::{math}
:label: eq-1-7
:enumerator: 1/7
E_{p}= m g z
:::

:::{math}
:label: eq-1-8
:enumerator: 1/8
e_{p}\equiv \frac{E_{p}}{m} = g z
:::

where $g$ is the gravitational acceleration (usually $9.81 m s^{-2})$, and $z$ is the altitude relative to the reference point $(m$, see Appendix A5 p. 317 for other units).

We will show that in machines, the change of the potential energy of the air due to altitude is always negligible, and that this is often also true for water. Kinetic energy and potential energy due to altitude are often combined into a single term, called *mechanical energy*:

:::{math}
:label: eq-1-9
:enumerator: 1/9
e_{m}\equiv e_{k}+ e_{p}= \frac{1}{2} C^{2}+ g z
:::

````{prf:example}
:label: ex-1-3
:enumerator: 1.3

A student is coasting down a mountain road with a bicycle. At a point with an altitude of $540 m (1772 ft)$, his/her speed is $10 km/h (6.214 mph)$. A few moments later, passing a point at an altitude of $490 m (1608 ft)$, his/her speed is $45 km/h (27.96 mph)$. The mass of the cyclist together with his/her equipment is $70 kg (154.3 lb)$. How much energy has s/he dissipated in the form of friction?

The student’s mechanical energy changed by

$$
\begin{aligned}
\Delta E_{m}= E_{m2}- E_{m1}= m(e_{m2}- e_{m1}) &= m\bigl[g(z_{2}- z_{1}) + \tfrac{1}{2}(C_{2}^{2}- C_{1}^{2})\bigr] \\
&= 70 \Bigl[9.81(490 - 540) + \tfrac{1}{2}\bigl(\bigl(\tfrac{45\times 10^{3}}{3600}\bigr)^{2} - \bigl(\tfrac{10\times 10^{3}}{3600}\bigr)^{2}\bigr)\Bigr] \\
&= 70 [-490.5 + 74.3] = -2.91 \times 10^{4}J = -29.1 kJ.
\end{aligned}
$$

The student has lost $29.1 kJ$ of mechanical energy. This quantity was transferred to the atmosphere in the form of turbulence and heat, and to the bicycle’s bearings and tires in the form of heat.

Energy changes may well be negative. Kinetic energy is however always positive.

Refer to Appendix A5 p. 317 for converting to and from SI units.

The passage of the bicycle through the air causes observable disturbances on a macroscopic scale that we call *turbulence*. After a short time, this kinetic energy has dissipated down to a microscopic scale, warming up the atmosphere.

````

(sec-1-3)=
## 1.3 Work

*Work* is a transfer of energy. An object does work (and thus loses energy) when it exerts a force over a displacement. In mechanics, this work is quantified using vectors:

:::{math}
:label: eq-1-10
:enumerator: 1/10
W \equiv \vec{F} \cdot \vec{l}
:::

where $W$ is the work $(J)$, $\vec{F}$ is the vector representing the force (of magnitude $F$ in $N)$, and $\vec{l}$ is the vector representing the displacement (of magnitude $l$ in $m)$.

In thermodynamics, we will use this equation 1/10 to quantify the work done by fluids. In order to do this, we will rewrite it by adding three particularities:

• We will measure the displacement *as the change in length of the object that does the work*;

• We will only consider cases where the vectors $\vec{F}$ and $\vec{l}$ are collinear;

• We will take into account the fact that $\vec{F}$ can vary as a function of $\vec{l}$.

With these three constraints, equation 1/10 becomes:

:::{math}
W_{\mathrm{A}\rightarrow \mathrm{B}}= \int_{\mathrm{A}}^{\mathrm{B}} \vec{F} \cdot \mathrm{d}\vec{l}
:::

Since $\mathrm{d}\vec{l}$ is measured from the length of the object performing the work, $dl$ will be negative when $W$ is positive (work is then done *to* the object, causing its length to decrease). Finally, since $\vec{F}$ is always collinear with $\mathrm{d}\vec{l}$ in our case, we can write:

:::{math}
:label: eq-1-11
:enumerator: 1/11
W_{\mathrm{A}\rightarrow \mathrm{B}}= -\int_{\mathrm{A}}^{\mathrm{B}} F\, dl
:::

where $W_{\mathrm{A}\rightarrow \mathrm{B}}$ is the work done between two points A and B $(J)$, $F$ is the force $(N)$, and $dl$ is the infinitesimal change in the length of the considered object $(m)$.

On a diagram representing the force as a function of distance, this work $W_{\mathrm{A}\rightarrow \mathrm{B}}$ is represented by the area under the curve from A to B (figure 1.3). The shape of the curve, in other words, the relationship $F_{(l)}$ between $F$ and $l$ during the process, will determine the quantity $W_{\mathrm{A}\rightarrow \mathrm{B}}$.

:::{figure} ../images/fig-1-3.jpg
:label: fig-1-3
:enumerator: 1.3
:alt: On a force-distance diagram, the work done by an object can be visualized by the area under the curve. In the case shown here, the object’s length $l$ increases, and the work will be negative (done by the object).

On a force-distance diagram, the work done by an object can be visualized by the area under the curve. In the case shown here, the object’s length $l$ increases, and the work will be negative (done by the object).
:::

*Diagram* CC-0 *Olivier Cleynen*

````{prf:example}
:label: ex-1-4
:enumerator: 1.4

A spring is compressed from a length of $30 cm (11.81 in)$ down to a length of $5 cm (1.968 in)$. The spring is such that it exerts a force (in newtons) independent of its length and equal to:

:::{math}
F_{(l)}= 6 \times 10^{3}\,\mathrm{N}
:::

What is the energy supplied to the spring in the form of work during compression?

The work done is obtained using equation 1/11, making sure to set the boundaries in SI units:

:::{math}
\begin{aligned}
W_{\mathrm{A}\rightarrow \mathrm{B}}= -\int_{\mathrm{A}}^{\mathrm{B}} F_{(l)}\, dl
&= -\int_{0.30}^{0.05} 6 \times 10^{3}\, dl
= -6\times 10^{3}[l]_{0.30}^{0.05}
= -6\times 10^{3}(0.05-0.30)
= +1.5\times 10^{3}\,J = +1.5\,kJ.
\end{aligned}
:::

The sign of the transferred work is positive: the spring has *received* energy. This does not surprise us: its length has decreased as it was compressed.

Springs with such a characteristic (independent of their length) are often ribbon springs, like those used in mechanical watches.
````

````{prf:example}
:label: ex-1-5
:enumerator: 1.5

Another spring is also compressed from a length of $30 cm$ down to a length of $5 cm$. It is such that it exerts a force (in $N$) related to its length $l$ (in $m$) by the relation:

:::{math}
F_{(l)}= 9 \times 10^{3}- 14 \times 10^{3}l
:::

What is the energy supplied to the spring in the form of work during compression?

The work done is still obtained using equation 1/11, and the integral is only slightly more complex:

:::{math}
\begin{aligned}
W_{\mathrm{A}\rightarrow \mathrm{B}}= -\int_{0.30}^{0.05} (9 \times 10^{3}- 14 \times 10^{3}l)\, dl
&= -\bigl[9 \times 10^{3}l - 7 \times 10^{3}l^{2}\bigr]_{0.30}^{0.05} \\
&= -10^{3}\bigl[9l - 7l^{2}\bigr]_{0.30}^{0.05}
= -10^{3}(0.4325 - 2.07)
= +1.6375 \times 10^{3}\,J = +1.638\,kJ.
\end{aligned}
:::

Springs with such a characteristic (force proportional to length) have regular coils.
````

````{prf:example}
:label: ex-1-6
:enumerator: 1.6

One final spring is compressed from a length of $30 cm$ down to a length of $5 cm$. It is such that it exerts a force (in $N$) related to its length $l$ (in $m$) by the relation:

:::{math}
F_{(l)}= 14 \times 10^{3}- 12 \times 10^{3}l^{0.3}
:::

What is the energy supplied to the spring in the form of work during compression?

The work done is still obtained using equation 1/11:

:::{math}
\begin{aligned}
W_{\mathrm{A}\rightarrow \mathrm{B}}= -\int_{0.30}^{0.05} (14\times 10^{3}-12 \times 10^{3}l^{0.3})\, dl
&= -10^{3}\Bigl[14 l - \frac{12}{1.3} l^{1.3}\Bigr]_{0.30}^{0.05} \\
&= -10^{3}(0.5121 - 2.2703)
= +1.7582 \times 10^{3}\,J = +1.758\,kJ.
\end{aligned}
:::

Springs with such a characteristic are called progressive springs: very soft at first, but increasing rapidly in hardness. They are often used in automobile suspensions. We will see in chapter 2 (*closed systems*) that gases have a similar characteristic.
````

(sec-1-4)=
## 1.4 Heat

(sec-1-4-1)=
### 1.4.1 Temperature

For now, we define *temperature* as a body’s potential for supplying or receiving heat.

The temperature of a body is a quantity that indicates its level of internal excitation. The higher the kinetic energy of its molecules, with different speeds and directions, the higher its temperature will be.

When the molecules making up a body are perfectly stationary relative to each other, the body has no internal vibration: this state defines zero temperature. In contrast, the temperature scale is open towards infinity. There is no defined maximum temperature point.

We cannot simply measure the “mean kinetic energy of the molecules” of a body, and as a result, it is very difficult to rigorously define a temperature scale (for example, what it means for a temperature to be “twice as large”). We will revisit the concept of temperature itself in chapter 4 (*the ideal gas*) and define it fully in chapter 7 (*the second law*). In the meantime, we will accept the definition given above.

Temperature is measured in kelvins $(K)$, on a scale created for the needs of thermodynamics and rather immodestly referred to as *absolute*.

Students will likely be familiar with at least one of two temperature scales:

• the Celsius scale $(^{\circ}C)$. Simply subtracting $273.15$ units from an absolute temperature (in kelvins) gives a temperature in degrees Celsius:

:::{math}
T(^{\circ}C) \equiv T(K) - 273.15 (1/12)
:::

:::{math}
T(K) = T(^{\circ}C) + 273.15 (1/13)
:::

• the Fahrenheit scale $(^{\circ} F)$. The translation to kelvins is a little more complex:

:::{math}
T(^{\circ} F) = 1.8 \times [T(K) - 273.15] + 32 (1/14)
:::

:::{math}
T(K) = \frac{T(^{\circ} F) - 32}{1.8} + 273.15 (1/15)
:::

Both of those scales precede the Kelvin scale, and they were cleverly redefined and synchronized with it in 1848 (wee will have the opportunity to study this clever manipulation in chapter 7, see §7.4 p. 191). Purists will note that the absolute unit is named kelvin and not “degree Kelvin”. Some indicative temperatures are listed in table 1.1.

:::{table} Examples of temperatures. Values with an asterisk are converted approximately.
:label: tab-1-1
:enumerator: 1.1

| kelvins | degrees Celsius | |
| --- | --- | --- |
| $0$ | $-273.15$ | Absolute zero (by definition) |
| $10^{-10}$ | $-273.1499999999$ | Lowest temperature ever reached (only a few particles) |
| $4.22$ | $-268.93$ | Helium boiling at atmospheric pressure |
| $44$ | $-229$ | Average temperature of the surface of Pluto* |
| $184$ | $-89.4$ | Lowest recorded atmospheric temperature on Earth* |
| $273.15$ | $0$ | Water melting at atmospheric pressure |
| $327$ | $54$ | Highest recorded atmospheric temperature on Earth* |
| $373.15$ | $100$ | Water boiling at atmospheric pressure |
| $400$ | $127$ | Nose of a Concorde in cruise flight* |
| $483$ | $200$ | Ordinary household oven* |
| $485$ | $210$ | Autoignition of diesel fuel* |
| $753$ | $480$ | Leading edges of a Lockheed SR-71 Blackbird in cruise* |
| $1100$ | $830$ | Wood fire* |
| $1900$ | $1600$ | Space Shuttle heat shield on atmospheric re-entry* |
| $2500$ | | Incandescent lamp filament |
| $5000$ | | Melting point of diamond (at $12\,\mathrm{GPa}$) |
| $5800$ | | Surface of the Sun |
| $16 \times 10^{6}$ | | Center of the Sun |
| $3 \times 10^{9}$ | | Within a nuclear weapon detonation |
| $3 \times 10^{9}$ | | Core of a massive star on its last day |
| $1 \times 10^{12}$ | | Particles colliding within the RHIC |
| $1.417 \times 10^{32}$ | | The Universe $5.391 \times 10^{-44}\,\mathrm{s}$ after the Big Bang |
:::

(sec-1-4-2)=
### 1.4.2 Heat

:::{aside}
« These results are inexplicable if heat be a substance. »

James Joule, 1845

*On the Changes of Temperature Produced by the Rarefaction and Condensation of Air* [[8](#ref-8)]

:::{aside}
« These circumstances ... pressingly demand a comparison between heat and work, to be undertaken with reference to the divergent assumption that the production of work is not only due to an alteration in the *distribution* of heat, but to an actual *consumption* thereof; and inversely, that by the consumption of work heat may be *produced*. »

Rudolf Clausius, 1850 [[10](#ref-10), [11](#ref-11), [21](#ref-21)]
:::
:::

When two bodies of different temperatures are brought into contact, their temperatures tend to equalize during a spontaneous transfer of energy. We

Heat, written $Q$, is **a form of energy** (measured in joules). On a macroscopic scale, it is a transfer of energy in chaotic form. It can be caused in several ways, the most relevant for the engineer being:

• loss of internal energy of a body, by coming into contact with a lower • disappearance of mass in a nuclear reaction;

• transformation of potential energy between atoms, by chemical reaction

(especially the combustion of hydrocarbons with atmospheric oxygen).

Just like we denote heat as $Q (J)$, we denote *specific heat* as $q (J kg^{-1})$.

The concept of heat is very difficult to understand. It was long believed to be a fluid (the *caloric*) of very low density, capable of permeating all materials.

This theory was abandoned in the mid-19th century, when it was shown that *heat is not conserved*, that is, it has the ability to disappear or appear.

For example, an engine in operation receives heat (through combustion) but releases less than it received. It transforms part of it into work, which we

On a microscopic scale, in other words, when we consider the movement of individual particles, the concepts of temperature and heat are even more diffi-

*Engineering Thermodynamics* by Olivier Cleynen cult to define (Richard Feynman [[30](#ref-30), [35](#ref-35)] explores this beautifully). However, this is beyond the scope of this book.

(sec-1-4-3)=
### 1.4.3 Thermal capacity

When the same amount of heat is supplied to two different bodies, their temperature can increase in different ways – for example, it takes less heat to raise the temperature of a kilogram of steel than a kilogram of aluminum. This tendency of a body’s temperature to increase is called its *thermal capacity* (or *heat capacity*).

The specific thermal capacity of a body is defined as the amount of heat required to raise the temperature of one kilogram of the substance by one kelvin:

:::{math}
c \equiv \frac{\mathrm{δ}q}{dT} = \frac{1}{m} \frac{\mathrm{δ}Q}{dT} (1/16)
:::

where $c$ is the *specific thermal capacity* of the substance $(J kg^{-1}K^{-1})$, δ$q$ is a (specific) infinitesimal quantity of heat $(J kg^{-1})$, δ$Q$ is an infinitesimal quantity of heat $(J)$, $m$ is the mass $(kg)$,

and $dT$ is an infinitesimal change in temperature $(K$ or $^{\circ}C)$.

In this equation 1/16, the infinitesimal transfer of heat is denoted by the symbol δ, while the infinitesimal change in temperature is denoted by the symbol $d$. This distinction is harmless and is detailed in Appendix A4 p. 316.

The specific thermal capacity of solids is generally invariant. However, for fluids, which we use extensively in machines, it is not so simple:

• By working a gas (namely, by allowing it to push on a movable wall), we significantly increase its specific thermal capacity. We will quantify this phenomenon in chapter 4 (*the ideal gas*).

• The specific thermal capacity of liquids and vapors becomes infinite (!) during boiling, which takes place over a particular range of properties. Outside of this range, the capacity becomes finite again, but it varies with temperature. We will describe these behaviors in chapter 5 (*liquids and vapors*).

````{prf:example}
:label: ex-1-7
:enumerator: 1.7

The specific thermal capacity of solid steel is constant (independent of temperature) and has a value of $c_{\mathrm{steel}}= 475 J kg^{-1}K^{-1}$. How much heat is required to change the temperature of a $50 kg (110.2 lb)$ block of steel from a temperature of $T_{\mathrm{A}}= 5^{\circ}C$ to a temperature of $T_{\mathrm{B}}= 18^{\circ}C$?

We use the definition 1/16 to write, in the general case:

:::{math}
c_{\mathrm{steel}}= \frac{1}{m_{\mathrm{steel}}} \frac{\mathrm{δ}Q}{dT}
:::

:::{math}
δ Q = c_{\mathrm{steel}}m_{\mathrm{steel}}dT
:::

B

:::{math}
Q_{\mathrm{A}\rightarrow \mathrm{B}}= \int m_{\mathrm{steel}}c_{\mathrm{steel}}dT
:::

A

Since the capacity $c_{\mathrm{steel}}$ is independent of $T$, this integral becomes simply: $Q_{\mathrm{A}\rightarrow \mathrm{B}}= m_{\mathrm{steel}}c_{\mathrm{steel}}\int ^{\mathrm{B}}_{\mathrm{A}}dT = m_{\mathrm{steel}}c_{\mathrm{steel}}(T_{\mathrm{B}}-T_{\mathrm{A}}) = 50 \times 475 \times (18 - 5) = +3.0875 \times 10^{5}J = +308.8 kJ$.

During integration, $\int ^{\mathrm{B}}_{\mathrm{A}}dT$ becomes $\Delta T$ (a temperature difference), while $\int ^{\mathrm{B}}_{\mathrm{A}}$ δ$Q$ becomes simply $Q_{\mathrm{A}\rightarrow \mathrm{B}}$ (a transfer between two states). Heat, a *path quantity*, is transferred, while temperature, a *state quantity*, is increased (see Appendix A4 on this topic).

In this book, when we quantify energy transfers, we convene to make their sign explicit (so we add a “+” in positive transfers).

A conversion of the temperatures to kelvins would not have changed the value of $\Delta T$. The result would then have been the same.

With an electrical resistance of the power of a standard domestic heater $(2 kW)$, it would take $\Delta t = \frac{Q_{\mathrm{A}\rightarrow \mathrm{B}}}{Q} = \frac{308.8\times 10^{3}}{2\times 10^{3}} = 154 s$ to warm up the steel, just over two minutes. We will see in chapter 4 (*the ideal gas*) that air at constant pressure has a specific thermal capacity three times greater than that of steel.

````

(sec-1-5)=
## 1.5 Hot and Cold

We conclude this chapter by revisiting some common language terms, as they are understood in thermodynamics. *Hot* — For us, “hot” is not a property of objects: instead of “this object is hot”, we say that its temperature is high. Instead of “this object is heating up/cooling down” we say that its temperature is increasing or decreasing. In everyday language, phrases like “it is hot” or “heat wave” also refer to temperature. *To heat* — For us, “to heat up” means to supply heat. We can “heat up” an object while its temperature drops. We can also raise the temperature of an object without supplying heat (figure 1.4). *Cold* — For us, the sensation of “cold” denotes a low temperature. We do not consider “cold” to be something that can be manufactured or measured. Instead, we would say that we are transfering heat away from an object (for example, a refrigerator extracts heat from a warm food item). *Fire* — Fire is the term given to the emission of light (electromagnetic radiation) from a gas at high temperatures. In thermodynamics, “fire” does not have any special properties. For us, it is the same heat whether it is generated by the combustion of wood or kerosene, by friction in a brake, or by a nuclear reaction. Ultimately, the only thing that matters is the temperature at which it is transmitted!

:::{figure} ../images/fig-1-4.svg
:label: fig-1-4
:enumerator: 1.4
:alt: Left: when air is compressed in a compressor, air gives heat away through the sides and the fins of the cylinders; and yet, its temperature increases. Right: by contrast, when liquid oxygen is expanded in a vane, liquid oxygen receives heat from the atmosphere (as evidenced by the condensation and frost from atmospheric air on the piping); in spite of this, its temperature drops.

Left: when air is compressed in a compressor, air gives heat away through the sides and the fins of the cylinders; and yet, its temperature increases. Right: by contrast, when liquid oxygen is expanded in a vane, liquid oxygen receives heat from the atmosphere (as evidenced by the condensation and frost from atmospheric air on the piping); in spite of this, its temperature drops.
:::

*Compressor photo* CC-by-sa *Fábio Teixeira*

*Liquid oxygen photo public domain Jensen Stidham / USAF*

:::{aside}
« The principle to be followed in constructing a thermometric scale might at first sight seem to be obvious, as it might appear that a perfect thermometer would indicate equal additions of heat, as corresponding to equal elevations of temperature, estimated by the numbered divisions of its scale. It is however now recognized (from the variations in the specific heats of bodies) as an experimentally demonstrated fact that thermometry under this condition is impossible, and we are left without any principle on which to found an absolute thermometric scale. »

William Thomson (not yet crowned *Baron Kelvin*…) 1848 [[9](#ref-9)]

*Thermometer* — We leave it to the student to explore how thermometers work: how can we *know* in absolute terms that a temperature is high or low?
:::

We simply note that we humans are ourselves very poor thermometers: since the human body attempts to maintain a constant temperature, our sensations of “hot” or “cold” are intrinsically linked to heat transfer.

Even though this vocabulary probably puts us among the unsociable scientists relegated to the end of the table, it equips us better to face what’s next, because in the next chapter, we will be dealing with *closed systems*.

::::{admonition} A Bit of History
:class: note
:label: hist-1-4

**Measuring the Degree of Heat**

*By Philippe Depondt*

*Pierre and Marie Curie University, Paris*

For Aristotle, in the 4th century BCE in Greece, fire was one of the four elements of matter along with water, air, and earth. The idea of measuring something, be it fire or anything else, that is, assigning a numerical value to a quantity, was completely foreign to him because his physics was essentially nonmathematical [[31](#ref-31)]: his theories were based on *qualitative* observations. The synthesis of Aristotle’s ideas with Christianity was made in the 12th century by Thomas Aquinas, and these ideas were widely dominant in the scholarly world in Europe until the early 17th century (for example, Galileo had to argue largely *against* these ideas).

Until the 17th century, descriptions of the world would unfortunately remain largely qualitative. The exception provided by astronomers is telling: in establishing his heliocentric model in the early 16th century, Copernicus could rely on measurements dating back to antiquity, and then on those of Arab astronomers from the Middle Ages. Similarly, it was the remarkably rigorous and precise measurements (less than one minute of angle) carried out in Tycho Brahe’s modern “laboratory” that led to Johannes Kepler’s discovery of his three laws, which formed one of the foundations of Newton’s dynamics.

In the case of thermodynamics, the English philosopher Francis Bacon, laying the foundations of inductive reasoning at the beginning of the 17th century, used heat as an example to illustrate his point. In order to study its nature, he proposed in the *Novum Organum* to compile all observations of phenomena in which heat appears, of phenomena where it does not appear, and finally of those where it appears “by degrees.” This method remained qualitative, but at approximately the same time, there was an explosion of attempts to make truly quantitative measurements of this “degree of heat.”

It seems that the first thermometer was invented around 1605 by a Dutchman named Cornelis Drebbel [[39](#ref-39)]: based on ideas dating back to Hero of Alexandria (1st century CE), it consisted of a hollow glass sphere extended by a tube pointing downwards and immersed in a colored liquid. If the sphere was heated, the liquid was pushed downwards by the expansion of the air, and conversely, if it was cooled, the liquid rose in the tube. It was thus an air thermometer (figure 1.5). This thermometer was later used to monitor fever in patients (figure 1.6), but it had the drawback of being as sensitive to changes in atmospheric pressure as to temperature.

:::{figure} ../images/fig-1-5.jpg
:label: fig-1-5
:enumerator: 1.5
:alt: An air thermometer from the early 17th century. The ball was filled with air whose volume varies with its temperature, pushing the water from the reservoir below whose surface is at atmospheric pressure. The liquid could be colored, and its changes in height were measured using a scale. Since atmospheric pressure varies with meteorological conditions, it affected the measurements: it was, in a way, a baro-thermometer.

An air thermometer from the early 17th century. The ball was filled with air whose volume varies with its temperature, pushing the water from the reservoir below whose surface is at atmospheric pressure. The liquid could be colored, and its changes in height were measured using a scale. Since atmospheric pressure varies with meteorological conditions, it affected the measurements: it was, in a way, a baro-thermometer.
:::

*Engraving by Robert Fludd (1626, public domain), selected by Lamouline 2005 [[45](#ref-45)]*

:::{figure} ../images/fig-1-6.jpg
:label: fig-1-6
:enumerator: 1.6
:alt: A medical thermometer from the early 17th century. The gas bulb was placed in the patient’s mouth. One can well imagine that the thermometer’s sensitivity to atmospheric pressure was not the biggest obstacle to its adoption...

A medical thermometer from the early 17th century. The gas bulb was placed in the patient’s mouth. One can well imagine that the thermometer’s sensitivity to atmospheric pressure was not the biggest obstacle to its adoption...
:::

*Drawing by Santori & Avicenne (Commentaria in primam Fen primi libr Avicennae, 1625, public domain), selected by Lamouline 2005 [[45](#ref-45)]*

In the middle of the century, liquid thermometers would prove to be much more reliable and easier to use. The glass bulb was now placed at the bottom of the device and filled with colored liquid that rose in a graduated tube; this tube was initially open, but it was found that by closing it, evaporation of the liquid could be prevented (figure 1.7). These improvements had been strongly supported by the Italian grand duke Ferdinando II de’ Medici, and these devices were thus called “Florence thermometers.”

:::{figure} ../images/fig-1-7.jpg
:label: fig-1-7
:enumerator: 1.7
:alt: A Florence thermometer from the mid-17th century. This time, it was the liquid, contained in the lower bulb, that contracted and expanded with temperature. Its changes in volume were such that a long spiral-blown glass tube was needed to measure them.

A Florence thermometer from the mid-17th century. This time, it was the liquid, contained in the lower bulb, that contracted and expanded with temperature. Its changes in volume were such that a long spiral-blown glass tube was needed to measure them.
:::

*Engraving by the Accademia del Cimento (Saggi di naturali esperienze, 1667, public domain), selected by Lamouline 2005 [[45](#ref-45)]*

However, all these thermometers remained difficult to use, significantly limiting their dissemination. René-Antoine Ferchault de Réaumur, around the middle of the 18th century, developed a water-alcohol mixture thermometer in which the alcohol level is precisely fixed to ensure the reproducibility of the instrument. He calibrated it by choosing two references (melting ice and boiling water) and dividing this interval into 80 degrees. This scale is called the “Réaumur scale.”

In 1724, in Danzig, the German Daniel Gabriel Fahrenheit described a thermometer that used the expansion of mercury and introduced a scale in which melting ice is at 32 degrees and the temperature of blood at 96 degrees; a mixture of ice, water, and sal ammoniac gave him the zero of his scale (see also section §7.4.3 p. 191).

In 1741, the Swedish Anders Celsius adopted the Réaumur scale but divided it into 100 intervals instead of 80. This convention was widely spread in France, and in 1794, at the time of the adoption of the metric system by the Convention, the Celsius scale was chosen as the official temperature scale.

The transition from the subjective sensation of hot and cold to the objective measurement of temperature with reliable instruments and a universal scale led to a large number of observations that were not self-evident until then: the temperature of a cellar is not higher in winter than in summer, iron is not “colder” than wood, etc., and all in all, this is quite recent!

The issue of graduations remained. The number of graduations varied widely, with artisans merely attempting to reproduce what they had already created themselves; at best, thermometers built by the same person gave roughly similar results. Due to the lack of a universally accepted scale, it was impossible to make measurements in different locations with different instruments for comparison.

In the early 18th century, the Frenchman Guillaume Amontons built an air thermometer based on the measurement of a pressure difference rather than volume. Having observed that if boiling water continued to be heated, its degree of heat did not increase, he used this as a fixed point of reference. Of course, the measurements needed to be corrected by simultaneously measuring atmospheric pressure. This system allowed Amontons to make a major discovery: if the gas pressure increases as the degree of heat increases, conversely, it decreases as the degree of heat decreases. At a minimum, this pressure must become zero, as well as the degree of heat. This extrapolated minimum corresponds to, in modern units, $-239.5^{\circ}\mathrm{C}$… A first measure of absolute zero!

::::

## Problems

```{exercise}
:label: prob-1-1
:enumerator: 1.1

**Free-Wheeling Bicycle A cyclist starts a free wheel descent. With their equipment and bike, their mass is $75 kg (165.3 lb)$. As they pass a point at an altitude of $1200 m (3937 ft)$, their speed is $50 km/h (31.1 mph)$. Exactly $7 \min$ later, as they pass a point at an altitude of $950 m$, their speed is $62 km/h$. 1. How much energy has the cyclist dissipated in the form of friction between these two points? Further down the descent, still freewheeling, the cyclist sees their speed stabilize at $45 km/h$ on a slope of $4 \%$. 2. What is the power with which the cyclist dissipates energy in the form of friction?**

```

```{exercise}
:label: prob-1-2
:enumerator: 1.2

**Power of a Steam Power Plant The path followed by the water in a steam power plant can be represented in a simplified way as follows (figure 1.8): *Diagram* CC-by-sa *Olivier Cleynen***

:::{admonition} Answer
:class: dropdown

1) In the end, the water has rejected as much energy as it has received, so $q_{\mathrm{D}\rightarrow \mathrm{A}}= -w_{\mathrm{A}\rightarrow \mathrm{B}}- q_{\mathrm{B}\rightarrow \mathrm{C}}- w_{\mathrm{C}\rightarrow \mathrm{D}}= -306 kJ kg^{-1}$ We ran engines for forty years before we understood this!
2) $\dot{Q}_{\mathrm{D}\rightarrow \mathrm{A}}=\dot{m}q_{\mathrm{D}\rightarrow \mathrm{A}}= -4.59 MW$
3) $\dot{W}_{\mathrm{C}\rightarrow \mathrm{D}}=\dot{m}w_{\mathrm{C}\rightarrow \mathrm{D}}= -2.91 MW$
4) $\eta _{\mathrm{plant}}= \left|\frac{w_{\mathrm{turbine}}+w_{\mathrm{pump}}}{q_{\mathrm{boiler}}}\right| = 32 \%$ (realistic value).

:::
```

   :::{figure} ../images/fig-1-8.jpg
   :label: fig-1-8
   :enumerator: 1.8
   :alt: Simplified diagram of the water circuit inside a steam power plant. The water follows a complete cycle through four processes. This circuit
   
   Simplified diagram of the water circuit inside a steam power plant. The water follows a complete cycle through four processes. This circuit, called the Rankine cycle, is studied in more detail in chapter 9 (*steam power cycles*) (section 9.4.2 p. 252).
   :::

**From A to B** the liquid water is compressed in the pump. It receives a specific work $w_{\mathrm{A}\rightarrow \mathrm{B}}= +50 kJ kg^{-1}$, with no heat transfer.

**From B to C** the water is heated in the boiler, where it exits as steam. It receives a specific heat $q_{\mathrm{B}\rightarrow \mathrm{C}}= +450 kJ kg^{-1}$, without receiving any work.

**From C to D** the water expands in the turbine, where it delivers a specific work $w_{\mathrm{C}\rightarrow \mathrm{D}}= -194 kJ kg^{-1}$, without receiving or giving heat.

**From D to A** the water is cooled in a condenser, with no work transfer. It returns to its original state and properties before returning to the pump to be compressed again.

The water flow rate circulating in the plant is $15 kg s^{-1}$.

1. What is the specific power rejected in the form of heat in the condenser?

2. What is the power (in watts) rejected by the condenser?

3. What is the power (in watts) generated by the turbine in the form of work?

4. What is the efficiency $\eta _{\mathrm{plant}}$ of the power plant, that is, the ratio between its net power and the power it receives as heat?

```{exercise}
:label: prob-1-3
:enumerator: 1.3

**Compression of Springs In the laboratory of a company manufacturing automotive suspension systems, an engineer compares the characteristics of three springs of different geometry. To do this, s/he measures the force $F$ (in $N)$ exerted by each spring as a function of its length $l$ (in $m)$, and models these behaviors as follows: • $F_{\mathrm{A} (l)}= 8 \times 10^{3}- 2 \times 10^{3}l$ • $F_{\mathrm{B} (l)}= 8 \times 10^{3}- 3 \times 10^{3}l^{1.6}$ • $F_{\mathrm{C} (l)}= 0.1 \times 10^{3}l^{-3}$ What is the amount of work required to compress each of these springs from a length of $40 cm (15.74 in)$ down to a length of $12 cm (4.724 in)$? exponentially when compressed. We will see in chapter 2 (*closed systems*) that when fluids are compressed and expanded slowly, they behave similarly to spring C, which has a conical geometry like those shown here. *Photo* CC-by-sa *Jean-Jacques Milan***

:::{admonition} Answer
:class: dropdown

1) $W_{\mathrm{A}}= \int _{l_{1}}^{l_{2}}F_{(l)}\,\mathrm{d}l = -10^{3}\left[8l - \frac{1}{2}2l^{2}\right]_{0.4}^{0.12}= +2.094\,\mathrm{kJ}$. 2) $W_{\mathrm{B}}= +2.138\,\mathrm{kJ}$ 3) $W_{\mathrm{C}}= +3.157\,\mathrm{kJ}$.

:::
```

   :::{figure} ../images/fig-1-9.jpg
   :label: fig-1-9
   :enumerator: 1.9
   :alt: Conical springs, whose stiffness increases exponentially when compressed. We will see in chapter 2 (closed systems) that when fluids are com
   
   Conical springs, whose stiffness increases exponentially when compressed. We will see in chapter 2 (*closed systems*) that when fluids are compressed and expanded slowly, they behave similarly to spring C, which has a conical geometry like those shown here.
   :::

```{exercise}
:label: prob-1-4
:enumerator: 1.4

**Spring-Powered Engine We model the operation of a gasoline engine by replacing the air in a cylinder with a spring. We want to quantify the energy received and then rejected by a powerful spring during a back-and-forth motion (similar to the air during the compression and expansion phases of a piston engine cycle). The experiment proceeds cyclically with the following four steps (figure 1.10): **From 1 to 2:** The experimenter compresses a spring from a length of $25 cm$ to a length of $8 cm$. The spring exerts a force related to its length (in meters) by the relation: $F = 25.4 \times 10^{3}- 40 \times 10^{3}l$ where $F$ is the force (in $N)$; and $l$ is the length of the spring (in $m)$. *Diagram* CC-by-sa *Olivier Cleynen* **From 2 to 3:** When the length of the spring reaches $8 cm$, the experimenter blocks the piston’s movement. A solid block is then inserted between the piston wall and the spring. The force on the piston (which has not moved) increases until reaching $32 kN$. **From 3 to 4:** Once the block has been inserted, the experimenter reverses the motion with the piston until the final length reaches again $25 cm$. **From 4 to 1:** The block is removed without moving the piston, and the force on the piston returns to the value it had at the beginning of the experiment. We want to quantify the energy received and then rejected by the {spring + block} assembly during one back and forth motion. 1. Draw the process on a diagram showing the force as a function of the inner length, qualitatively (that is, without showing numerical values). 2. How much energy did the spring receive from the experimenter during the outbound journey (from 1 to 2)? 3. What is the characteristic $F_{(l)}$ of the {spring + block} assembly during the return journey (from 3 to 4)? 4. How much energy did the spring receive from the piston during the return journey (from 3 to 4)? 5. In the end, how much energy did the experimenter receive or spend during the experiment? 6. At what frequency should the experiment be repeated for the power to reach $25 hp$, that is, $18.4 kW$?**

:::{admonition} Answer
:class: dropdown

2) $W_{1\rightarrow 2}= +3.196 kJ$ 3) $F_{(l)3\rightarrow 4}= 35.2 \times 10^{3}- 40 \times 10^{3}l$ 4) $W_{3\rightarrow 4}= -4.862 kJ$ 5) $W_{\mathrm{cycle}}= 1.666 kJ$ 6) $f = 11.04 s^{-1}$ (11 times per second)

:::
```

   :::{figure} ../images/fig-1-10.jpg
   :label: fig-1-10
   :enumerator: 1.10
   :alt: Experiment conducted with a powerful spring. The piston compresses the spring from to , then the spring pushes back the piston from to . On
   
   Experiment conducted with a powerful spring. The piston compresses the spring from $1$ to $2$, then the spring pushes back the piston from $3$ to $4$. On the return path, the force exerted by the spring is greater.
   :::

```{exercise}
:label: prob-1-5
:enumerator: 1.5

**Preparing a Bath** A student exhausted from doing integral calculus with springs wishes to take a bath. Tap water arrives at a temperature of $10^{\circ}C (50 ^{\circ} F)$ in the electric water heater; it has a constant thermal capacity of $c_{\mathrm{liquid\ water}}= 4.2 kJ kg^{-1}K^{-1}$ and a constant density $\rho _{\mathrm{liquid\ water}}= 10^{3}kg m^{-3}$. 1. How much energy is needed to heat the water to $40^{\circ}C (104 ^{\circ} F)$ in order to fill a bathtub of $270 L (10.57 US gal)$? 2. How long will it take the heater to increase the temperature of the water if its heating power is $\dot{Q}= +2 kW$?

:::{admonition} Answer
:class: dropdown

1) $Q_{\mathrm{water}}= \rho _{\mathrm{water}}V_{\mathrm{water}}c_{\mathrm{water}}\Delta T = +34.02 MJ$
2) $\Delta t = \frac{Q_{\mathrm{water}}}{\dot{Q}} = 4.7 h$

:::
```

```{exercise}
:label: prob-1-6
:enumerator: 1.6

**Hydraulic Jack We want to lift a vehicle with a mass of $1200 kg (2645.5 lb)$ using the hydraulic jack schematized in figure 1.11. The surface area of the left piston is $5 cm^{2} (0.775 sq in)$. *Diagram* CC-0 *Olivier Cleynen* The oil within the jack is assumed to be incompressible, meaning its volume is considered constant regardless of pressure. The purpose of the setup is to allow an average-sized person to lift and hold the vehicle in place with the left piston (whose end is equipped with handles). 1. Design the right piston (under the vehicle) so that the force in the left piston does not exceed $100 N (22.48 lbf)$. 2. What is the power required to hold the vehicle in place? We want to lift the vehicle by $25 cm (9.843 in)$, in less than 30 seconds. 3. How far would the left piston need to be pushed for this? 4. What would be the work and power to be supplied in this case?**

:::{admonition} Answer
:class: dropdown

1) $A_{2}\le \frac{F_{2}}{p_{2}} = \frac{F_{2}}{p_{1}} = 5.89 \times 10^{-2}m^{2}= 589 cm^{2} (91.3 sq in) 2)\dot{W} = 0 W$ of course, since there is no movement… 3) By calculating the swept oil volume $V, d_{1}= \frac{V_{1}}{A_{1}} = \frac{V_{2}}{A_{1}} = 29.43 m$, an impracticable length, which can be avoided by adding a pumping mechanism. $4)\dot{W}_{\mathrm{mean}}\le \frac{W_{\mathrm{A}\rightarrow \mathrm{B}}}{\Delta t} = 98.1 W$.
*Engineering Thermodynamics* by Olivier Cleynen

:::
```

   :::{figure} ../images/fig-1-11.jpg
   :label: fig-1-11
   :enumerator: 1.11
   :alt: Schematic diagram of a hydraulic jack.
   
   Schematic diagram of a hydraulic jack.
   :::

```{exercise}
:label: prob-1-7
:enumerator: 1.7

**Water Turbine A constant flow rate of $1200 kg s^{-1}$ of water passes through a small hydraulic power plant represented in figure 1.12. • At point $1$, the water arrives at a speed of $3 m s^{-1}$ with a temperature of $T_{1}= 5^{\circ}C$ and an altitude $z_{1}= 75 m (246.1 ft)$. • At point $2$, it exits at a speed of $2.5 m s^{-1}$ with a temperature $T_{2}= 5.04^{\circ}C$ and an altitude $z_{2}= 4 m (13.12 ft)$. The water pressure is the same at 1 and 2, and the velocity profile of the water at each point is approximately uniform. The water has a specific thermal capacity of $c_{\mathrm{liquid} \mathrm{water}}= 4.2 kJ kg^{-1}K^{-1}$.**

:::{admonition} Answer
:class: dropdown

1) $\Delta e_{m}= -697.9 J kg^{-1}$ (so, a loss by water)
2) $q_{1\rightarrow 2}= +168 J kg^{-1} 3)\dot{W}_{\mathrm{turbine}}=\dot{m}(\Delta e_{m}+ q_{1\rightarrow 2}) = -635.9 kW$.

:::
```

   :::{figure} ../images/fig-1-12.jpg
   :label: fig-1-12
   :enumerator: 1.12
   :alt: Schematic diagram of a water turbine. Water enters at the top left, rotates the turbine blades, is heated by internal friction, and exits at
   
   Schematic diagram of a water turbine. Water enters at the top left, rotates the turbine blades, is heated by internal friction, and exits at the bottom right of the machine.
   :::

1. What is the specific mechanical power received or supplied by the water as it passes through the power plant?

2. What is the specific power provided as heat by internal friction?

3. What is the power (in watts) released in the form of work by the turbine?

```{exercise}
:label: prob-1-8
:enumerator: 1.8

**Central Heating Boiler** The boiler of the central heating system of a building, represented in figure 1.13, operates with the combustion of kerosene. The water enters the boiler at a temperature $T_{\mathrm{C}}= 20^{\circ}C (68 ^{\circ} F)$ and exits at $T_{\mathrm{D}}= 70^{\circ}C (158 ^{\circ} F)$, with a flow rate $\dot{V}_{\mathrm{water}}= 0.25 L s^{-1}(0.054 99 imp gal)$. The combustion chamber admits air at $T_{\mathrm{A}}= 8^{\circ}C (46.4 ^{\circ} F)$ and it exits through the chimney at a temperature $T_{\mathrm{B}}= 120^{\circ}C (248 ^{\circ} F)$; the air flow rate is $\dot{m}_{\mathrm{air}}= 0.5 kg s^{-1}$. Specific heat of combustion of kerosene: $46.4 MJ kg^{-1}$ Specific thermal capacity of liquid water: $4.18 kJ kg^{-1}K^{-1}$ Specific thermal capacity of air at constant pressure: $1.15 kJ kg^{-1}K^{-1}$ 1. What is the hourly consumption of kerosene by the boiler? 2. What is the efficiency of the boiler, that is, the ratio between its useful heat transfer and its energy consumption?**

:::{admonition} Answer
:class: dropdown

1) $\dot{m}_{\mathrm{kerosene}}= \frac{\dot{Q}_{\mathrm{kerosene}}}{q_{\mathrm{kerosene}}} = \frac{-\dot{Q}_{\mathrm{water}}-\dot{Q}_{\mathrm{air}}}{q_{\mathrm{kerosene}}}= 2.51 \times 10^{-3}\,\mathrm{kg\,s^{-1}}= 9.1\,\mathrm{kg\,h^{-1}}$
2) $\eta _{\mathrm{boiler}}= \left|\frac{\dot{Q}_{\mathrm{water}}}{\dot{Q}_{\mathrm{kerosene}}}\right| = 44.8\%$

:::
```

   :::{figure} ../images/fig-1-13.jpg
   :label: fig-1-13
   :enumerator: 1.13
   :alt: Schematic diagram of a boiler used for heating a building. The water (C → D) enters from the right and is heated by the air (A → B) mixed with kerosene.
   
   Schematic diagram of a boiler used for heating a building. The water (C $\rightarrow$ D) enters from the right and is heated by the air (A $\rightarrow$ B) mixed with kerosene.
   :::

```{exercise}
:label: prob-1-9
:enumerator: 1.9

**Helicopter Turboshaft Engine** A helicopter is equipped with two turboshaft engines, namely, gas turbines whose purpose is to rotate a shaft emerging from the engine (figure 1.14). We can evaluate several characteristics of these engines without knowing the details of their internal operation. Each of the two engines admits atmospheric air at a temperature of $15^{\circ}C$. The air is compressed, heated, and then expanded, which allows work to be generated to rotate the rotors. At the engine outlet, the air is discharged at atmospheric pressure and a temperature of $360^{\circ}C (680 ^{\circ} F)$. At constant pressure, the specific thermal capacity of air is approximately $c_{p \mathrm{air}}= 1050 J kg^{-1}K^{-1}$. The combustion of kerosene releases $q_{\mathrm{kerosene}}= 46 MJ kg^{-1}$. 1. What is the specific power rejected by the engines in the form of heat to the atmosphere? *Hint: this is the specific heat that the rejected air must lose to return to its initial temperature.* The flight manual indicates that in the combustion chamber (the part of the engine where the fuel is burned), the air is admitted at a temperature of $250^{\circ}C$ and is heated by the combustion, at constant pressure, up to $776^{\circ}C (1428.8 ^{\circ} F)$. 2. What is the specific power generated by the engines in the form of work? *Hint: in the end, the net energy supplied by the air in the form of work and heat had been supplied to it in the combustion chamber.* In order to maintain the helicopter in stationary flight at full load, the rotors require a total power from the two engines in the form of work of $1.32 MW$ (approximately $1800 hp)$. 3. What is the total air flow rate that needs to be admitted to the two turboshaft engines? 4. What is the total power (in $W)$ to be supplied in the two combustion chambers? 5. What is the hourly consumption of kerosene for the helicopter in stationary flight?**

:::{admonition} Answer
:class: dropdown

1) $q_{\mathrm{rejected}}= +362.25 kJ kg^{-1}$
2) $q_{\mathrm{chamber}}+ w_{\mathrm{shaft}}+ q_{\mathrm{atmospheric} \mathrm{cooling}}= 0$ or
$q_{\mathrm{chamber}}+ w_{\mathrm{shaft}}- q_{\mathrm{rejected}}= 0$; thus we have
$w_{\mathrm{shaft}}= -q_{\mathrm{chamber}}+ q_{\mathrm{rejected}}= -190.1 kJ kg^{-1}$
(these powers do not depend on the mass flow,
and are independent of the number of engines
taken into account).
3) $\dot{m}_{\mathrm{air}}= 6.95 kg s^{-1}$
4) $\dot{Q}_{\mathrm{chambers}}= 3.836 MW$
5) $\dot{m}_{\mathrm{kerosene}}= \frac{\dot{Q}_{\mathrm{chambers}}}{q_{\mathrm{kerosene}}} = 300.2 kg h^{-1}$ (realistic value).

:::
```

   :::{figure} ../images/fig-1-14.svg
   :label: fig-1-14
   :enumerator: 1.14
   :alt: A Sikorsky S-76B helicopter, equipped with two P&WC pt-6b turboshaft engines, each with . The airflow through the engines is shown in a sche
   
   A Sikorsky S-76B helicopter, equipped with two *P&WC* pt-6b turboshaft engines, each with $980 hp$. The airflow through the engines is shown in a schematic diagram. We will study these engines in more detail in chapter 10 (*air-based power cycles*).
   :::
