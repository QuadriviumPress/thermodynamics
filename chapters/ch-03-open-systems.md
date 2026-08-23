---
title: "3. Open Systems"
short_title: "Chapter 3"
label: ch-03-open-systems
---

:::{figure} ../images/art-p078-1.svg
:alt: Chapter opening illustration
:::

# 3. Open Systems

(ch-3)=

Open Systems

*Measuring the Intangible in the Ungraspable*

:::{figure} ../images/art-p059-1.svg
:alt: Illustration from the original text
:::

:::{admonition} Executive summary
:class: tip
An open system is crossed by a mass flow. Heat and work transfers cause variations in the enthalpy of the fluid. For work to be reversible, the movement must be infinitely slow.
:::

## Introduction

In the previous chapter, we quantified energy exchanges within closed

systems. This chapter 3 (*open systems*) aims to answer a similar question:

how to quantify energy transfers within a system when it is crossed by a

mass flow?

(sec-3-1)=
## 3.1 Why Use an Open System?

In many machines, the fluid used to transfer heat and work is continuously

circulating. It can then be difficult to identify a particular amount of mass,

making it a closed system, in order to quantify energy transfers to and

from it. For example, in a jet engine nozzle, air expands and accelerates

continuously: at any given moment, there is no identifiable volume that

would have *one* specific speed or *one* particular pressure.

Using an open system is very useful to account for energy in flows. Rather

than separating stages in time (for example before and after compression),

we quantify work and heat transfers by separating stages in space (for

example upstream and downstream of the compressor).

(sec-3-2)=
## 3.2 Accounting Conventions

(sec-3-2-1)=
### 3.2.1 The open system

We call an *open system* an arbitrary subject of study whose boundaries are permeable to mass (figure 3.3). In general, its volume can change, and it can have multiple inlets and outlets, each with a different flow rate and pressure.

:::{figure} ../images/fig-3-1.jpg
:label: fig-3-1
:enumerator: 3.1
:alt: Sign conventions for an open system. Inflows are positive, outflows are negative; they are all represented with inward arrows.

Sign conventions for an open system. Inflows are positive, outflows are negative; they are all represented with inward arrows.
:::

In our study of thermodynamics, we will only use open systems:

• with fixed volume;

• having only one inlet and one outlet;

« The constructive difficulties that have to be overcome in a large gas motor because of the immense piston pressures and heat expansion of the complicated cylinder heads (cracks galore!) are well known. A safe gas turbine would in this respect be an improvement. »

Aurel Stodola, 1904

*Die Dampfturbinen* [[26](#ref-26), [27](#ref-27)]

*Diagram* CC-0 *Olivier Cleynen*

• being crossed by a constant mass flow rate$\dot{m}$ (positive by convention).

These systems are said to be in *steady state* (sometimes called *steady flow* or *stationary flow* regime).

(sec-3-2-2)=
### 3.2.2 Sign conventions

Just like for closed systems, we will take the open system’s point of view to quantify transfers:

• Receiving work, heat, or mass results in a *positive* transfer;

• Expending work, heat, or mass results in a *negative* transfer.

Thus, we add up all transfers as on a bank statement.

(sec-3-3)=
## 3.3 The First Law in an Open System

We have seen that in a closed system, the law of conservation of energy is expressed by the equation $q+w = \Delta u$ (2/2). In an open system, the situation is a little different and we must consider additional forms of energy.

(sec-3-3-1)=
### 3.3.1 Entering and exiting the system: flow work

Let’s imagine an open system in steady flow, containing a small water pump. In order to insert water into the pump at a given pressure, energy must be supplied to the system. Conversely, to push the water outside (at a higher pressure), the system must supply energy. How can we quantify this energy?

Consider the case of a *fluid element* (namely, a small quantity of fluid in transit, with volume $V_{\mathrm{element}})$ entering our system at pressure $p_{1}$ (figure 3.2).

The work $W_{\mathrm{insertion}}$ received by the system when the element is pushed

through the insertion is:

:::{math}
:label: eq-3-1
:enumerator: 3/1
W_{\mathrm{insertion}}= p_{1}V_{\mathrm{element}}
:::

where $W_{\mathrm{insertion}}$ is the insertion work $(J)$, and $V_{\mathrm{element}}$ is the volume of the fluid element $(m^{3})$.

If such a volume of fluid enters the system every second, then the system

receives power in the form of work, which we call *insertion power*,$\dot{W}_{\mathrm{insertion}}$.

:::{figure} ../images/fig-3-2.jpg
:label: fig-3-2
:enumerator: 3.2
:alt: A fluid element of volume entering at pressure into the open system.

A fluid element of volume $V_{\mathrm{element}}$ entering at pressure $p$ into the open system.
:::

*Diagram* CC-0 *Olivier Cleynen*

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

We sometimes express it in specific form (§1.1.5):

:::{math}
W_{\mathrm{insertion}}= p_{1}\dot{V}_{1}=\dot{m}_{1}p_{1}v_{1}=\dot{m} p_{1}v_{1} (3/2)
:::

:::{math}
w_{\mathrm{insertion}}= p_{1}v_{1} (3/3)
:::

where$\dot{W}_{\mathrm{insertion}}$ is the insertion power $(W)$,

:::{math}
w_{\mathrm{insertion}} is the specific insertion power (J kg^{-1}) ,
:::

:::{math}
m_{1} is the net mass flow rate at 1 (kg s^{-1}) ,
:::

$m$ is the mass flow rate crossing the system (always positive, $kg s^{-1})$, $V_{1}$ is the volumetric flow rate of fluid $(m^{3}s^{-1})$,

and $v_{1}$ is the specific volume of the fluid at the inlet $(m^{3}kg^{-1})$.

Similarly, for the fluid to exit the system at the other end, the system must

continuously supply a power called *extraction power*:

:::{math}
W_{\mathrm{extraction}}= -p_{2}\dot{V}_{2}=\dot{m}_{2}p_{2}v_{2}= -\dot{m} p_{2}v_{2} (3/4)
:::

:::{math}
w_{\mathrm{extraction}}= -p_{2}v_{2} (3/5)
:::

where the outgoing mass flow rate$\dot{m}_{2}$ (negative) is expressed in terms of the mass flow rate$\dot{m}$ crossing the system (always positive, $kg s^{-1})$.

The net sum of these two powers at the boundaries is called *flow power*, $W_{\mathrm{flow}}\equiv \dot{W}_{\mathrm{insertion}}+\dot{W}_{\mathrm{extraction}}$. Its sign depends on the operating conditions – the student is encouraged to visualize and formulate the conditions under which the flow power can be negative, zero, or positive.

(sec-3-3-2)=
### 3.3.2 Energy balance

Let us try to design an open system in steady flow in the most general way possible, as represented in figure 3.3. We will now account for all energy transfers within it.

When entering the system, the fluid already has an internal energy $u_{1}$; therefore, the system sees its own internal energy increase with power$\dot{U}_{1}$:

:::{math}
:label: eq-3-6
:enumerator: 3/6
\dot{U}_{1}=\dot{m} u_{1}
:::

Similarly, the fluid has a specific mechanical energy $e_{\mathrm{mech}1}$ (equation 1/9), and the system also receives power $\dot{E}_{\mathrm{mech}1}$:

:::{math}
:label: eq-3-7
:enumerator: 3/7
\dot{E}_{\mathrm{mech}1}=\dot{m} e_{\mathrm{mech}1}=\dot{m} \bigl(\tfrac{1}{2} C_{1}^{2}+ g z_{1}\bigr)
:::

These expressions 3/6 and 3/7 have the opposite sign at the system’s outlet, where we assign them the index 2.

At this point, we have covered all of the energy forms that can be observed crossing the boundaries of an open system together with the fluid: flow work, internal energy, and mechanical energy. Since the first law states that energy is indestructible (§1.1.2), the addition of power $\dot{Q}$ in the form of heat or $\dot{W}$ in the form of work can only vary these three forms. This results in the equation:

:::{math}
:label: eq-3-8
:enumerator: 3/8
\dot{Q}_{1\rightarrow 2}+\dot{W}_{1\rightarrow 2}+ (\dot{W}_{\mathrm{insertion}}+\dot{U}_{1}+\dot{E}_{\mathrm{mech}1}) + (\dot{W}_{\mathrm{extraction}}+\dot{U}_{2}+\dot{E}_{\mathrm{mech}2}) = 0
:::

where all terms are expressed in watts.

:::{figure} ../images/fig-3-3.jpg
:label: fig-3-3
:enumerator: 3.3
:alt: An arbitrary open system. The system (whose boundaries are dashed lines, in red) is crossed from left to right by the fluid flowing with a constant mass flow rate $\dot{m}$. It receives power $\dot{W}_{1\rightarrow 2}$ in the form of work and power $\dot{Q}_{1\rightarrow 2}$ in the form of heat.

An arbitrary open system. The system (whose boundaries are dashed lines, in red) is crossed from left to right by the fluid flowing with a constant mass flow rate $\dot{m}$. It receives power $\dot{W}_{1\rightarrow 2}$ in the form of work and power $\dot{Q}_{1\rightarrow 2}$ in the form of heat.
:::

*Diagram* CC-0 *Olivier Cleynen*

We can re-express equation 3/8 in terms of directly measurable quantities:

:::{math}
:label: eq-3-9
:enumerator: 3/9
\dot{Q}_{1\rightarrow 2}+\dot{W}_{1\rightarrow 2}+\dot{m} \bigl(p_{1}v_{1}+ u_{1}+ \tfrac{1}{2} C_{1}^{2}+ g z_{1}\bigr) =\dot{m} \bigl(p_{2}v_{2}+ u_{2}+ \tfrac{1}{2} C_{2}^{2}+ g z_{2}\bigr)
:::

or:

:::{math}
:label: eq-3-10
:enumerator: 3/10
\dot{Q}_{1\rightarrow 2}+\dot{W}_{1\rightarrow 2}=\dot{m}\bigl[\Delta u + \Delta (pv) + \tfrac{1}{2}\Delta (C^{2}) + g \Delta z\bigr]
:::

:::{math}
:label: eq-3-11
:enumerator: 3/11
q_{1\rightarrow 2}+ w_{1\rightarrow 2}= \Delta u + \Delta (pv) + \Delta e_{\mathrm{mech}.}
:::

where the symbols $\Delta$ indicate the change of properties between points 1 and 2 within the system.

Equations 3/9 and 3/11 are extremely useful in thermodynamics, because they allow us to quantify by deduction the powers involved in flows. They allow us, in particular, to predict the properties of the fluid at the outlet of a device for which we know the mechanical power and heat emissions. For example, we can determine the remaining energy in the air at the outlet of a turbine for which we know the power.

````{prf:example}
:label: ex-3-1
:enumerator: 3.1

The compressor of a turbofan admits $1.5 kg s^{-1}$ of air at a pressure of 0.8 bar, internal energy of $192.5 kJ kg^{-1}$, and specific volume of $0.96 m^{3}kg^{-1}$. It compresses the air to 30 bar, releasing it with an internal energy of $643.1 kJ kg^{-1}$ and a specific volume of $8.57 \times 10^{-2}m^{3}kg^{-1}$. The velocity and altitude of the air remain unchanged.

What is the power of the compressor if its heat transfers are negligible?

We apply equation 3/10 to obtain: $W_{1\rightarrow 2}= -\dot{Q}_{1\rightarrow 2}+\dot{m}[\Delta u + \Delta (pv) + \frac{1}{2}\Delta (C^{2}) + g \Delta z] = 0 +\dot{m}[\Delta u + \Delta (pv) + 0 + 0] = 1.5 [(643.1 \times 10^{3}- 192.5 \times 10^{3}) + (30 \times 10^{5}\times 8.57 \times 10^{-2}- 0.8 \times 10^{5}\times 0.96)]$

$= +9.464 \times 10^{5}W = +946.4 kW$.

The only difficulty in applying this equation concerns the proper

conversion of units. Pressure and energy should always be converted from their usual units to si units.

The power is positive, as expected since the air *receives* the work.

In a turbine, the work would be negative.

````

(sec-3-3-3)=
### 3.3.3 Enthalpy

In many cases, the terms $u$ and $pv$ vary in the same manner together with the state of the fluid (in fact, we will even see in the next chapter that in the case of an ideal gas, they are both proportional to the temperature). In order to simplify their use in calculations, they are often combined into a single term.

We call the sum of the terms $u$ and $pv$ the *specific enthalpy*, and assign it the symbol $h$:

:::{math}
h \equiv u + p v
:::

where the terms are expressed in $J kg^{-1}$.

Of course, the *enthalpy* $H$ is simply defined as:

:::{math}
H \equiv m h
:::

where $H$ is measured in joules (J).

In practice, the term *enthalpy* is often used even if it refers to specific enthalpy; the symbol and context help determine which variable is being referred to.

By using the concept of enthalpy, equations 3/9 and 3/11 are simplified to

become:

:::{math}
Q_{1\rightarrow 2}+\dot{W}_{1\rightarrow 2}=\dot{m}(\Delta h + \Delta e_{\mathrm{mech}.})
:::

:::{math}
q_{1\rightarrow 2}+ w_{1\rightarrow 2}= \Delta h + \Delta e_{\mathrm{mech}.}
:::

(3/12)

(3/13)

« The decrease of the heat contents is equal to the heat value of the gained “useful work” plus the heat carried away to the outside plus the increase of kinetic energy per pound (or kilogram) of steam. »

Aurel Stodola, 1904

(where the “heat contents” are not yet named *enthalpy*)

*Die Dampfturbinen* [[26](#ref-26), [27](#ref-27)]

(3/14)

(3/15)

Thus, in an open system, we see that heat and work transfers change the *enthalpy* of the fluid, and not only its internal energy as in a closed system.

````{prf:example}
:label: ex-3-2
:enumerator: 3.2

In a nozzle, air expands without any work or heat transfer. It enters with a specific enthalpy of $776 kJ kg^{-1}$ and a velocity of $30 km/h (18.6 mph)$ and exits at the same altitude, with an enthalpy of $754 kJ kg^{-1}$.

What is the air ejection velocity?

We start from equation 3/15:

:::{math}
q_{1\rightarrow 2}+ w_{1\rightarrow 2}= \Delta h + \Delta e_{\mathrm{mech}.}
:::

:::{math}
\Delta e_{\mathrm{mech}.}= -\Delta h + 0 + 0
:::

:::{math}
1
:::

:::{math}
_{2}- C^{2}_{1}) = -\Delta h
:::

:::{math}
2 (C^{2}
:::

:::{math}
\frac{1}{}
:::

:::{math}
C_{2}= [-2 \Delta h + C^{2}_{1}]^{2}
:::

:::{math}
\frac{1}{}
:::

:::{math}
2 \frac{}{2}
:::

So $C_{2}= [-2 \times (754 \times 10^{3}- 776 \times 10^{3}) + ( \frac{30}{3.6})] = 209.9 m s^{-1}= 755.7 km/h = 470 mph$.

Care must be used with conversions: in the equations, velocities

and energies are always in si units.

````

(sec-3-4)=
## 3.4 Quantifying Work with an Open System

## System

(sec-3-4-1)=
### 3.4.1 Work of a fluid in a slow process

We have seen that when the fluid undergoes a slow process, the work done by a closed system can be quantified by carrying out the integral $-\int pdv$ (2/15). With an open system, the expression is slightly different. In order to develop it, we propose to study the steady compression of a fluid passing through a compressor.

To this end, let us first observe the process undergone by a fixed mass quantity $m_{A}$ circulating in the compressor (figure 3.4). As it passes between the moving blades, its pressure varies by $dp$ and its volume by $dv$. This is simply a moving closed system: since the process is very slow (reversible), the work δ$w_{m_{\mathrm{A}}}$ received by the system will be:

:::{math}
:label: eq-3-16
:enumerator: 3/16
δ w_{m_{\mathrm{A}}}= -pdv
:::

during a reversible process, and where the notation δ is used to denote the infinitesimal transfer of work (work being a path quantity, see Appendix A4 p. 316).

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

:::{figure} ../images/fig-3-4.jpg
:label: fig-3-4
:enumerator: 3.4
:alt: A fixed mass quantity 𝑚𝐴flows from left to right through a compressor. It is compressed: its properties change from 𝑝and 𝑣to 𝑝+ d𝑝and 𝑣+ d𝑣. If we consider the point of view of a closed system in transit, the work transfer is δ𝑤𝑚A = −𝑝d𝑣.

A fixed mass quantity $m_{A}$ flows from left to right through a compressor. It is compressed: its properties change from $p$ and $v$ to $p + dp$ and $v + dv$. If we consider the point of view of a closed system in transit, the work transfer is δ$w_{m_{\mathrm{A}}}= -pdv$.
:::

Now, let’s observe the course of this *same* phenomenon from the point of view of an open system (figure 3.5). What specific power δ$w_{\mathrm{O.S}.}$ must be supplied to the compressor so that each fluid particle receives work δ$w_{m_{\mathrm{A}}}$?

:::{figure} ../images/fig-3-5.jpg
:label: fig-3-5
:enumerator: 3.5
:alt: The same flow as in figure 3.4, now observed from the viewpoint of a stationary open system crossed from left to right by a steady flow. We seek to quantify the work δ$w_{\mathrm{O.S}.}$ to be supplied to the system so that each mass quantity $m_{\mathrm{A}}$ receives work δ$w_{m_{\mathrm{A}}}$.

The same flow as in figure 3.4, now observed from the viewpoint of a stationary open system crossed from left to right by a steady flow. We seek to quantify the work δ$w_{\mathrm{O.S}.}$ to be supplied to the system so that each mass quantity $m_{\mathrm{A}}$ receives work δ$w_{m_{\mathrm{A}}}$.
:::

The open system has four work transfer forms:

**The specific insertion power** $w_{\mathrm{insertion}}$ (3/3) is due to the permanent arrival of the fluid at the system’s inlet. From the viewpoint of the open system, we have:

:::{math}
w_{\mathrm{insertion}}= +p v
:::

**The specific compression power** $-$δ$w_{m_{\mathrm{A}}}$ is the specific work that the open system must transfer to each mass quantity $m_{A}$ to effectively compress it:

:::{math}
- δ w_{m_{\mathrm{A}}}= -(-pdv)
:::

*Diagram* CC-0 *Olivier Cleynen*

*Diagram* CC-0 *Olivier Cleynen*

(3/17)

(3/18)

continuously remove the fluid.

to the compressor:

reversible.

flow, we obtain:

in steady flow, when the process is reversible, and regardless of the heat input.

figure 3.6.

**The specific extraction power** $w_{\mathrm{extraction}}$ is spent by the open system to

At the outlet, the fluid properties have become $p + dp$ for pressure,

and $v + dv$ for volume. Thus, we have:

$w_{\mathrm{extraction}}= -(p + dp)(v + dv)$ (3/19)

**The specific power received from the outside** δ$w_{\mathrm{O.S}.}$ is the power that

feeds the compression: this is the quantity we aim to quantify.

These four powers cancel each other out, since the total work transfer

involved in the flow does not depend on the adopted viewpoint:

δ$w_{\mathrm{O.S}.}+ w_{\mathrm{insertion}}+ (-$δ$w_{m_{\mathrm{A}}}) + w_{\mathrm{extraction}}= 0$ (3/20)

Therefore, we can quantify the specific power δ$w_{\mathrm{O.S}.}$ that must be supplied

δ$w_{\mathrm{O.S}.}= -w_{\mathrm{insertion}}+$ δ$w_{m_{\mathrm{A}}}- w_{\mathrm{extraction}}$

δ$w_{\mathrm{O.S}.}= -p v + (-pdv) + (p + dp)(v + dv)$

$= -p v - pdv + p v + pdv + dp v + dp dv$

$= dp v + dp dv$

And since the product $dp \times dv$ tends to zero when using infinitesimal

quantities, we obtain the surprising expression:

δ$w_{\mathrm{O.S}.}= vdp$ (3/21)

The terms $dp$ and $dv$ in our study are not necessarily positive: this expression applies equally to expansions and compressions, as long as they are

By integrating this expression 3/21 to apply it to the general case in steady

$w_{\mathrm{O.S}.}= \int vdp$ (3/22)

B

$W_{\mathrm{A}\rightarrow \mathrm{B}}=\dot{m}\int vdp$ (3/23) A

Thus, when we want to quantify reversible work in an open system, it is the

integral $+ \int vdp$ that needs to be calculated, and not $-\int pdv$.

On a pressure-volume diagram, we can visualize this work by adding the

insertion work and extraction work to the compression work, as shown in

The reversible work done in steady, reversible flow is thus visualized by the

area enclosed *to the left* of the curve, as shown in figure 3.7.

*Engineering Thermodynamics* by Olivier Cleynen

:::{figure} ../images/fig-3-6.jpg
:label: fig-3-6
:enumerator: 3.6
:alt: Work received by an open system crossed by a fluid, during a slow process. The system first receives the insertion work $(p_{\mathrm{ini}.}v_{\mathrm{ini}.}$, in orange, positive) to enter the system, then it spends compression work (hatched area, negative), and finally, it spends extraction work $(p_{\mathrm{fin}.}v_{\mathrm{fin}.}$, in blue, negative). The net sum of these three areas is the specific power to be supplied to the open system.

Work received by an open system crossed by a fluid, during a slow process. The system first receives the insertion work $(p_{\mathrm{ini}.}v_{\mathrm{ini}.}$, in orange, positive) to enter the system, then it spends compression work (hatched area, negative), and finally, it spends extraction work $(p_{\mathrm{fin}.}v_{\mathrm{fin}.}$, in blue, negative). The net sum of these three areas is the specific power to be supplied to the open system.
:::

:::{figure} ../images/fig-3-7.jpg
:label: fig-3-7
:enumerator: 3.7
:alt: Work measured in an open system, during a reversible process. The integral of $vdp$ is visualized by the area to the left of the curve. If the fluid returns to its initial state (having completed a *thermodynamic cycle*), the work done is visualized by the area enclosed within the curve. In this case, the quantification is the same for closed and open systems.

Work measured in an open system, during a reversible process. The integral of $vdp$ is visualized by the area to the left of the curve. If the fluid returns to its initial state (having completed a *thermodynamic cycle*), the work done is visualized by the area enclosed within the curve. In this case, the quantification is the same for closed and open systems.
:::

*Diagram* CC-0 *Olivier Cleynen*

*Diagram* CC-0 *Olivier Cleynen*

````{prf:example}
:label: ex-3-3
:enumerator: 3.3

A pump slowly compresses $2 kg s^{-1}(4.41 lb/s)$ of water from $1$ to 20 bar (from $14.5$ to $290 psi)$. During compression, the specific volume of water remains constant at $v_{L}= 10^{-3}m^{3}kg^{-1}$. What is the power required in the form of work?

The process can be drawn qualitatively (that is, without showing numerical values) on a pressure-volume diagram as follows:

````

:::{figure} ../images/art-p069-1.jpg
:alt: Illustration from the original text
:::

````{prf:example}

We use equation 3/23, being cautious with the units. Since $v$ is independent of $p$, integration is straightforward:$\dot{W}_{\mathrm{A}\rightarrow \mathrm{B}}=\dot{m}\int ^{\mathrm{B}}_{\mathrm{A}}vdp =\dot{} m v_{L}\int ^{\mathrm{B}}_{\mathrm{A}}dp =\dot{m} v_{L}[p]^{p_{\mathrm{B}}}_{p_{\mathrm{A}}}= 2 \times 10^{-3}(20 \times 10^{5}- 1 \times 10^{5}) = +3.8 \times 10^{3}W = +3.8 kW$.

This power is indeed positive, since the fluid in the system is

receiving the work.

Here the specific volume $v_{L}$ is constant (as always with liquid

water). If it were the pressure that was constant, then the work would be zero even if $v$ were to vary.

````

````{prf:example}
:label: ex-3-4
:enumerator: 3.4

A compressor slowly compresses an air flow of $2 kg s^{-1}$ from 1 bar to 20 bar. During compression, the specific volume and pressure of the air are related by the expression $p v^{1.35}= k$. At the inlet, the specific volume of the air is $v_{\mathrm{A}}= 0.8 m^{3}kg^{-1}$. What is the power required in the form of work?

The process can be drawn qualitatively on a pressure-volume diagram as follows:

````

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

````{prf:example}

Here the specific volume is a function of pressure: we have $v = \left(\frac{k}{p}\right)^{\frac{1}{1.35}}= k^{\frac{1}{1.35}} p^{-\frac{1}{1.35}}$. We start from equation 3/23:

:::{math}
\dot{W}_{\mathrm{A}\rightarrow \mathrm{B}}=\dot{m}\int _{\mathrm{A}}^{\mathrm{B}}v\,\mathrm{d}p =\dot{m}\, k^{\frac{1}{1.35}} \int _{\mathrm{A}}^{\mathrm{B}}p^{-\frac{1}{1.35}}\,\mathrm{d}p =\dot{m}\, k^{\frac{1}{1.35}} \left[\frac{1}{-\frac{1}{1.35}+1}\,p^{-\frac{1}{1.35}+1}\right]_{p_{\mathrm{A}}}^{p_{\mathrm{B}}}
= \dot{m}\,(p_{\mathrm{A}} v_{\mathrm{A}}^{1.35})^{\frac{1}{1.35}}\frac{1}{0.25926}\left[p^{0.25926}\right]_{p_{\mathrm{A}}}^{p_{\mathrm{B}}}
= 2\,(1\times 10^{5}\times 0.8^{1.35})^{\frac{1}{1.35}}\frac{1}{0.25926}\left[(20\times 10^{5})^{0.25926}-(1\times 10^{5})^{0.25926}\right]
= +7.247 \times 10^{5}\,\mathrm{W} = +724.7\,\mathrm{kW}.
:::

Here the key is to correctly describe the function $v_{(p)}$ before

proceeding with the integration.

The power of the compressor is $190$ times larger than that

of the pump in the previous example. Additionally, the specific volume of the air at the inlet is $800$ times larger: a much larger machine will be required (it must handle a volumetric flow rate $V_{\mathrm{A}}=\dot{m} v_{\mathrm{A}}= 1.6 m^{3}s^{-1}= 1600 L s^{-1}= 423 US gal/s$ at the inlet).

````

(sec-3-4-2)=
### 3.4.2 Work of a fluid in a fast process

When the process is carried out rapidly (as is always the case in practice), we encounter the phenomena described in the previous chapter (§2.4.3): the pressure exerted on the moving walls no longer corresponds to the “average” pressure inside the fluid. The work required in compressions is greater and the work received during expansions is less than during slow processes.

Using an open system to account for energy transfers does not change the problem, of course. We do not have the means to predict analytically the work required for compression at a given speed. The problem –calculating the spatial distribution of pressure inside the fluid over time– falls within the scope of fluid mechanics, and will be solved on a case-by-case basis.

:::{figure} ../images/fig-3-8.jpg
:label: fig-3-8
:enumerator: 3.8
:alt: Reversible (solid line) and irreversible (dashed line) compressions represented on a pressure-volume diagram. In an open system, work transfers can be visualized with the area to the left of the curve, but only when the processes are reversible.

Reversible (solid line) and irreversible (dashed line) compressions represented on a pressure-volume diagram. In an open system, work transfers can be visualized with the area to the left of the curve, but only when the processes are
:::

*Diagram* CC-0 *Olivier Cleynen*

reversible.

On our pressure-volume diagrams, we represent irreversible processes with a dashed line, to clearly differentiate them from reversible processes, as shown in figure 3.8.

````{prf:example}
:label: ex-3-5
:enumerator: 3.5

Air is continuously compressed from 1 to 20 bar in a compressor. Just after leaving the compressor, the air enters a turbine that expands it from 20 to 1 bar. After leaving the turbine, the air is again inserted into the compressor.

What will be the shape of the processes on a pressure-volume diagram?

If the processes occur infinitely slowly, the pressure and specific volume always pass through the same values during the back-and-forth movements:

````

:::{figure} ../images/art-p071-1.jpg
:alt: Illustration from the original text
:::

````{prf:example}

However, if the processes are carried out with realistic speed, at each trip the final specific volume is larger than it would have been during a slow trip:

````

:::{figure} ../images/art-p071-2.jpg
:alt: Illustration from the original text
:::

````{prf:example}

Thus, the properties gradually shift on the pressure-volume diagram. Unless the processes are infinitely slow, running the compressor requires more energy than the turbine is able to provide. This excess energy is absorbed by the air, increasing its internal energy and temperature.

````

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

(sec-3-5)=
## 3.5 Quantifying Heat with an Open System

## System

With an open system, we will use the same method as with a closed system:

since we cannot quantify heat transfers directly, we will always proceed by

deduction. Mathematically, we simply reuse equation 3/14 to obtain:

:::{math}
Q_{1\rightarrow 2}=\dot{m}(\Delta h + \Delta e_{\mathrm{mech}.}) -\dot{W}_{1\rightarrow 2}
:::

:::{math}
q_{1\rightarrow 2}= \Delta h + \Delta e_{\mathrm{mech}.}- w_{1\rightarrow 2}
:::

for an open system.

Once again, the main challenge in quantifying a heat transfer is predicting and quantifying the change in enthalpy, $\Delta h$. For gases, $h$ is almost proportional to temperature; for liquids and vapors, the relationship is more complex. We will learn how to quantify enthalpy in fluids in chapter 4 (*the ideal gas*) and chapter 5 (*liquids and vapors*).

(3/24)

(3/25)

::::{admonition} A Bit of History: Temperature
:class: note
:label: hist-3-5

and Amount of Heat

\*

*By Philippe Depondt*

*Pierre and Marie Curie University, Paris*

In the second half of the 17th century, we started to concern ourselves with the matter of distinguishing between the *degree* of heat and the *quantity* of heat. This was a new question that could only arise when it became possible to reliably measure the temperature, or the “degree of heat,” of a body.

Our understanding of heat is largely tied to the sensation of hot or cold: we get burned from contact with boiling water, we feel cold when holding an ice cube in our hand. We can “feel” more or less hot, or more or less cold, an object containing “heat” would “be” more or less hot, all of this was a bit the same... In this context, the idea of a materiality of heat, the idea that a measurable quantity of heat could be transferred from one body to another and induce predictable and measurable temperature changes, remained far off!

Joseph Black (1728-1799), in Edinburgh, Scotland, then took a decisive step forward: he observed that snow does not instantly melt even though the ambient temperature can be well above the melting temperature of ice. Piles of snow, even in full sun-light, can take several days to disappear... He then posed the question: what is the temperature of the water capable of completely melting its own weight of snow at $0^{\circ}C (32 ^{\circ} F)$ without changing its temperature? The experiment provided the answer: $78^{\circ}C (172.4 ^{\circ} F)$! The lukewarm water cooled down, while the snow remained at the same temperature: the 78 degrees of heat brought by the lukewarm water were incorporated into the ice. The conclusion drawn was that the melting of the snow required the supply of these 78 degrees of heat by the liquid water. He called this heat *latent heat* [[39](#ref-39)], to differentiate it from *sensible heat* associated with measurable temperature changes. Beyond a clever experiment and a brilliant interpretation, a new concept had emerged.

Black continued his activities by conducting a whole series of calorimetry experiments, mixing water at different temperatures, mixing bodies of different natures at different temperatures; each time he

::::

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

demonstrated that the specific heat depends on the

nature of the body:

We must, therefore, conclude that different bodies, although they be of the same size, or even of

the same weight, when they are reduced to the

same temperature or degree of heat, whatever that

be, may contain very different quantities of the

matter of heat; which different quantities are necessary to bring them to this level, or equilibrium,

with one another.

Joseph Black, 1807 [[2](#ref-2)]

He did not make any assumptions about the nature

of this heat that he characterized. For most of his

contemporaries, however, its apparent conservation

indicated that it was a material fluid devoid of mass

which Lavoisier later named *caloric*. In this view,

this substance could be transferred from one body

to another to raise the temperature of the receiving

body and lower that of the giving body: some bodies

(such as water) contained more of it at a given temperature than others (like oil), resulting in different

specific heats. On the other hand, Black believed

that the fusion of a solid or the vaporization of a

liquid could be a kind of chemical combination of

the caloric fluid with the matter: the caloric would

then disappear as such and become “latent”.

:::{figure} ../images/fig-3-9.jpg
:label: fig-3-9
:enumerator: 3.9
:alt: Joseph Black conducting an experiment on latent heat during a university lecture in Edinburgh. One can imagine that he had no difficulty engaging the students, since it was about thermodynamics...

Joseph Black conducting an experiment on latent heat during a university lecture in Edinburgh. One can imagine that he had no difficulty engaging the students, since it was about thermodynamics...
:::

latent heat during a university lecture in Edinburgh. One can imagine that he had no difficulty engaging the students, since it was about thermodynamics...

*Engraving by unknown author published by Louis Figuier in 1867 (public domain)*

## Problems

```{exercise}
:label: prob-3-1
:enumerator: 3.1

**Steam Turbine A steam turbine (figure 3.10) is used in a small power plant fueled by the combustion of biomass. At the inlet of the turbine, the steam has the following properties: • Pressure: $45 bar (652.7 psi)$ • Temperature: $400^{\circ}C (932 ^{\circ} F)$ • Specific volume: $0.064 77 m^{3}kg^{-1}$ • Internal energy: $2914.2 kJ kg^{-1}$ At the outlet of the turbine, the following properties are measured: • Pressure: $0.75 bar (10.8 psi)$ • Temperature: $91.61^{\circ}C (196.9 ^{\circ} F)$ • Specific volume: $2.122 m^{3}kg^{-1}$ • Internal energy: $2316.3 kJ kg^{-1}$ The heat losses are negligible. 1. What is the specific power output released by the turbine in the form of work? 2. What steam flow rate is required to produce a power of $4 MW$? *Diagram* CC-0 *Olivier Cleynen; Photo* CC-by-sa *Siemens Pressebild***

:::{admonition} Answer
:class: dropdown

1) $w_{\mathrm{A}\rightarrow \mathrm{B}}= -730.3 kJ kg^{-1} 2)\dot{m} =\frac{\dot{W}_{\mathrm{A}\rightarrow \mathrm{B}}}{\dot{w}_{\mathrm{A}\rightarrow \mathrm{B}}} = 5.477kgs^{-1}$

:::
```

   :::{figure} ../images/fig-3-10.svg
   :label: fig-3-10
   :enumerator: 3.10
   :alt: Schematic diagram and photo of a steam turbine.
   
   Schematic diagram and photo of a steam turbine.
   :::

```{exercise}
:label: prob-3-2
:enumerator: 3.2

**Electric Power Generator In a portable electricity-generating power plant, the electric generator is driven by a mechanical shaft. Along this shaft, there is an air compressor and a turbine (figure 3.11). This type of device, sometimes simply called a “gas turbine”, is particularly compact and efficient; however, it requires the use of refined fuels. Schematic diagram of an electricity-generating turboshaft engine *Diagram* CC-by-sa *Olivier Cleynen* The compressor brings the air from atmospheric conditions to a high pressure and temperature. Compressor inlet: • Pressure: $1 bar (14.5 psi)$ • Specific volume: $0.751 m^{3}kg^{-1}$ • Internal energy: $206.78 kJ kg^{-1}$ Compressor outlet: • Pressure: $35 bar (507.6 psi)$ • Specific volume: $6.602 \times 10^{-2}m^{3}kg^{-1}$ • Internal energy: $578.13 kJ kg^{-1}$ Between the compressor and the turbine, the combustion chamber raises the temperature. The combustion takes place at constant pressure; it brings the gases to a specific volume of $0.1168 m^{3}kg^{-1}$ and an internal energy of $1028.8 kJ kg^{-1}$. At the turbine outlet, the gases are ready to be cooled in a catalytic exhaust system designed, among other things, to reduce noise emissions. Turbine outlet: • Pressure: $1.2 bar (17.4 psi)$ • Specific volume: $1.526 m^{3}kg^{-1}$ • Internal energy: $460.88 kJ kg^{-1}$ The air flow rate admitted into the machine is $8 kg s^{-1}$; the changes in its mechanical energy are nearly zero. Heat losses through the walls of the machine are negligible. Mechanical losses are $2 \%$ of the power transmitted to the generator. The electric generator itself has an efficiency of $85 \%$. 1. What power is received or rejected by the air in the compressor? 2. What power is received or rejected by the air in the turbine? 3. What is the electric power generated by the power plant? 4. Represent the processes undergone by the air as it passes through the engine on a pressure-volume diagram, qualitatively (that is, without showing numerical values). 5. What is the power lost in the form of heat together with the exhaust gases? [hint: it is the heat that the gases should lose to return to their state at the inlet of the compressor]**

:::{admonition} Answer
:class: dropdown

.2**
$1)\dot{W}_{\mathrm{A}\rightarrow \mathrm{B}}= +4.219 MW 2)\dot{W}_{\mathrm{C}\rightarrow \mathrm{D}}= -6.349 MW 3)\dot{E}_{\mathrm{generator}}= \eta _{\mathrm{generator}}\eta _{\mathrm{transmission}}(\dot{W}_{\mathrm{A}\rightarrow \mathrm{B}}+\dot{W}_{\mathrm{C}\rightarrow \mathrm{D}}) = -1.774 MW 5)\dot{Q}_{\mathrm{cooling}}= -\dot{W}_{\mathrm{A}\rightarrow \mathrm{B}}-\dot{Q}_{\mathrm{combustion}}-\dot{W}_{\mathrm{C}\rightarrow \mathrm{D}}= -2.897 MW$ (so more than half of the combustion heat… )

:::
```

   :::{figure} ../images/fig-3-11.jpg
   :label: fig-3-11
   :enumerator: 3.11
   :alt: generating turboshaft engine
   
   generating turboshaft engine
   :::

```{exercise}
:label: prob-3-3
:enumerator: 3.3

**Steam Boiler A power plant provides electricity as well as industrial and domestic heat from the combustion of household waste (known as a *cogeneration* plant). It is equipped with a water circuit that receives some of the heat released by the combustion, at constant pressure, in a boiler. Water enters the boiler (figure 3.12) in a liquid state, pressurized at $71.89 kg_{f}/cm^{2}(70.5 bar)$. Its internal energy is then $1160.2 kJ kg^{-1}$. We want to feed the turbine with $317 t h^{-1}$ of steam at an enthalpy of $3595.9 kJ kg^{-1}$. *Diagram* CC-0 *Olivier Cleynen* The combustion of household waste generates between $9$ and $11 MJ kg^{-1}$ of heat; the boiler efficiency is $76 \%$. What is the minimum flow rate of waste that the power plant must receive in order to produce the required amount of steam?**

:::{admonition} Answer
:class: dropdown

$1)\dot{m}_{\mathrm{waste}}\ge 92.1 t/h \approx 203 000 lb/h$

:::
```

   :::{figure} ../images/fig-3-12.jpg
   :label: fig-3-12
   :enumerator: 3.12
   :alt: Schematic diagram of a boiler operating from the combustion of waste.
   
   Schematic diagram of a boiler operating from the combustion of waste.
   :::

```{exercise}
:label: prob-3-4
:enumerator: 3.4

**Turbine Engine Nozzle In the nozzle of a small turbojet engine, the air pressure drops while its speed increases. The nozzle (figure 3.13) is a component without any moving parts: no work is done there. Heat losses are negligible, and the air flow rate is $26 kg s^{-1}(57.22 lb/s)$. At the inlet, the following characteristics are measured: • Specific enthalpy: $1092 kJ kg^{-1}$ • Velocity: $10 m s^{-1}(32.8 ft/s)$ • Temperature: $1250.33 ^{\circ} F (950 K)$ • Specific volume: $1.36 m^{3}kg^{-1}$ • Pressure: $2.325 kg_{f}/cm^{2}(2.28 bar)$**

:::{admonition} Answer
:class: dropdown

1) $C_{2}= 624 m s^{-1}$ (about $2250 km/h$ or
$1400 mph$...)
$2)\dot{V}_{1}=\dot{m} v_{1}= 35.4 m^{3}s^{-1}\&\dot{V}_{2}= 66.3 m^{3}s^{-1}$.

:::
```

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

   :::{figure} ../images/fig-3-13.png
   :label: fig-3-13
   :enumerator: 3.13
   :alt: Schematic diagram of a nozzle and installation (with variable geometry) on the Pratt & Whitney F100 engine of a Lockheed Martin F-16.
   
   Schematic diagram of a nozzle and installation (with variable geometry) on the *Pratt & Whitney* F100 engine of a Lockheed Martin F-16.
   :::

tion (with variable geometry) on the *Pratt & Whitney* F100 engine of a Lockheed Martin F-16.

*Diagram* CC-0 *Olivier Cleynen; Photo* CC-by-sa *Ad Meskens (edited)*

• Internal energy: $781.85 kJ kg^{-1}$

At the outlet, the air is brought back down to atmospheric pressure $(1 bar)$. It is predicted (we will see how in chapter 4) that the air characteristics will reach:

• Temperature: $944.7 ^{\circ} F (780.2 K)$

• Specific volume: $2.55 m^{3}kg^{-1}$

• Internal energy: $642.1 kJ kg^{-1}$

1. What is the ejection speed of the gases?

2. What are the volumetric flow rates of air at the inlet and outlet of the nozzle?

```{exercise}
:label: prob-3-5
:enumerator: 3.5

**Water Turbine An engineer is working on a small hydroelectric power plant project. The objective is to harness the flow of a river $(3170 US gal/s$ or $12 m^{3}s^{-1})$ with a turbine connected to an electric generator (figure 3.14). power plant *Diagram* CC-0 *Olivier Cleynen* In its liquid state, water is essentially incompressible (meaning its density does not change when its pressure changes). Its internal energy also varies negligibly during adiabatic compressions and expansions. The engineer first considers placing the turbine at the foot of a water reservoir, where the pressure is 4 bar and the velocity is nearly zero. The water falls through a height of $2 m (6.56 ft)$ through the turbine, and its ejection velocity is $4 m s^{-1}$ at atmospheric pressure $(1 bar)$. 1. What power could the turbine transmit to the generator? The engineer then studies a different configuration (figure 3.15). The turbine would keep the same characteristics but would be positioned further downstream from the water reservoir (shifted horizontally and vertically by $25 m$, or $82 ft$, each). *Diagram* CC-0 *Olivier Cleynen* 2. What would be the power transmitted in this case?**

:::{admonition} Answer
:class: dropdown

$1)\dot{W}_{\mathrm{A}\rightarrow \mathrm{B}}= -3.74 MW 2)\dot{W}_{\mathrm{A}\rightarrow \mathrm{B}2}= -6.68 MW$

:::
```

   :::{figure} ../images/fig-3-14.jpg
   :label: fig-3-14
   :enumerator: 3.14
   :alt: Schematic diagram of a hydroelectric power plant
   
   Schematic diagram of a hydroelectric power plant
   :::

   :::{figure} ../images/fig-3-15.jpg
   :label: fig-3-15
   :enumerator: 3.15
   :alt: Schematic diagram of the modified power plant. A rigid pipe brings water to the turbine placed lower down.
   
   Schematic diagram of the modified power plant. A rigid pipe brings water to the turbine placed lower down.
   :::

```{exercise}
:label: prob-3-6
:enumerator: 3.6

**Afterburner System In order to increase the thrust it generates, the nozzle from problem 3.4 is modified to add and *afterburning* device (later to be studied in §10.6.2 p. 291). It consists of a set of burners that allow a second combustion of fuel to occur in the engine, just before the air enters its expansion in the nozzle (figure 3.16). After the second combustion, the air goes through its expansion and acceleration until atmospheric pressure. At the inlet, the conditions are the same as those indicated in problem 3.4. The specific power added in the form of heat by the burners reaches $1322.5 kJ kg^{-1}$. The burnt fuel has a specific thermal capacity of $30 MJ kg^{-1}$. The combustion takes place at constant pressure, and it does not increase the gas’s kinetic energy. When the air completes its acceleration, its internal energy is predicted to be $1406.4 kJ kg^{-1}$ and its specific volume to be $5.59 m^{3}kg^{-1}$. 1. What is the increase in ejection speed (and thus thrust) generated by the afterburner? 2. How much fuel flow rate should be injected into the burners, in $kg/h$? 3. What is the volumetric flow rate of air after its final acceleration? 4. What is the efficiency of the afterburner, in other words, the ratio between the increase in gas kinetic energy and the increase in power to be supplied in the form of heat? tem. Its operation is studied in §10.6.2 p. 291. *Diagram* CC-by-sa *Olivier Cleynen***

:::{admonition} Answer
:class: dropdown

1) $+52\%$ compared to dry thrust ($C_{3\mathrm{b}}= 950.1\,\mathrm{m\,s^{-1}}$)
2) $\dot{m}_{\mathrm{fuel}}= \dot{m}_{\mathrm{air}}\frac{q_{1\rightarrow 2\mathrm{b}}}{q_{\mathrm{fuel}}}= 4126\,\mathrm{kg/h} = 9096\,\mathrm{lb/h}$
3) $\dot{V}_{3\mathrm{b}}= 145.3\,\mathrm{m^{3}\,s^{-1}}$
4) $\eta_{\mathrm{afterburning}}= \frac{\tfrac{1}{2}(C_{3\mathrm{b}}^{2}-C_{2}^{2})}{q_{1\rightarrow 2\mathrm{b}}} = 19.2\%$ (one reason
why it is never used on civilian aircraft)

:::
```

   :::{figure} ../images/fig-3-16.jpg
   :label: fig-3-16
   :enumerator: 3.16
   :alt: Schematic diagram of an afterburner system. Its operation is studied in §10.6.2 p. 291.
   
   Schematic diagram of an afterburner system. Its operation is studied in §10.6.2 p. 291.
   :::

```{exercise}
:label: prob-3-8
:enumerator: 3.8

**Theoretical and Actual Turbines In the free turbine of a helicopter’s turboshaft engine, air is expanded to extract work which is transmitted to the two rotors. The characteristics are as follows: • Mass flow rate: $2 kg s^{-1}$ • Heat losses: negligible • Inlet: 4 bar and $0.41 m^{3}kg^{-1}$ • Outlet pressure: 1.1 bar In the most favorable case, the expansion would take place reversibly, and the air would follow a relationship of the form $pv^{1.4}= k$ (where $k$ is a constant). 1. Which conditions must be met for the expansion to be reversible? 2. What would be the power supplied by the turbine in this case? In practice, it is observed that the power supplied by the turbine is $20 \%$ lower than the value calculated above. An engineer installs probes at the inlet and outlet of the turbine and observes that the pressure there indeed reaches the theoretically expected values. S/he also measures the heat transfer from the air to the turbine and confirms that it is negligible. 3. Draw the processes undergone by the air in the reversible and real cases on a pressure-volume diagram, qualitatively. 4. In which form will the engineer find (and measure) the missing $20 \%$ of power?**

:::{admonition} Answer
:class: dropdown

.8**
1) see §2.4.4 p. 49
2) $\dot{W}_{\mathrm{A}\rightarrow \mathrm{B}}=\dot{m}\,k^{\frac{1}{1.4}}\left[\frac{1}{-\frac{1}{1.4}+1} p^{-\frac{1}{1.4}+1}\right]_{p_{\mathrm{A}}}^{p_{\mathrm{B}}}= -354.1\,\mathrm{kW}$
4) In the form of $\Delta h$ – the outlet air will have
higher specific volume and temperature (internal
energy), and maybe also higher kinetic energy.

:::
```

```{exercise}
:label: prob-3-9
:enumerator: 3.9

**Compressor and Turbine of a Turboprop Engine The compressor within a turboprop engine (figure 3.17) admits a constant flow of air at ambient conditions $(0.8 bar/11.6 psi$ and $1 m^{3}kg^{-1})$. It must bring this air to a final pressure of $11 bar (159.5 psi)$, without any heat transfer. *Diagram* CC-by-sa *Olivier Cleynen* Within the compressor, the air behaves in such a way that its properties follow the relation $p v^{1.4}= k$, where $k$ is a constant. 1. What is the minimum specific power to be supplied to the compressor? 2. Represent the properties of the gas as it passes through the compressor on a pressure-volume diagram, qualitatively. 3. On the above diagram, show the change the gas would undergo if the compressor were not reversible (real compressor, inducing internal friction in the gas) but nevertheless maintained its outlet pressure at 11 bar.**

:::{admonition} Answer
:class: dropdown

1) $w_{\mathrm{A}\rightarrow \mathrm{B}}\ge \int ^{\mathrm{B}}_{\mathrm{A}}vdp = +312 kJ kg^{-1}$
2) & 3) see fig. 3.8 p. 71;
4) $w_{\mathrm{C}\rightarrow \mathrm{D}}= -729.3\,\mathrm{kJ\,kg^{-1}}
5) $\dot{m}_{\mathrm{air}}= \frac{\dot{W}_{\mathrm{propeller}}}{w_{\mathrm{propeller}}} = \frac{\dot{W}_{\mathrm{propeller}}}{w_{\mathrm{A}\rightarrow \mathrm{B}}+w_{\mathrm{C}\rightarrow \mathrm{D}}}= 1.438\,\mathrm{kg\,s^{-1}}$$.
*Engineering Thermodynamics* by Olivier Cleynen

:::
```

   :::{figure} ../images/fig-3-17.jpg
   :label: fig-3-17
   :enumerator: 3.17
   :alt: Schematic diagram of a turboprop engine. These engines are studied in more detail in §10.5.4 p. 286.
   
   Schematic diagram of a turboprop engine. These engines are studied in more detail in §10.5.4 p. 286.
   :::

::::{admonition} A Bit of History
:class: note

*Engineering Thermodynamics* by Olivier Cleynen

::::

Within the same engine, the turbine, which is adiabatic, must power not only to the compressor but also the propeller at the front of the engine. It is equipped with numerous probes to measure the properties of the air.

At its inlet, the following properties are measured:

• Pressure 11 bar

• Velocity $12 m s^{-1}$

• Specific volume $0.36 m^{3}kg^{-1}$

• Internal energy $985.8 kJ kg^{-1}$

At the outlet, the properties of the air have become:

• Pressure 0.8 bar

• Velocity $12 m s^{-1}$

• Specific enthalpy $652.5 kJ kg^{-1}$

4. What is the specific power of the turbine?

5. What condition must be met within the engine to provide the propeller with a power of $600 kW$?
