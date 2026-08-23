---
title: "4. The Ideal Gas"
short_title: "Chapter 4"
label: ch-04-the-ideal-gas
---

:::{figure} ../images/art-p110-1.svg
:alt: Chapter opening illustration
:::

# 4. The Ideal Gas

(ch-4)=

The Ideal Gas

*The Improbable Thermometer of Scholar Clapeyron*

:::{figure} ../images/art-p081-1.svg
:alt: Illustration from the original text
:::

:::{admonition} Executive summary
:class: tip
The ideal gas is a mathematical model that allows us to predict the properties (internal energy, enthalpy) of a gas simply based on its temperature. By approximation, air is an ideal gas.
:::

## Introduction

In chapters 2 and 3 we learned to quantify energy transfers — but we can

only do so when we know the values of $u$ or $h$, which are quantities that

are impossible to measure directly in practice.

This chapter 4 (*the ideal gas*) aims to answer two questions:

• How can we describe the behavior of air when it is heated or compressed?

• How can we predict the values of $u$ and $h$ when using air?

This chapter is incompatible with chapter 5 (*liquids and vapors*), where we

will have to forget everything learned here.

(sec-4-1)=
## 4.1 Definition

(sec-4-1-1)=
### 4.1.1 The manometer as a thermometer

Let us start with the most important point:

:::{figure} ../images/art-p082-1.svg
:alt: Illustration from the original text
:::

The ideal gas model defines by itself a temperature scale. It is proposed to measure the absolute temperature $T$ very simply with a manometer, stating that it is directly proportional to the pressure $p$ and inversely proportional to the density $\rho$.

We can thus say that the ideal gas does not describe the reality of things, that it is not a physical principle, but only a simplified model of gas behavior. Its range of validity is limited and fuzzy.

(sec-4-1-2)=
### 4.1.2 Definition: the equation of state

We will call *ideal gas* a fluid in the gaseous state whose product of pressure and volume, $pv$, remains proportional to its temperature. The proportionality constant is called the *gas constant*, denoted as $R$; it depends on the nature of the gas.

:::{math}
:label: eq-4-1
:enumerator: 4/1
pv = RT
:::

by definition for an ideal gas, where $p$ is the pressure $(Pa)$, $v$ is the specific volume $(m^{3}kg^{-1})$, $T$ is the temperature $(K)$, and $R$ is the gas constant of the considered gas $(J K^{-1}kg^{-1})$.

Equation 4/1 is called the *equation of state of ideal gases*. It can also be expressed in terms of mass:

:::{math}
:label: eq-4-2
:enumerator: 4/2
pV = mRT
:::

where $V$ is the volume $(m^{3})$, and $m$ is the mass of the gas considered $(kg)$.

:::{aside}
« The change in temperature occasioned in gases by a change in volume may be regarded as one of the most important facts of physics, owing to the numerous consequences it entails, and at the same time as one of the most difficult to elucidate and to measure by decisive experiments. It appears in several circumstances to present singular anomalies. »

Sadi Carnot, 1824 [[4](#ref-4)]
:::

:::{aside}
« M. S. Carnot, avoiding the use of mathematical analysis, arrives through a series of subtle and hard to grasp reasonings at results which are without difficulty deduced from a more general law, which I shall endeavor to establish. »

Émile Clapeyron, 1834 [[5](#ref-5)]
:::

It is also possible to express Equation 4/2 in terms of the amount of substance in moles.[^ch4-fn1] Because it is inseparable from the concept of absolute temperature, it took 150 years for this equation to take its final form: the one given by Émile Clapeyron in 1834 [[5](#ref-5)].

````{prf:example}
:label: ex-4-1
:enumerator: 4.1

A mass of $2 kg$ of gas with a constant $R = 100 J K^{-1}kg^{-1}$ is contained in a reservoir of $200 L (52.83 US gal)$ at a pressure of $3 bar (43.51 psi)$. What is its temperature?

We start from Equation 4/2 to express the temperature: $T = \frac{p V}{m R} = \frac{3\times 10^{5}\times 0.2}{2\times 100} = 300 K = 26.85^{\circ}C = 80.33 ^{\circ} F$.

Admirable Émile! The simplicity of this calculation will be missed in the next chapter.

The only thorn in this equation concerns the units, which must be properly converted to SI: $200 L = 0.2 m^{3}$ and $3 bar = 3 \times 10^{5}Pa$. The temperature is always in kelvins.

````

````{prf:example}
:label: ex-4-2
:enumerator: 4.2

Atmospheric air can be modeled as an ideal gas with $R_{\mathrm{air}}= 287 J kg^{-1}K^{-1}$. Under ambient conditions $(1 bar, 20^{\circ}C$, that is, $14.5 psi$ and $68 ^{\circ} F)$, what are the specific volume and the density of the atmosphere?

We start from Equation 4/1 to express the specific volume: $v = \frac{R T}{p} = \frac{287\times (20+273.15)}{1\times 10^{5}} = 0.841 m^{3}kg^{-1}$. The density then follows simply: $\rho = \frac{1}{v} = 1.189 kg m^{-3}$.

Once again, forgetting to convert the temperature units to kelvins would be fatal (try using $0^{\circ}C$ or $0 ^{\circ} F$).

In one cubic meter $(220 gal imp)$, we have only $1.2 kg (2.6 lb)$ of air. This is very little, especially when compared to liquid water $(1000 kg$ for the same volume). Air machines typically operate with large volumetric flow rates.

````

[^ch4-fn1]: Sometimes in other books, the constant in $J K^{-1}kg^{-1}$ is denoted as $r$. The quantity then denoted $R = 8.3143 J K^{-1}mol^{-1}$ is universal, and gases adopt different values of $r$ depending on their molar mass $M \equiv \frac{m}{n}$. In this book, we do not quantify amounts of substance.

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

(sec-4-1-3)=
### 4.1.3 What does an ideal gas represent?

The ideal gas is the simplest model one can imagine to represent the behavior of a gas.

According to this model, molecules behave like spheres bouncing off each other (figure 4.1). One can imagine a large number of very small billiard balls in chaotic motion, colliding and bouncing off each other without attracting one another or dissipating their energy through friction.

:::{figure} ../images/fig-4-1.jpg
:label: fig-4-1
:enumerator: 4.1
:alt: An ideal gas can be visualized as a set of balls in random motion. They collide without friction and without mutual attraction. The speed of each ball changes with each collision.

An ideal gas can be visualized as a set of balls in random motion. They collide without friction and without mutual attraction. The speed of each ball changes with each collision.
:::

*Diagram* CC-by-sa *by Commons User:Sharayanan & Olivier Cleynen*

In this chaos, temperature is a measure of the kinetic energy of the molecules. It is quantified by measuring the time-averaged force resulting from the impact of the molecules on a wall of the container – that is, with pressure. With this model, we can propose a temperature scale such that $T \propto p$.

The fewer molecules impacting the surface, and the more forcefully they must impact it in order to generate a given pressure. Thus, when the density $\rho$ decreases at a given pressure, it means that the temperature is increasing: we can also propose $T \propto \frac{1}{\rho}$.

If these two proposals are combined into a single equation, we obtain a simple model to quantify temperature: $T \propto pv$.

(sec-4-1-4)=
### 4.1.4 What does an ideal gas** *not* **represent?

The behavior of molecules when they are close to each other is actually very complex, since the attractive forces then play a decisive role. The influence of these forces is all the more significant when the molecules are slow and structurally complex (the interaction between two hydrocarbon molecules, for example, is more difficult to model than the interaction between two helium molecules).

The macroscopic consequences of these interactions, and the conditions under which they should no longer be neglected, are addressed in chapter 5 (*liquids and vapors*).

« Anyone who wants to analyze the properties of matter in a real problem might want to start by writing down the fundamental equations and then try to solve them mathematically. Although there are people who try to use such an approach, these people are the failures in this field; the real successes come to those who start from a *physical* point of view, people who have a rough idea where they are going and then begin by making the right kind of approximations, knowing what is big and what is small in a given complicated situation. »

Richard Feynman, 1963 [[30](#ref-30), [35](#ref-35)] *The Feynman Lectures on Physics*

For now, we will remember that the ideal gas model works better:

• When molecules collide at high speed, that is, when the gas temperature is high;

• When the average space between molecules is large, that is, when the specific volume of the gas is large.

These conditions ensure that the attractive forces between molecules can only play a minor role in the overall behavior of the gas. They are met for air in the vast majority of engineering applications. We will use the value

:::{math}
R_{\mathrm{air}}= 287 J kg^{-1}K^{-1} for pure air in our machines.
:::

(sec-4-1-5)=
### 4.1.5 Model limitations

It will not take long for the student to find the limits of Equation 4/2, which indicates that a non-zero mass of ideal gas occupies *zero volume* at zero temperature. Strictly speaking, the ideal gas cannot exist – the mathematical model loses its meaning at very low temperatures since it does not take into account the volume of the molecules themselves.

Several other equations of state can be used to better match real gases over a wider range of properties.

Thus, the *Van der Waals equation*, proposed as early as the late 18th century, suggests:

:::{math}
:label: eq-4-3
:enumerator: 4/3
(p + \frac{a}{v^{2}})(v - b) = RT
:::

where $a$ and $b$ are two constants.

This equation has the advantage of taking into account two factors ignored in the equation of state 4/1: the attractive force between molecules (the term $a/v^{2}$, which becomes part of the pressure expression) and the volume occupied by the molecules themselves (the term $b$ which is subtracted from the available volume).

Despite the difficulties inherent in quantifying the terms $a$ and $b$, these modifications have significantly extended the range of application of equations of state. They earned their author, Johannes Diderik Van der Waals, the Nobel Prize in Physics in 1910.

Building mathematical models to describe the state of real gases is an important research area in fluid mechanics. The curious student can refer to equations of state such as the Beattie-Bridgeman, Benedict-Webb-Rubin, or the Strobridge models, in order get an overview of their increasing complexity. As for us, we will stick to equation 4/1.

(sec-4-2)=
## 4.2 Properties of Ideal Gases

(sec-4-2-1)=
### 4.2.1 Two important thermal capacities

We have already discussed the concept of thermal capacity in the first chapter (1/16). It is defined as the amount of heat required to increase the temperature of one kilogram of the substance by one Kelvin (or one degree

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

Celsius, since these temperature differences are equal). Thus, we have:

:::{math}
c = \frac{\mathrm{δ}q}{dT} (4/4)
:::

where $c$ is the specific thermal capacity $(J K^{-1}kg^{-1})$, δ$q$ the (specific) infinitesimal heat transfer $(J kg^{-1})$,

and $dT$ the produced infinitesimal change in temperature $(K)$.

Since the temperature of a gas also varies when work is done on it or by it, there are an infinite number of different ways to change its temperature by one degree, by combining heat and work (figure 4.2). Each of these requires a unique amount of heat; thus, there are *infinitely many thermal capacities* associated with it.

:::{figure} ../images/fig-4-2.jpg
:label: fig-4-2
:enumerator: 4.2
:alt: Two identical quantities of gas receive the same amount of heat $Q$. The temperature increase will be lower on the right due to the work done on the piston.

Two identical quantities of gas receive the same amount of heat $Q$. The temperature increase will be lower on the right due to the work done on the piston.
:::

*Diagram* CC-0

Among these, two particular values (figure 4.3) serve as references for describing the behavior of an ideal gas:

**the thermal capacity at constant volume:** $c_{v}$,

**the thermal capacity at constant pressure:** $c_{p}$.

These two quantities are properties (or state quantities, see Appendix A4 p. 316), and we will soon use them to quantify energy in gases. In an ideal gas, $c_{v}$ and $c_{p}$ are independent of temperature. In real gases, these capacities vary with temperature (figure 4.4), but for most hand-written engineering applications, it is reasonable to use average values. For air, we will take $c_{v (\mathrm{air})}= 718 J kg^{-1}K^{-1}$ and $c_{p (\mathrm{air})}= 1005 J kg^{-1}K^{-1}$.

:::{figure} ../images/fig-4-3.jpg
:label: fig-4-3
:enumerator: 4.3
:alt: Definitions of heat capacities. On the left, the volume is fixed and the specific thermal capacity will be $c_{v}$. On the right, the pressure is constant and the capacity will be $c_{p}$.

Definitions of heat capacities. On the left, the volume is fixed and the specific thermal capacity will be $c_{v}$. On the right, the pressure is constant and the capacity will be $c_{p}$.
:::

*Diagram* CC-0

:::{figure} ../images/fig-4-4.jpg
:label: fig-4-4
:enumerator: 4.4
:alt: Specific thermal capacity of air as a function of temperature. There is a noticeable change in values in the temperature range used in engineering, which we will neglect in the scope of this book.

Specific thermal capacity of air as a function of temperature. There is a noticeable change in values in the temperature range used in engineering, which we will neglect in the scope of this book.
:::

*Data from NBS Circular 564 “Tables of Thermal Properties of Gases” (1955) up to* $1000 K$*, calculated*

*according to the model of B. G. Kyle in “Chemical and Process Thermodynamics” (1984) above* $1000 K$*, and published by Israel Urieli*

(sec-4-2-2)=
### 4.2.2 Difference of thermal capacities

The large number of equations we are discussing makes this short section 4.2.2 useful, but not essential. For the engineer, its only interest is to simplify the writing of the equations in the section that comes after it.

Let us observe the amounts of energy involved in the experiment described in figure 4.3. We supply each body with a different amount of heat to achieve the same temperature change. The difference between the two required amounts of heat comes from the fact that the gas at constant pressure (on the right) has done work during the process.

What is the difference between the thermal capacities of each? In both cases,

:::{math}
we have q_{1\rightarrow 2}+ w_{1\rightarrow 2}= \Delta u (2/2). For body A on the left, since no work is
:::

done and the process is at constant volume, we can write:

:::{math}
q_{\mathrm{A}}= c_{v}\Delta T
:::

(4/5)

:::{math}
\Delta u = q_{\mathrm{A}}
:::

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

For body B on the right, with constant pressure $p_{\mathrm{cst}.}$, we can write:

:::{math}
q_{\mathrm{B}}= c_{p}\Delta T
:::

(4/6)

:::{math}
\Delta u = q_{\mathrm{B}}+ (-p_{\mathrm{cst}.}\Delta v)
:::

By combining the two systems 4/5 and 4/6, we obtain

:::{math}
c_{v}\Delta T = c_{p}\Delta T - p_{\mathrm{cst}.}\Delta v (4/7)
:::

which simply states that the difference between the two amounts of heat supplied to the gas is found in the work done by the gas on the right. (To be truly rigorous, in order to assert that $\Delta u_{A}$ and $\Delta u_{B}$ are equal, we would need to wait for equation 4/11 which comes in the next section.)

A little algebra leads to:

:::{math}
(c_{p}- c_{v})\Delta T = p_{\mathrm{cst}.}\Delta v
:::

:::{math}
(c_{p}- c_{v}) = \frac{pv_{2}- pv_{1}}{\Delta T} = \frac{RT_{2}- RT_{1}}{\Delta T} = \frac{R \Delta T}{\Delta T}
:::

:::{math}
c_{p}- c_{v}= R (4/8)
:::

This expression only serves to simplify equation 4/13 that we will write below.

(sec-4-2-3)=
### 4.2.3 Ratio of thermal capacities

The ratio of thermal capacities at constant pressure and constant volume is named $\gamma$. Thus:

:::{math}
\gamma \equiv \frac{c_{p}}{} (4/9)
:::

:::{math}
c_{v}
:::

By returning to figure 4.3 it quickly appears that $c_{p}$ must be greater than $c_{v}$; thus $\gamma$ is always greater than $1$. We take $\gamma _{\mathrm{air}}= 1.4$.

(sec-4-3)=
## 4.3 Energy and Temperature

(sec-4-3-1)=
### 4.3.1 Historical context

The first research undertakings aimed at exploring the concept of temperature took place at the very beginning of the 19th century. The scientific community was then very interested in gases – it was noticed that there are *two* ways to increase their temperature: by heating them, but also by compressing them.

Frenchman Joseph Louis Gay-Lussac sought to understand why the temperature of a gas drops when it expands (he actually sought, according to the concepts of the time, to identify the source of the *caloric* and the reasons why it flows). He thus endeavored to produce gas expansions that were as simple as possible, and to measure the temperature. Thirty years later, the Englishman James Prescott Joule resumed and deepened these experiments, but this time, by quantifying heat as *work equivalence*. These experiments with gas balloons and thermometers are anything but spectacular – but they would play a pivotal role in thermodynamics, because they allowed for

the first time to distinguish heat, work, energy, and temperature. Joule’s meticulous work lead to the first formal expression of the first law of thermodynamics, and to the end of the caloric theory according to which heat was a very low-density and invisible fluid. Our modern unit for energy is named after him as a tribute to these results.

(sec-4-3-2)=
### 4.3.2 Joule’s law

:::{aside}
« I have taken two two-tubulure balloons, each with a capacity of twelve liters. To one of the tubulures of each balloon was adapted a faucet, and to the other a very-sensitive alcohol thermometer, whose centigrade degrees could easily be divided into hundredths[...] The vacuum having being made in both balloons, and having assured myself that they retained it exactly, I filled one of them with the gas upon which I wished to operate. About twelve hours later, I established communication between them by means of a lead pipe, and upon opening the faucets, the gas then precipitated itself into the empty balloon until the pressure equilibrium was re-established on both sides. During this time, the thermometer experienced variations which I carefully noted. »

Louis Joseph Gay-Lussac, 1807 [[3](#ref-3)]
:::

In their most remarkable experiment, Joule and Gay-Lussac were seeking to vary the pressure and volume of a gas *without transferring heat or work to it*. For this, they let a compressed gas in a container expand into a second, empty container (figure 4.5). The work done was zero, since no surface had been moved – the process was entirely irreversible. The temperature was measured and... nothing happened! Joule and Gay-Lussac measured neither heat transfer nor temperature variation.

:::{figure} ../images/fig-4-5.jpg
:label: fig-4-5
:enumerator: 4.5
:alt: The expansion of Joule and Gay-Lussac. A gas is initially trapped in a reservoir on the left; it is allowed to expand by opening the valve (in the center) which separates it from a completely empty reservoir on the right. Joule and Gay-Lussac are interested in the temperature changes measured in each reservoir. The closer the gas properties resemble the behavior of ideal gases model (§4.1.4), the smaller the temperature changes they measure, becoming undetectable for some simple gases at high temperatures.

The expansion of Joule and Gay-Lussac. A gas is initially trapped in a reservoir on the left; it is allowed to expand by opening the valve (in the center) which separates it from a completely empty reservoir on the right. Joule and Gay-Lussac are interested in the temperature changes measured in each reservoir. The closer the gas properties resemble the behavior of ideal gases model (§4.1.4), the smaller the temperature changes they measure, becoming undetectable for some simple gases at high temperatures.
:::

*Diagram* CC-0 *Olivier Cleynen*

Joule carried out a multitude of different experiments during which he observed that regardless of the supplied work, the relationship between internal energy (which varies only with work and heat) and temperature remained essentially the same – and he suggested that for an ideal gas, it always remains identical.

This postulate is known as *Joule’s law* and is posited as true for any ideal gas. It can be summarized as follows:

The temperature of an ideal gas only varies with its internal energy.

Mathematically, we can write it as:

:::{math}
:label: eq-4-10
:enumerator: 4/10
u = f(T)
:::

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

The function $f$ can be evaluated with an experiment in which the change of $u$ is quantified. For example, during a process at constant volume $q = \Delta u$ and $q = c_{v}\Delta T$. We can thus assert that the function $f$ is a simple proportional relation. With the internal energy arbitrarily set to zero at zero temperature $(u = 0 J kg^{-1}$ when $T = 0 K)$, we obtain:

:::{math}
u = c_{v}T
:::

for any ideal gas, regardless of the process (reversible or not), where $u$ is the specific internal energy $(J kg^{-1})$; $T$ is the temperature $(K)$;

and $c_{v}$ is the specific thermal capacity at constant volume $(J kg^{-1}K^{-1})$.

For a mass $m$ of ideal gas, we have of course:

:::{math}
U = m c_{v}T
:::

As long as our fluid behaves as an ideal gas, this relation 4/11 remains true. It works for any process, reversible or not, and regardless of volume, pressure, or temperature constraints.

On the other hand, it should be noted that this equation 4/11, which results from Joule’s law, does not work all for liquids and vapors. For example, we can add energy to a mass of boiling water without its temperature increasing. We will study liquids and vapors in chapter 5.

````{prf:example}
:label: ex-4-3
:enumerator: 4.3

The specific thermal capacity at constant volume for air is measured at $c_{v (\mathrm{air})}= 718 J kg^{-1}K^{-1}$. We take a mass of $0.5 kg$ of air at $20^{\circ}C$ and transfer $+15 kJ$ as heat and $-10 kJ$ as work. What is its final temperature?

We know that the energy has varied with the transfers: $\Delta U = W_{\mathrm{A}\rightarrow \mathrm{B}}+ Q_{\mathrm{A}\rightarrow \mathrm{B}}= m c_{v}\Delta T$. Thus, the temperature has varied proportionally: $T_{\mathrm{B}}= T_{\mathrm{A}}+ \frac{\Delta U}{m c_{v}} = T_{\mathrm{A}}+ \frac{W_{\mathrm{A}\rightarrow \mathrm{B}}+ Q_{\mathrm{A}\rightarrow \mathrm{B}}}{m c_{v}}= 20 + \frac{-10\times 10^{3}+(+15\times 10^{3})}{0.5\times 718}$

Good old James! We just only need to quantify the energy

changes to know the temperature, and vice versa.

Here the temperatures in $degrees Celsius$ are only added and a

conversion to kelvins would not have changed the result. In case of doubt, it is better not to take this shortcut.

````

(sec-4-3-3)=
### 4.3.3 Enthalpy of an ideal gas

Because we have just linked the internal energy $u$ to the temperature, and because and the product $pv$ also depends on the temperature, we can now easily express the enthalpy $h$ of an ideal gas in terms of temperature only.

Indeed, we have $h \equiv u + pv$ (3/12); with a quick insertion of equations 4/1 and 4/11 we can write, for any ideal gas:

:::{math}
h = u + pv = c_{v}T + RT = (c_{v}+ R) T
:::

« The difference between the means of tile experiments and interpolations being exactly such as was found to be due to the increased effect of the temperature of the room in the latter case, we arrive at the conclusion, that *no change of temperature occurs when air is allowed to expand in such a manner as not to develope mechanical*

(4/11) *power*. »

James Prescott Joule, 1845 [[8](#ref-8)]

(4/12)

$_{0.5\times 718}= 33.92^{\circ}C$.

(4/13)

expression to obtain:

For any ideal gas,

where $h$ is the specific enthalpy $(J kg^{-1})$; $T$ is the temperature $(K)$;

and

````{prf:example}

at $c_{p (\mathrm{air})}= 1005 J kg^{-1}K^{-1}$.

compressor to the air?

energy…

````

### 4.3.4

temperature $T$:

quantify these three forms of energy.

```{exercise}
:label: prob-4-4
:enumerator: 4.4

Using the equation 4/8 that we developed earlier, we can simplify this $h = c_{p}T$ (4/14) regardless of the process (reversible or not), $c_{p}$ is the specific thermal capacity at constant pressure $(J kg^{-1}K^{-1})$. Example 4.4 The specific thermal capacity at constant pressure for air is measured A flow rate of $2 kg s^{-1}$ of air passes through a compressor, where its temperature increases by $150^{\circ}C$. What is the power supplied by the We know that the change energy is directly proportional to the change in temperature. Using equations 3/14 and 4/14, we obtain:$\dot{W}_{\mathrm{A}\rightarrow \mathrm{B}}+\dot{} Q_{\mathrm{A}\rightarrow \mathrm{B}}=\dot{m} \Delta h =\dot{m} c_{p}\Delta T = 2 \times 1005 \times (+150) = +301.5 kW$. With an ideal gas, a simple thermometer is enough to quantify...but not to differentiate work and heat. Here we cannot separate$\dot{W}_{\mathrm{A}\rightarrow \mathrm{B}}$ from$\dot{Q}_{\mathrm{A}\rightarrow \mathrm{B}}$. We also cannot predict the state of the gas at the outlet, that is its pressure $p$ and specific volume $v$ (only their product). For this, a precise description of what happens between the inlet and the outlet would be needed.

:::{admonition} Answer
:class: dropdown

$w_{1\rightarrow 2}= \Delta h = c_{p}\Delta T = +85.4 kJ kg^{-1}$ (3/15 & 4/13)

:::
```

**Interlude: what to remember so far**

The ideal gas is a model for quantifying the temperature of a gas. According

to this model, the three main forms of energy we have used so far — internal

energy $u$, enthalpy $h$, and the term $pv$ — are directly proportional to the

$u = c_{v}T (J kg^{-1})$

$h = c_{p}T (J kg^{-1})$

$pv = RT (J kg^{-1})$

If we measure the absolute temperature of a gas, then we can immediately

**Elementary Reversible Processes**

Here we intend to calculate the properties of an ideal gas, as well as

the energy transfers involved, when it is compressed or expanded under

completely arbitrary constraints of volume, pressure, or temperature.

*Engineering Thermodynamics* by Olivier Cleynen

(sec-4-4-1)=
### 4.4.1 What is this chapter section for?

The gas processes we study here are very hypothetical and not necessarily exciting, but they deserve the attention of the student for two reasons:

1. The behavior of gases is inherently complex, even when we use the ideal gas model. These elementary processes serve as small exercises for us, to help us learn step by step;

2. These elementary processes are conceptual tools that we will later assemble, first to quantify the theoretical limits of machines (in chapter 7), and then to describe the behavior of gases inside real machines (in chapter 10).

(sec-4-4-2)=
### 4.4.2 Processes at constant pressure

It is possible to heat or cool a gas while maintaining its pressure constant (figure 4.6). A process at constant pressure is called *isobaric*. In order to generate such a process, we can:

• with a closed system, heat or cool the gas while maintaining a constant force on the walls;

• with an open system, heat or cool the gas by simply letting it flow in a duct, without any moving parts. This is the case, for example, in the combustion chamber of a jet engine.

When the pressure is constant, the properties of the gas vary according to the relation

:::{math}
T
:::

$v =$ constant (4/15)

:::{figure} ../images/fig-4-6.jpg
:label: fig-4-6
:enumerator: 4.6
:alt: A constant-pressure (isobaric) process undergone by an ideal gas. In a closed system (left), the piston exerts a constant force throughout the process. In an open system (right), no work is done.

A constant-pressure (isobaric) process undergone by an ideal gas. In a closed system (left), the piston exerts a constant force throughout the process. In an open system (right), no work is done.
:::

*Diagram* CC-0 *Olivier Cleynen*

:::{figure} ../images/fig-4-7.jpg
:label: fig-4-7
:enumerator: 4.7
:alt: Heating at constant pressure of an ideal gas, represented on a pressure-volume diagram.

Heating at constant pressure of an ideal gas, represented on a pressure-volume diagram.
:::

*Diagram* CC-0 *Olivier Cleynen*

:::{math}
In a closed system, we have q_{1\rightarrow 2}+ w_{1\rightarrow 2}= \Delta u (2/2) and, if the process is
:::

reversible, heat and work can be easily related to the temperature:

:::{math}
2 2
:::

:::{math}
w_{1\rightarrow 2}= -\int pdv = -p_{\mathrm{cst}.}\int dv = -p_{\mathrm{cst}.}\Delta v
:::

:::{math}
1 1
:::

:::{math}
:label: eq-4-16
:enumerator: 4/16
w_{1\rightarrow 2}= -R \Delta T
:::

during a reversible process at constant pressure $p_{\mathrm{cst}.}$, in a closed system.

and we notice that the work is of opposite sign to the change in temperature.

Heat can be easily quantified:

:::{math}
q_{1\rightarrow 2}= \Delta u - w_{1\rightarrow 2}= \Delta u + p_{\mathrm{cst}.}\Delta v = \Delta h
:::

:::{math}
:label: eq-4-17
:enumerator: 4/17
q_{1\rightarrow 2}= c_{p}\Delta T
:::

during a reversible process at constant pressure, in a closed system.

When the process takes place in an open system, we have $q_{1\rightarrow 2}+ w_{1\rightarrow 2}=$

$\Delta h$ (3/15), and, if the process is reversible, heat and work can be easily

quantified:

:::{math}
2
:::

:::{math}
w_{1\rightarrow 2}= \int vdp
:::

:::{math}
1
:::

:::{math}
:label: eq-4-18
:enumerator: 4/18
w_{1\rightarrow 2}= 0
:::

during a reversible process at constant pressure, in an open system.

The work is of course zero, since there are no moving parts present to mechanically extract energy from the gas.

Heat is then responsible for the entire change in temperature:

:::{math}
q_{1\rightarrow 2}= \Delta h - w_{1\rightarrow 2}= \Delta h
:::

:::{math}
:label: eq-4-19
:enumerator: 4/19
q_{1\rightarrow 2}= c_{p}\Delta T
:::

during a reversible process at constant pressure, in an open system.

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

````{prf:example}
:label: ex-4-5
:enumerator: 4.5

For air, we have $c_{p (\mathrm{air})}= 1005 J kg^{-1}K^{-1}, c_{v (\mathrm{air})}= 718 J kg^{-1}K^{-1}, R_{\mathrm{air}}= 287 J kg^{-1}K^{-1}$. How much energy is needed to heat the air in a $30 m^{2} (322.9 ft^{2})$ apartment from $10^{\circ}C$ to $20^{\circ}C (50 ^{\circ} F$ to $68 ^{\circ} F)$?

The heating will likely take place at constant pressure (unless the apartment is hermetically sealed, the pressure will be atmospheric everywhere and the air will “leak” under the doors). We assume a pressure of 1 bar and a ceiling height of $2.5 m$. We use a closed system encompassing all the heated air.

We have a volume of $75 m^{3}$, which leads to the total mass of air as $m_{\mathrm{A}}= \frac{p_{\mathrm{A}}V_{\mathrm{A}}}{R T_{\mathrm{A}}} = \frac{1\times 10^{5}\times 75}{287\times (10+273.15)}= 92.29\,\mathrm{kg} = 203.5\,\mathrm{lb}$. The heat required to heat this amount of air at constant pressure can be quantified with equation 4/17: $Q_{\mathrm{A}\rightarrow \mathrm{B}}= m c_{p}\Delta T = 93.29 \times 1005 \times (20 - 10) = +9.28 \times 10^{5}J = +928 kJ$.

This result represents the final *net* heat transfer to the air (after

losses to walls and windows, as well as transfers that compensate for them).

Conversely, cooling would cause outside air to come in, which

would need to be taken into account in the mass calculation.

````

(sec-4-4-3)=
### 4.4.3 Processes at constant volume

It is possible to heat or cool a gas while maintaining its volume constant (figure 4.8). A process at constant volume is called *isochoric*.

• With a closed system, we can heat or cool a gas in a fixed and closed reservoir. This is the case, for example, during the combustion phase in a gasoline engine.

• With an open system, the manipulation is more complex. When heating the gas, we must compress it, in order to prevent its volume from increasing; conversely, while cooling it, we must expand it so as to prevent its volume from decreasing. This manipulation has no common practical application.

When the specific volume of a perfect gas is constant, its properties vary according to the relation

:::{math}
T
:::

$p =$ constant (4/20)

In a closed system, we have $q_{1\rightarrow 2}+w_{1\rightarrow 2}= \Delta u$and, if the process is reversible, heat and work can be easily related to temperature.

Since the volume does not change, the work is of course zero:

:::{math}
2
:::

:::{math}
w_{1\rightarrow 2}= -\int pdv
:::

:::{math}
1
:::

:::{math}
w_{1\rightarrow 2}= 0 (4/21)
:::

during a reversible process at constant volume, in a closed system.

maintain the specific volume constant.

volume diagram.

:::{figure} ../images/fig-4-8.jpg
:label: fig-4-8
:enumerator: 4.8
:alt: A constant-volume (isochoric) process undergone by an ideal gas. In a closed system (left), the volume is fixed and no work is done. In an open system (right), the gas must be compressed while heating and expanded while cooling, to

A constant-volume (isochoric) process undergone by an ideal gas. In a closed system (left), the volume is fixed and no work is done. In an open system (right), the gas must be compressed while heating and expanded while cooling, to
:::

closed system (left), the volume is fixed and no work is done. In an open system (right), the gas must be compressed while heating and expanded while cooling, to

*Diagram* CC-0 *Olivier Cleynen*

:::{figure} ../images/fig-4-9.jpg
:label: fig-4-9
:enumerator: 4.9
:alt: Cooling of an ideal gas at constant volume, represented on a pressure-

Cooling of an ideal gas at constant volume, represented on a pressure-
:::

*Diagram* CC-0 *Olivier Cleynen*

*Engineering Thermodynamics* by Olivier Cleynen

The heat transfer can be easily quantified:

:::{math}
q_{1\rightarrow 2}= \Delta u - w_{1\rightarrow 2}= \Delta u
:::

:::{math}
q_{1\rightarrow 2}= c_{v}\Delta T (4/22)
:::

during a reversible process at constant volume, in a closed system.

When the process occurs in an open system, we have $q_{1\rightarrow 2}+ w_{1\rightarrow 2}= \Delta h$

and, if the process is reversible, heat and work can be quantified, although

with a little more difficulty:

:::{math}
w_{1\rightarrow 2}= \int _{1}^{2}vdp = v_{\mathrm{cst}.}\int _{1}^{2}dp = v_{\mathrm{cst}.}\int _{1}^{2} \frac{R}{v_{\mathrm{cst}.}} dT = R\int _{1}^{2}dT
:::

:::{math}
w_{1\rightarrow 2}= R \Delta T (4/23)
:::

during a reversible process at constant volume, in an open system.

One can then easily quantify the heat to be supplied:

:::{math}
q_{1\rightarrow 2}= \Delta h - w_{1\rightarrow 2}= c_{p}\Delta T - R \Delta T
:::

:::{math}
q_{1\rightarrow 2}= c_{v}\Delta T (4/24)
:::

during a reversible process at constant volume, in an open system.

````{prf:example}
:label: ex-4-6
:enumerator: 4.6

For air, we measure $c_{p (\mathrm{air})}= 1005 J kg^{-1}K^{-1}, c_{v (\mathrm{air})}= 718 J kg^{-1}K^{-1}$, $R_{\mathrm{air}}= 287 J kg^{-1}K^{-1}$. In a cylinder of a gasoline engine, air is at a pressure of $17 bar (246.6 psi)$ with a density of $9.4 kg m^{-3}$. The combustion of the fuel (so fast that the volume does not have time to vary) results in the supply of $1450 kJ kg^{-1}$ of heat. What are the temperature and pressure values reached?

Initially, the temperature is $T_{\mathrm{A}}= \frac{p_{\mathrm{A}}v_{\mathrm{A}}}{R} = \frac{p_{\mathrm{A}}}{\rho _{A}R} = \frac{17\times 10^{5}}{9.4\times 287} = 630.1 K = 357^{\circ}C = 674.5 ^{\circ} F$. We use a closed system consisting of the mass of air. Since the volume does not change, the work is zero (4/21) and it is the heat transfer which changes the internal energy (4/22): $q_{\mathrm{A}\rightarrow \mathrm{B}}= \Delta u - w_{\mathrm{A}\rightarrow \mathrm{B}}= \Delta u = c_{v}\Delta T$; thus $T_{\mathrm{B}}= T_{\mathrm{A}}+ \frac{q_{\mathrm{A}\rightarrow \mathrm{B}}}{c_{v}} = 630.1 + \frac{1450\times 10^{3}}{718} = 2649.6 K = 2376.5^{\circ}C = 4309.6 ^{\circ} F$. The final pressure is obtained by comparing the final condition and the initial condition (4/20): $\frac{RT_{\mathrm{A}}}{p_{\mathrm{A}}} = v_{\mathrm{A}}= v_{\mathrm{B}}= \frac{RT_{\mathrm{B}}}{p_{\mathrm{B}}}$; thus $p_{\mathrm{B}}= \frac{T_{\mathrm{B}}}{T_{\mathrm{A}}} p_{\mathrm{A}}= \frac{2649.6}{630.1} \times 17 \times 10^{5}= 7.148 \times 10^{6}Pa = 71.5 bar = 1037 psi$.

Care must be taken with temperatures in the fractions, where

they must be expressed in kelvins.

The maximum temperature, exceeding $2300^{\circ}C$, surpasses the

melting temperature of most metals. In a gasoline engine, this temperature is only reached sporadically, with each combustion.

The data in this example mimic those of problem 2.5 p. 54. This

time, we can predict the final conditions without having to make any measurements.

````

(sec-4-4-4)=
### 4.4.4 Processes at constant temperature

:::{aside}
« It is easy to imagine a small quantity of gaseous or liquid combustible, or dust coal, gradually introduced into a volume of compressed and highly heated air, and burning by spontaneous or separate ignition. The piston is forced out at the same time in such a way that no increase of temperature takes place, because the heat developed by each particle of combustible is instantly absorbed by the cooling due to expansion. Therefore the whole of the heat developed will be transformed into work. »

Rudolf Diesel, 1893

*Theorie und Konstruktion eines rationellen Wärmemotors zum Ersatz der Dampfmaschinen und der heute bekannten Verbrennungsmotoren* [[23](#ref-23), [24](#ref-24)]
:::

It is possible to heat or cool a gas while maintaining its temperature constant (figure 4.10). A process at constant temperature is called *isothermal*.

For an ideal gas, a process at constant temperature always occurs at constant energy. For each joule of heat supplied to the gas, one joule of work must be extracted from it; conversely, every heat withdrawal must be compensated by an equal amount of work input.

In practice, this complexity makes it so that isothermal heat transfers are rarely used in industry. However, they have crucial theoretical importance, which we will explore in chapter 7 (*the second law*).

When the temperature of an ideal gas remains constant, its properties vary according to the relation

:::{math}
:label: eq-4-25
:enumerator: 4/25
p v = constant
:::

In a closed system, we have $q_{1\rightarrow 2}+w_{1\rightarrow 2}= \Delta u$, and if the process is reversible, heat and work can be related to the properties of the gas, although not

:::{figure} ../images/fig-4-10.jpg
:label: fig-4-10
:enumerator: 4.10
:alt: A constant-temperature (isothermal) process undergone by an ideal gas. In a closed system (left), the gas is allowed to do work on a piston while being heated, and conversely, work is done on the gas when it is cooled. In an open system (right), the same manipulations are carried out continuously.

A constant-temperature (isothermal) process undergone by an ideal gas. In a closed system (left), the gas is allowed to do work on a piston while being heated, and conversely, work is done on the gas when it is cooled. In an open system (right), the same manipulations are carried out continuously.
:::

*Diagram* CC-0 *Olivier Cleynen*

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

:::{figure} ../images/fig-4-11.jpg
:label: fig-4-11
:enumerator: 4.11
:alt: Expansion (heating) at constant temperature of an ideal gas, represented on a pressure-volume diagram.

Expansion (heating) at constant temperature of an ideal gas, represented on a pressure-volume diagram.
:::

without some difficulty.

:::{math}
2
:::

$w_{1\rightarrow 2}= -\int pdv = -\int R T_{\mathrm{cst}.}v dv = -R T_{\mathrm{cst}.}\int$

:::{math}
1
:::

$w_{1\rightarrow 2}= R T_{\mathrm{cst}.}\ln (v_{1}$

:::{math}
v_{2})
:::

during a reversible process at constant temperature, in a closed system.

One can also express work in terms of pressure, since with equation 4/25, we have:

:::{math}
= \frac{p_{2}}{}
:::

:::{math}
\frac{v_{1}}{}
:::

:::{math}
v_{2}p_{1}
:::

thus:

:::{math}
w_{1\rightarrow 2}= R T_{\mathrm{cst}.}\ln (\frac{p_{2}}{}
:::

:::{math}
p_{1})
:::

during a reversible process at constant temperature, in a closed system.

The heat transfer can be easily quantified. Indeed, the internal energy does

not change:

:::{math}
q_{1\rightarrow 2}= \Delta u - w_{1\rightarrow 2}= 0 - w_{1\rightarrow 2}
:::

:::{math}
q_{1\rightarrow 2}= -w_{1\rightarrow 2}
:::

during a reversible process at constant temperature, in a closed system.

When the process occurs in an open system, we have $q_{1\rightarrow 2}+ w_{1\rightarrow 2}= \Delta h$

and, if the process is reversible, heat and work can be quantified in the same

way:

$w_{1\rightarrow 2}= \int ^{2}vdp = \int ^{2}R T_{\mathrm{cst}.}p dp = R T_{\mathrm{cst}.}\int ^{2}$

:::{math}
1 1 1
:::

$w_{1\rightarrow 2}= R T_{\mathrm{cst}.}\ln (\frac{p_{2}}{p_{1}} ) = R T_{\mathrm{cst}.}\ln (v_{1}$

:::{math}
v_{2})
:::

during a reversible process at constant temperature, in an open system.

*Diagram* CC-0 *Olivier Cleynen*

$2 1 v dv = -R T_{\mathrm{cst}.}[\ln v]^{v}_{v^{2}_{1}}$

$1$

(4/26)

« $^{\mathrm{When} \mathrm{a} \mathrm{gas} \mathrm{varies} \mathrm{in} \mathrm{volume} \mathrm{with}-}$ *out changing temperature, the quantities of heat absorbed or released by this gas are in arithmetic progression, if the increases or reductions in volume happen to be in geometric progression.* When one compresses a liter of air maintained at the temperature of 10°,

(4/27) and it is reduced to 1/2 liter, a certain quantity of heat is released. This quantity will always be the same if one again reduces the volume from 1/2 liter to 1/4 liter, from 1/4 liter to 1/8, and so on. »

Sadi Carnot, 1824 [[4](#ref-4)]

(4/28)

$1 p dp = R T_{\mathrm{cst}.}[\ln p]^{p_{2}} p_{1}$

(4/29)

This relation, identical to equation 4/27, should not surprise the insightful student, since the $pv =$ constant relationship ensures that for two given points in figure 4.11, the area under the curve is always equal to the area to the left of the curve.

The heat transfer can be quantified without difficulty, of course:

:::{math}
q_{1\rightarrow 2}= \Delta h - w_{1\rightarrow 2}= 0 - w_{1\rightarrow 2}
:::

:::{math}
:label: eq-4-30
:enumerator: 4/30
q_{1\rightarrow 2}= -w_{1\rightarrow 2}
:::

during a reversible process at constant temperature, in an open system.

````{prf:example}
:label: ex-4-7
:enumerator: 4.7

For air, we measure $c_{p (\mathrm{air})}= 1005 J kg^{-1}K^{-1}, c_{v (\mathrm{air})}= 718 J kg^{-1}K^{-1}$, $R_{\mathrm{air}}= 287 J kg^{-1}K^{-1}$. A mass of $2.5 kg (5.512 lb)$ of air in a reservoir is at a pressure of $2 bar (29.01 psi)$ and a temperature of $800^{\circ}C (1472 ^{\circ} F)$. We want to supply it with $100 kJ$ of heat without changing its temperature. What should be the transfer of work? What will be the volume and pressure in the end?

The work is easy to determine: $W_{\mathrm{A}\rightarrow \mathrm{B}}+ Q_{\mathrm{A}\rightarrow \mathrm{B}}= \Delta U = 0$ here since the temperature does not change. Thus, $W_{\mathrm{A}\rightarrow \mathrm{B}}= -Q_{\mathrm{A}\rightarrow \mathrm{B}}= -100 kJ$ (the gas must provide as much work as it receives as heat). The final properties are obtained using equation 4/26:

:::{math}
w_{\mathrm{A}\rightarrow \mathrm{B}}= R T_{\mathrm{cst}.}\ln (\frac{v_{\mathrm{A}}}{v_{\mathrm{B}}}) = R T_{\mathrm{cst}.}\ln (\frac{V_{\mathrm{A}}}{V_{\mathrm{B}}})
:::

:::{math}
\frac{V_{\mathrm{A}}}{V_{\mathrm{B}}} = \exp [\frac{w_{\mathrm{A}\rightarrow \mathrm{B}}}{R T_{\mathrm{cst}.}}] = \exp [\frac{W_{\mathrm{A}\rightarrow \mathrm{B}}}{m R T_{\mathrm{cst}.}}]
:::

:::{math}
= \exp [\frac{-100 \times 10^{3}}{2.5 \times 287 \times (800 + 273.15)}] = 0.878207
:::

Aobntda isnin ac ef in$V$aAl $=$vo l$^{\frac{m R T_{\mathrm{A}}}{p_{\mathrm{A}}}}$um e $V=_{\mathrm{B}}=^{2.5\times}\frac{V_{\mathrm{A}}2\times 10}{0.878207}^{287\times (800 _{5}+}= ^{2 7}4^{3}.^{.1}3^{5}8^{)}4= m 3_{3}. 8=5 1m1^{3}5 8= U 1S0 1g7a lU. S gal$, we Finally, the final pressure is obtained by comparing the final and initial states: $p_{\mathrm{A}}V_{\mathrm{A}}= m R T_{\mathrm{A}}= m R T_{\mathrm{B}}= p_{\mathrm{B}}V_{\mathrm{B}}$ (or with equation 4/27): $p_{\mathrm{B}}= p_{\mathrm{A}} \frac{V_{\mathrm{A}}}{V_{\mathrm{B}}} = 2\times 10^{5}\times 0.878 207 = 1.756\times 10^{5}Pa = 1.756 bar = 25.47 psi$.

The volume increases and the pressure decreases, since the gas

is doing work while it receives heat.

It is difficult to hide that this type of process is rarely used in

practice, but it will serve us to develop an extraordinary absolute thermometer-engine-refrigerator, in chapter 7 (*the second law*).

````

(sec-4-4-5)=
### 4.4.5 Reversible adiabatic processes

An *adiabatic* process is one where there is no heat transfer (figure 4.12). This can be achieved by wrapping the gas container or duct with a thick layer of thermal insulation.

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

:::{figure} ../images/fig-4-12.jpg
:label: fig-4-12
:enumerator: 4.12
:alt: A reversible adiabatic (isentropic) process undergone by an ideal gas. In a closed system (left) as well as in an open system (right), the apparatus is perfectly insulated, so that there is no heat transfer, even if the gas temperature varies.

A reversible adiabatic (isentropic) process undergone by an ideal gas. In a closed system (left) as well as in an open system (right), the apparatus is perfectly insulated, so that there is no heat transfer, even if the gas temperature varies.
:::

A *reversible adiabatic* process is carried out infinitely slowly. A piston in a cylinder will need to be moved infinitely slowly for this, and a steady-flow compressor will need to be infinitely long. Later, in chapter 8 (*entropy*), we will call these processes *isentropic*.

It must be noted that even though there is absolutely no heat transfer, the temperature must necessarily vary in such a process, since the work is non-zero. This temperature change is often the intended effect, as we will see in chapter 7 (*the second law*).

In a closed system, we have $q_{1\rightarrow 2}+w_{1\rightarrow 2}= \Delta u$and, if the process is reversible, heat and work are quantified without any difficulty:

:::{math}
q_{1\rightarrow 2}= 0
:::

during a reversible adiabatic process, by definition.

:::{math}
w_{1\rightarrow 2}= \Delta u - q_{1\rightarrow 2}= \Delta u
:::

:::{math}
w_{1\rightarrow 2}= c_{v}\Delta T
:::

during a reversible adiabatic process in a closed system.

When the process occurs in an open system, we have $q_{1\rightarrow 2}+ w_{1\rightarrow 2}= \Delta h$

and we can also write:

:::{math}
q_{1\rightarrow 2}= 0
:::

:::{math}
w_{1\rightarrow 2}= c_{p}\Delta T
:::

*Diagram* CC-0 *Olivier Cleynen*

(4/31)

(4/32)

(4/33)

(4/34)

:::{figure} ../images/fig-4-13.jpg
:label: fig-4-13
:enumerator: 4.13
:alt: Reversible adiabatic expansion of an ideal gas, represented on a pressure-volume diagram.

Reversible adiabatic expansion of an ideal gas, represented on a pressure-volume diagram.
:::

*Diagram* CC-0 *Olivier Cleynen*

during a reversible adiabatic process, in an open system.

Unfortunately, these two equations 4/32 and 4/34 are of no use until we have predicted the temperature $T_{2}$ at the end of the process. However, in a reversible adiabatic process, nothing remains constant: the specific volume, pressure, and temperature all vary. How can we quantify these properties?

Let us start with an infinitely small adiabatic process in a closed system.

When the process is reversible, δ$w = -pdv$ and then:

:::{math}
δ q = du - δ w = 0
:::

:::{math}
du + pdv = 0
:::

By using $du = c_{v}dT$ for an ideal gas and $p = RT/v$, we can rewrite this

equation as:

:::{math}
c_{v}dT + \frac{RT}{v} dv = 0
:::

:::{math}
1 1
:::

:::{math}
\frac{}{T} dT + \frac{R}{} \frac{}{v} dv = 0
:::

:::{math}
c_{v}
:::

By integrating between two states 1 and 2:

:::{math}
\ln (\frac{T_{2}}{} \frac{}{} \ln (\frac{v_{2}}{v_{1}}) = 0
:::

:::{math}
T_{1}) + ^{\frac{R}{c_{v}}}
:::

:::{math}
\frac{R}{}
:::

:::{math}
\ln (\frac{T_{2}}{T_{1}}) + \ln (\frac{v_{2}}{} ^{cv}= 0
:::

:::{math}
v_{1})
:::

:::{math}
\frac{R}{}
:::

:::{math}
:label: eq-4-35
:enumerator: 4/35
\ln (\frac{T_{2}}{T_{1}}) = \ln (\frac{v_{1}}{} cv
:::

:::{math}
v_{2})
:::

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

And since $R = c_{p}- c_{v}$ (4/8) and $\gamma \equiv c_{p}/c_{v}$ (4/9), we have $\frac{R}{c_{v}} = \gamma - 1$, which allows us to reformulate equation 4/35 above as:

:::{math}
\frac{T_{2}}{} \frac{v_{1}}{} \gamma -1
:::

:::{math}
(T_{1}) = (v_{2})
:::

Thus, we have linked temperature and specific volume when the process is reversible adiabatic (devoid of heat transfer and infinitely slow).

Some algebraic manipulations, which are left to the student to revise, allow

us to derive this expression in terms of pressure. We thus obtain the

following three relations:

:::{math}
\frac{T_{1}}{} \frac{v_{2}}{} \gamma -1
:::

:::{math}
(T_{2}) = (v_{1})
:::

(4/36)

:::{math}
\frac{\gamma -1}{}
:::

:::{math}
\frac{T_{1}}{} \frac{p_{1}}{}
:::

:::{math}
\gamma
:::

:::{math}
(T_{2}) = (p_{2})
:::

(4/37)

:::{math}
\frac{p_{1}}{} \frac{v_{2}}{} \gamma
:::

:::{math}
(p_{2}) = (v_{1})
:::

(4/38)

for any reversible adiabatic process.

This last equation 4/38 is equivalent to the expression:

$pv^{\gamma}=$ constant (4/39)

for any reversible adiabatic process.

````{prf:example}
:label: ex-4-8
:enumerator: 4.8

For air, we have $c_{p (\mathrm{air})}= 1005 J kg^{-1}K^{-1}, c_{v (\mathrm{air})}= 718 J kg^{-1}K^{-1}, R_{\mathrm{air}}= 287 J kg^{-1}K^{-1}$, and $\gamma _{\mathrm{air}}= 1.4$. A compressed air tank of $200 L (52.83 US gal)$ contains air at 40 bar and $50^{\circ}C (580.2 psi$ and $122 ^{\circ} F)$. The ambient atmosphere is at $1 bar (14.5 psi)$. What is the maximum amount of work that can be extracted from the compressed air without supplying heat?

The maximum work will be obtained if the expansion is reversible. Since we are not allowed to supply heat, our best option here is to perform a reversible adiabatic expansion from 40 bar to 1 bar. We want to calculate the final temperature, since it will give us the change in energy, thus the work done by the gas. Among the three daunting relations 4/36 to 4/38, it is the second one that interests us:

With $\left(\frac{T_{\mathrm{A}}}{T_{\mathrm{B}}}\right) = \left(\frac{p_{\mathrm{A}}}{p_{\mathrm{B}}}\right)^{\frac{\gamma-1}{\gamma}}$. Thus: $T_{\mathrm{B}}= T_{\mathrm{A}}(\frac{p_{\mathrm{A}}}{p_{\mathrm{B}}} ) ^{\gamma}= (50 + 273.15) ( \frac{40}{1} )^{-\frac{1.4-1}{1.4}} = 112.6 K = -160.5^{\circ}C = -257 ^{\circ} F$. The work done by the closed system composed of the gas is therefore $w_{\mathrm{A}\rightarrow \mathrm{B}}= \Delta u - q_{\mathrm{A}\rightarrow \mathrm{B}}= c_{v}\Delta T - 0 = 718 \times (-160.5 - 50) = -1.5115 \times 10^{5}J kg^{-1}= -151.1 kJ kg^{-1}$. By calculating the mass $m_{\mathrm{A}}= \frac{p_{\mathrm{A}}V_{\mathrm{A}}}{R T_{\mathrm{A}}} = \frac{40\times 10^{5}\times 0.2}{287\times (50+273.15)}= 8.626\,\mathrm{kg}$, we obtain $W_{\mathrm{A}\rightarrow \mathrm{B}}= m_{\mathrm{A}}w_{\mathrm{A}\rightarrow \mathrm{B}}= 8.626 \times -151.1 \times 10^{3}= -1.3038 \times 10^{6}J = -1.304 MJ$.

This amount of energy is enough to accelerate, without friction,

:::{math}
0.5
:::

a vehicle weighing $1 t$ to a speed $C = [\frac{1.3038\times 10^{6}}{^{1}_{2}\times 1000} ] = 51.1 m s^{-1}\approx 180 km/h \approx 114 mph$.

The final temperature, $-160^{\circ}C$ (!), reminds us not to confuse

“adiabatic” with “constant temperature”.

In the fractions, the pressures can be left in bars or $psi$, but the

temperatures cannot remain in $^{\circ}C$ or $^{\circ} F$.

The expansion corresponds to the maximum work because it is

reversible. If it were not reversible, then the temperature of the gas would drop less and the work would be lower (we would still have $w = c_{v}\Delta T)$. In the most extreme case, that of Joule and Gay-Lussac’s expansion (§4.3.2), the temperature would remain at $50^{\circ}C$ and no work would be done.

````

(sec-4-4-6)=
### 4.4.6 Arbitrary processes

It is important to keep in mind that in practice, the properties of a gas can be *changed in any arbitrary manner* (figure 4.14).

:::{figure} ../images/fig-4-14.jpg
:label: fig-4-14
:enumerator: 4.14
:alt: An entirely arbitrary process undergone by an ideal gas represented on a pressure-volume diagram. Such a process requires a complex combination of heat and work transfers, which the student is invited to conceptualize.

An entirely arbitrary process undergone by an ideal gas represented on a pressure-volume diagram. Such a process requires a complex combination of heat and work transfers, which the student is invited to conceptualize.
:::

CC-0 *Olivier Cleynen*

We have focused on four specific processes of ideal gases, since each plays an important role for physicists and engineers in the design of thermal machines. However, this should not limit our way of thinking about a gas or the changes it may undergo. By cleverly controlling heat and work transfers, we can certainly cause any arbitrary process.

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

::::{admonition} A Bit of History:
:class: note
:label: hist-4-10

the sum of the masses multiplied by the squares of

the velocities due to the action of the accelerating

Lavoisier and Laplace’s Inquiries forces. In the hypothesis we are examining, heat is the vis viva resulting from the imperceptible

\* movements of the molecules of a body; it is the

*By Philippe Depondt* sum of the products of the mass of each molecule

*Pierre and Marie Curie University, Paris* by the square of its velocity.

If one brings into contact two bodies whose tem-

The debates on the nature of heat continued until peratures are different, the quantities of motion

the end of the 19th century with the gradual ac-they will mutually communicate will initially be

ceptance of atomic theories. An important step unequal; the vis viva of the colder body will inin this reflection is succinctly and eloquently precrease by the same amount by which the vis viva

sented in the *Mémoire sur la chaleur* (Memoir on of the other will decrease, and this increase will

Heat), 1780 [[1](#ref-1)] by the French physicists Lavoisier continue until the quantities of motion communiand Laplace: cated from one to the other are equal; in this state, the temperature of the bodies will have reached

“Physicists are divided on the nature of heat. uniformity.

Many among them regard it as a fluid spread This way of regarding heat easily explains why

throughout nature, and of which bodies are more the direct impulse of solar rays is negligible, while

or less penetrated, according to their temperature they produce a great amount of heat. Their imand their particular disposition to retain it; it can pulse is the product of their mass by their simple

combine with them, and, in this state, it ceases to velocity; now, although this velocity is excessive,

act on the thermometer and to transfer from one their mass is so small that this product is almost

body to another; it is only in the state of freedom, nil, whereas their vis viva, being the product of

which allows it to establish equilibrium within their mass by the square of their velocity, repbodies, that it forms what we call *free heat*. resents heat of an order much superior to that

Other physicists think that heat is merely the of their direct impulse. This impulse on a white

result of the imperceptible movements of the body, which abundantly reflects light, is greater

molecules of matter. It is known that bodies, even than on a black body, and yet the solar rays comthe densest ones, are filled with a great number of municate less heat to the former because these

pores or small voids, whose volume can consider-rays, by being reflected, carry away their vis viva,

ably surpass that of the matter they contain; these which they communicate to the black body that

empty spaces allow their imperceptible parts the absorbs them.

freedom to oscillate in all directions, and it is We will not decide between the two preceding

natural to think that these parts are in continual hypotheses; several phenomena seem to favor the

agitation, which, if it increases to a certain point, latter; such is, for example, that of the heat procan disunite and decompose bodies; it is this induced by the friction of two solid bodies; but there

ternal motion which, according to the physicists are others that are more simply explained by the

we speak of, constitutes heat. former; perhaps both occur simultaneously. In

To develop this hypothesis, we shall observe that, any case, since one can only form these two hyin all movements where there is no abrupt change, potheses regarding the nature of heat, one must

there exists a general law which geometers have accept the principles common to both; thus, acdesignated under the name of the *principle of the* cording to both, *the quantity of free heat always*

*conservation of vis viva*; this law consists in that, *remains the same in the simple mixing of bodies*.

in a system of bodies acting upon each other in This is evident if heat is a fluid that tends to reach

any manner, the vis viva, that is to say, the sum equilibrium, and if it is merely the vis viva reof the products of each mass by the square of sulting from the internal motion of matter, the

its velocity, remains constant. If the bodies are principle in question follows from the principle

driven by accelerating forces, the vis viva is equal of the conservation of vis viva. The conservation

to what it was at the origin of the movement, plus

of free heat in the simple mixing of bodies is thus independent of any hypothesis regarding the nature of heat; it has been generally accepted by physicists, and we shall adopt it in the following research.”

At the time when this text was written, the atomic hypothesis remained largely speculative due to the lack of adequate experimental means: the experiment by Jean Perrin that finally settled the issue only took place in the early years of the 20th century, and the X-ray diffraction experiments suggested by Max von Laue occurred in 1912.

::::

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

## Problems

   :::{figure} ../images/art-p106-1.svg
   :alt: Illustration from the original text
   :::

   4.3 Energy and Temperature

   There is air in a flexible compartment at a pressure

   of $3bar (43.51psi)$. Its internal energy is $836kJkg^{-1}$.

   It is heated at constant pressure until $900^{\circ}C$; then it is

   cooled and expanded while its properties vary according to the relation $pv^{1.1}=$ const. until its temperature

   reaches $25^{\circ}C$.

   *[Trick question]* How much energy has it received or

   rejected since the beginning of the process?

   4.1 Air Pressure

   A mass of $5kg (11lb)$ of air is enclosed in a tank of $2m^{3}$

   $(528.3US gal)$.

   1. What are its specific volume and density?

   2. What is the pressure if the temperature is $20^{\circ}C$?

```{exercise}
:label: prob-4-2
:enumerator: 4.2

**Heating of an Air Tank A compressed air tank made out of sealed concrete has a fixed volume of $1.2 m^{3}$. Air is stored in it at a pressure of 2 bar. The tank is placed in the sun and solar heating raises the temperature from $5^{\circ}C$ to $60^{\circ}C (41 ^{\circ} F$ to $140 ^{\circ} F)$. 1. What are the mass, specific volume, density, and pressure inside the tank, before and after heating? When the temperature reaches $60^{\circ}C$, a valve opens and lets air escape to bring the pressure in the tank back down to the initial pressure of $2 bar (29 psi$. During the release, the temperature of the air inside the tank remains constant. 2. How much air mass should be allowed to escape? When the pressure has reached 2 bar, the valve closes and the tank, once again sealed, cools slowly at constant volume. The final temperature returns to $5^{\circ}C$. 3. What is the final pressure in the tank?**

:::{admonition} Answer
:class: dropdown

1) $m_{1}= \frac{p_{1}V_{1}}{RT_{1}} = 3.006 kg$; $v_{1}= 0.3991 m^{3}kg^{-1}$;
$\rho _{1}= 2.505 kg m^{-3}$; $p_{1}= 2 bar$;
$m_{2}= m_{1}; v_{1}= v_{2}; \rho _{1}= \rho _{2}; p_{2}= \frac{RT_{2}}{v_{2}} = 2.395bar.$
2) $m_{3}= 2.51 kg$, thus $m_{\mathrm{exhaust}}= m_{3}-m_{2}0.4959 kg$;
$3) p_{4}= \frac{RT_{4}m_{4}}{V_{4}} = 1.67bar.$

:::
```

```{exercise}
:enumerator: 4.4

**Power of an Air Pump An air pump (figure 4.15) compresses air adiabatically, with a steady flow. The air temperature increases from $15^{\circ}C$ to $100^{\circ}C$. What is the specific power input? portable air tank *Photo by Commons User:Grikalmis (retouched, public domain)***

:::{admonition} Answer
:class: dropdown

$w_{1\rightarrow 2}= \Delta h = c_{p}\Delta T = +85.4 kJ kg^{-1}$ (3/15 & 4/13)

:::
```

   :::{figure} ../images/fig-4-15.jpg
   :label: fig-4-15
   :enumerator: 4.15
   :alt: A small electric compressor mounted on a portable air tank
   
   A small electric compressor mounted on a portable air tank
   :::

```{exercise}
:label: prob-4-5
:enumerator: 4.5

**Turbine of a Turbojet Engine A student disassembles the *Turboméca Marboré* turbojet engine from a Fouga Magister in order to study and modify its operation. S/he operates the engine on a test bench. At the inlet of the turbine, the conditions are measured at $110 m s^{-1}(246 mph)$ and $1000^{\circ}C (1832 ^{\circ} F)$. At the outlet of the turbine, these properties are measured at $125 m s^{-1}(279.6 mph)$ and $650^{\circ}C (1202 ^{\circ} F)$. The student also measures the heat losses from the turbine as $75 kJ kg^{-1}$. 1. What is the specific power delivered by the turbine? 2. What condition must the student maintain to obtain a power of $1 MW$?**

:::{admonition} Answer
:class: dropdown

1) With equation 3/15, $w_{\mathrm{turbine}}= c_{p}(T_{\mathrm{B}}- T_{\mathrm{A}}) + \frac{1}{2^{2}})\dot{m} =\dot{}(C^{2}_{\mathrm{B}}- \frac{W_{\mathrm{turbine}}C^{2}_{\mathrm{A}}) -}{w_{\mathrm{turbine}}} = 3.64kgs^{-1}q_{\mathrm{A}\rightarrow \mathrm{B}}= -275kJkg^{-1}$

:::
```

```{exercise}
:label: prob-4-9
:enumerator: 4.9

**Elementary Processes: Vocabulary A fixed mass of perfect gas, with the sole purpose of exasperating a student in thermodynamics, slowly undergoes the following processes:**

:::{admonition} Answer
:class: dropdown

Isothermal $2 \rightarrow 3$, isochoric $1 \rightarrow 2$.

:::
```

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

Among the processes above, which ones are:

1. at constant temperature (isothermal)?

2. at constant volume (isochoric)?

```{exercise}
:label: prob-4-10
:enumerator: 4.10

**Elementary Processes: Pressure and Volume Among the reversible processes described on each of the diagrams in figure 4.16, identify (without having to justify) the process at constant temperature, at constant pressure, reversible adiabatic, and at constant volume. perfect gas *Diagram* CC-0 *Olivier Cleynen***

:::{admonition} Answer
:class: dropdown

10**
*Clockwise, starting horizontally, on both diagrams:*
isobaric $(p$ constant), isothermal $(T$ constant),
reversible adiabatic, isochoric $(v$ constant).

:::
```

   :::{figure} ../images/fig-4-16.svg
   :label: fig-4-16
   :enumerator: 4.16
   :alt: Elementary processes undergone by a perfect gas
   
   Elementary processes undergone by a perfect gas
   :::

```{exercise}
:label: prob-4-11
:enumerator: 4.11

**Compressor of a Turbofan Inside one of the engines of a commercial aircraft, the compressor (figure 4.17) is almost adiabatic. During cruise at $33 000 ft$, the atmosphere is at $-50^{\circ}C (-58 ^{\circ} F)$ and $0.25 bar (3.626 psi)$. The fan is driven by the turbine through a mechanical shaft. It receives $55 kg s^{-1}$ of air at atmospheric conditions, and compresses this flow up until $8 bar (116 psi)$. 1. Starting from the following relation, $p_{1}v_{2}^{\gamma}$ (4/38) $(p_{2}) = (v_{1})$ *Photo* CC-by-sa *Olivier Cleynen* valid for a reversible adiabatic process undergone by a perfect gas, show (without using equation 4/36) that: $\frac{\gamma -1}{\gamma} \frac{T_{1}}{} \frac{p_{1}}{} (T_{2}) = (p_{2})$ (4/37) 2. What is the minimum theoretical power to be supplied to the compressor? 3. Under what conditions would this power be obtained? In reality, the compressor requires significantly more power to operate. We model the actual process inside the compressor with two distinct phases: • A heating at constant pressure, conducted by friction, with power representing $15 \%$ of the theoretical power calculated earlier; • Then, an ideal compression up to 8 bar. 4. Compare the theoretical compression from question 2 and this new process on a pressure-volume diagram. Graphically represent the work done on one of the processes. 5. What is the power supplied to the compressor in this new scenario? under license by Sulzer in Switzerland *Photo* CC-by-sa *Sulzer AG***

:::{admonition} Answer
:class: dropdown

11**
1) Replace $v_{2}$ with $\frac{RT_{2}}{p_{2}}$, do the same with $v_{1}$. Work
out the algebra and the result will come naturally;
2) With eq. 4/37, we obtain $T_{\mathrm{B}}= 600.7 K$, thus
$W_{\mathrm{A}\rightarrow \mathrm{B}}= +20.87 MW$;
3) see §4.4.5 p. 100;
5) $T_{\mathrm{C}}= 279.8 K$; $T_{\mathrm{D}}= 753.1 K$; thus
$W_{\mathrm{real} \mathrm{compressor}}=\dot{W}_{\mathrm{friction} \mathrm{losses} \mathrm{A}\rightarrow \mathrm{C}}+\dot{W}_{\mathrm{C}\rightarrow \mathrm{D}}= +29.29 MW (+40 \%)$.

:::
```

   :::{figure} ../images/fig-4-17.jpg
   :label: fig-4-17
   :enumerator: 4.17
   :alt: Air intake of one of the four General Electric GEnx-2B turbofans equipping a Boeing 747-8. The two-color fan blades are visible in the foreg
   
   Air intake of one of the four General Electric GEnx-2B turbofans equipping a Boeing 747-8. The two-color fan blades are visible in the foreground; behind, the air flow is divided between the compressor inlet (internal) and the cold flow rectifier stators (external).
   :::

   :::{figure} ../images/fig-4-18.jpg
   :label: fig-4-18
   :enumerator: 4.18
   :alt: Diesel Engine from 1898, manufactured under license by Sulzer in Switzerland
   
   Diesel Engine from 1898, manufactured under license by Sulzer in Switzerland
   :::

```{exercise}
:label: prob-4-12
:enumerator: 4.12

**Compression and Combustion in a Diesel Engine In 1890, a young German engineer with a passion for thermodynamics (§7.6) developed a low-power, low-speed, and high-efficiency engine in a laboratory (figure 4.18). The engine was designed to be robust and simple; it had only one cylinder. Here, we study part of its operating cycle. The piston inside the cylinder periodically varies the volume between $3 L$ (*bottom dead center*, piston at the bottom of its stroke) and $0.3 L$ (*top dead center*, piston at the top of its stroke). The engine starts its cycle at bottom dead center, when it is filled with air at $20^{\circ}C$ and $1 bar (68 ^{\circ} F$ and $14.5 psi)$. The piston compresses this air to top dead center. The compression is done reversibly (very slowly), but non-adiabatically: the air receives heat through the walls throughout the process. The engineer predicted that its properties would vary according to the relation $p v^{1.5}=$ constant. 1. The work done by a force$\vec{F}$ along a displacement $l$ is expressed as $W \equiv \vec{F} ⋅\vec{l}$ (1/11) Starting from this equation, express the work done on a fixed mass body in terms of its specific volume and internal pressure. 2. How much energy in the form of work will the gas compression have cost? 3. How much energy in the form of heat will the gas have received during compression? When the piston reaches the top of its stroke, fuel is progressively injected into the cylinder to allow for combustion to occur. The amount of injected fuel provides for a total heat input of $2 kJ$. The combustion takes place at constant pressure. 4. Draw the processes undergone by the gas during compression and combustion on a pressure-volume diagram, qualitatively (that is, without showing numerical values). 5. What will be the maximum temperature reached within the engine? 6. In order to avoid structural failure, the engineer must ensure that the force transmitted by the piston never exceeds $10 kN (2248 lbf)$. What constraint must be respected for this?**

:::{admonition} Answer
:class: dropdown

12**
1) see §1.3 p. 16 & §2.4.1 p. 36;
2) $W_{\mathrm{A}\rightarrow \mathrm{B}}= -m\int ^{\mathrm{B}}_{\mathrm{A}}pdv = +1.298 kJ$
3) Wth $p_{\mathrm{B}}= kv^{-1.5}= 31.6 bar$, we have $T_{\mathrm{B}}=$ B
$926.3 K$. Then, $Q_{\mathrm{A}\rightarrow \mathrm{B}}= \Delta U -W_{\mathrm{A}\rightarrow \mathrm{B}}= +0.3254 kJ$.
5) With constant pressure, with equation 4/17,
$T6)^{\mathrm{C}}S= <^{\frac{Q_{\mathrm{B}\rightarrow \mathrm{C}}}{F_{\mathrm{ma}}m c_{p}}} _{p_{\mathrm{C}}^{\mathrm{x}}}+_{.}=T _{\mathrm{B}}3 =.1 6144 8\times 3 1.70 K_{-3}(m12_{2}1 (1\mathrm{d}^{\circ}$i$C$am).eter $D_{\max}= 6.35 cm)$.

:::
```

```{exercise}
:label: prob-4-13
:enumerator: 4.13

**Turbojet Engine An early 1960s military aircraft is equipped with a turbojet engine (figure 4.19). We wish to calculate the theoretical maximum speed at which it could accelerate the air at the nozzle outlet. The engine is tested on a stationary test bench. When air passes through the turbojet engine, it goes through four components that we will model as if they were ideal: **The compressor** (figure 4.20) compresses the air adiabatically and reversibly. At the inlet, the air is at 0.9 bar and $5^{\circ}C$; at the outlet, the pressure is increased to 19 bar. **The combustion chamber** allows for the heating of air while maintaining its pressure constant. At the outlet of the combustion chamber, the temperature has been increased to $1100^{\circ}C$. **The turbine** extracts energy from the air to power the compressor. In the turbine, the air expands adiabatically and reversibly. **The nozzle** is a component in which no power is added or extracted from the air. As it flows across the nozzle, the air expands adiabatically *Diagram* CC-by-sa *Olivier Cleynen***

:::{admonition} Answer
:class: dropdown

2) With equation 4/37, $T_{\mathrm{B}}= 664.83 K$ 3) With equation 3/15, $w_{\mathrm{compressor}}= w_{\mathrm{A}\rightarrow \mathrm{B}}= +388.61 kJ kg^{-1}$ 4) $T_{\mathrm{C}}= 1373.15 K$; thus $q_{\mathrm{combustion}}= q_{\mathrm{B}\rightarrow \mathrm{C}}= +711.86 kJ kg^{-1}$ 5) Since $w_{\mathrm{turbine}}= -w_{\mathrm{compressor}}$, we have $T_{D}= 986.47 K$ 6) With equation 4/37, $p_{\mathrm{D}}= 5.97 bar$ 7) Idem, with equation 4/37, $T_{\mathrm{E}}= 574.49 K$ 8) With equation 3/15, $C_{\mathrm{E}}= (-2\Delta h)^{\frac{1}{2}} = 909.98 m s^{-1}$ Of course, these values do not account for the irreversibilities in an actual turbojet. These effects are approached in problem 4.11 p. 108 and formalized in chapter 10 (*air-based power cycles*).
*Engineering Thermodynamics* by Olivier Cleynen

:::
```

   :::{figure} ../images/fig-4-19.svg
   :label: fig-4-19
   :enumerator: 4.19
   :alt: Schematic of a turbojet engine. Air flows through the machine from left to right.
   
   Schematic of a turbojet engine. Air flows through the machine from left to right.
   :::

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

and reversibly; its speed increases significantly. At the outlet of the nozzle, it has returned to atmospheric pressure and is expelled into the atmosphere.

The goal of the problem is to calculate the speed at which the turbojet engine is capable of releasing the air.

1. Starting from the following relation,

$T_{1}v_{2}^{\gamma -1}$ (4/36)

$(T_{2}) = (v_{1})$

valid for a reversible adiabatic process undergone by a perfect gas, show (without using equation 4/38) that:

$\frac{\gamma -1}{\gamma}$

$T_{1}p_{1}$ (4/37)

$(T_{2}) = (p_{2})$

2. What is the air temperature at the compressor outlet?

3. What is the specific power supplied to the compressor?

4. What is the specific power supplied in the form of heat in the combustion chamber?

5. What must be the temperature at the turbine outlet for it to power the compressor?

6. What will then be the pressure at the turbine outlet?

7. What will be the exhaust gas temperature at the nozzle outlet?

8. Finally, what will be the gas ejection speed at the nozzle outlet?

9. Draw the complete series of processes on a pressure-volume diagram, qualitatively.

10. On the same pressure-volume diagram, plot the processes that the gas would follow if the compressor could not compress the air reversibly (real compressor, compression with internal friction).

   :::{figure} ../images/fig-4-20.jpg
   :label: fig-4-20
   :enumerator: 4.20
   :alt: Compressor of a dissected snecma Atar turbojet engine (1948). Air flows from the left to the center of the image.
   
   Compressor of a dissected snecma Atar turbojet engine (1948). Air flows from the left to the center of the image.
   :::

turbojet engine (1948). Air flows from the left to the center of the image.

*Photo* CC-by-sa *Olivier Cleynen*
