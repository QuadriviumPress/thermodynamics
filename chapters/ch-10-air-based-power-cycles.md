---
title: "10. Air-Based Power Cycles"
short_title: "Chapter 10"
label: ch-10-air-based-power-cycles
---

:::{figure} ../images/art-p277-1.jpg
:alt: Chapter opening illustration
:::

# 10. Air-Based Power Cycles

(ch-10)=

Air-Based Power Cycles

*Build Your Own Combustion Cycle: the Essential Starter Pack*

:::{figure} ../images/art-p267-1.svg
:alt: Illustration from the original text
:::

:::{admonition} Executive summary
:class: tip
Air-based engines are more compact and lighter than steam engines. Many modifications are made to ideal cycles to reduce bulk and adapt to the temperature limits of engine components.
:::

## Introduction

In this final chapter, we cover the cycles of engines that use air a as a working fluid. These are sometimes called *gas power cycles*, although because the term *gas engine* is understood differently in different contexts,

we choose the term *air-based engine* in this book. This chapter 10 aims to answer the same two questions as its predecessor with liquids/vapors:

• Why and how are air-based engines used today?

• Why are we moving away from ideal cycles and how do we quantify these compromises?

(sec-10-1)=
## 10.1 Why Use an Air-Based Engine?

The use of air as a working fluid, rather than water, brings several advantages.

• First, it is possible to completely dispense with condensers and coolers. The cooling phase (§7.2.1) takes place directly in the atmosphere, which easily accommodates all the hot gases that are rejected, and which serves as a reservoir from which to draw fresh air to feed into the engine.

For an equal power level, the mass, volume, and often the cost of air-based engines are therefore greatly reduced compared to their steam counterparts. This is particularly interesting when the engine must contribute to carrying its own weight.

• Second, the heat input is carried out without loss. It is now possible to have the combustion occur directly within the working fluid – this is why we speak of *internal combustion engines* – and thus to avoid the heat loss associated with a boiler (§9.3.3).

The main drawback of air-based engines is that internal combustion requires a high-quality fuel. Since the combustion residues must flow inside the thermodynamic part of the machine, we cannot use economical or otherwise advantageous heat sources such as the combustion of waste, wood, or coal.

Ultimately, the relatively lower weight of air engines compared to their steam counterparts means that they are systematically used when mass plays an important role, such as in air or road transport.

(sec-10-2)=
## 10.2 Evaluation of Air-Based Engines

(sec-10-2-1)=
### 10.2.1 Thermal efficiency

It now goes without saying that we always seek to achieve a high *thermal* its theoretical maximum $\eta _{\mathrm{Carnot} \mathrm{engine}}= 1 - \frac{T_{\min.}}{T_{\max.}}$ (7/6).

As we have already suggested in §9.2, thermal efficiency should not, however, be maximized at the expense of other important parameters, the most notable of which we present below for air-based engines.

(sec-10-2-2)=
### 10.2.2 Work ratio

In a running engine, the irreversibility of compressions and expansions is not independent of speed. When they operate outside their optimal operating range, engines thus see their specific power decrease. Irreversibilities can even reduce efficiency to zero, with the engine running without producing useful work (as would a disengaged car engine). The *work ratio* is a concept that assesses the robustness of a cycle to the increase of these irreversibilities.

In order to address this concept, let us first study the case of an engine whose arbitrarily-chosen energy flows are described in figure 10.1; in this engine, compressions and expansions are reversible. Now, if instead of being ideal, the turbine suddenly saw its isentropic efficiency drop down to $95 \%$, it would supply $95 W$. The net power of the engine would then decrease from $10$ to $5 W$ – a reduction of $50 \%$.

:::{figure} ../images/fig-10-1.jpg
:label: fig-10-1
:enumerator: 10.1
:alt: The cycle of a hypothetical engine with low work ratio. The delivered poweriṡ𝑊net =̇ 𝑊compression+̇𝑊expansion = +90+(−100) = −10 W, and the efficiency 20 = 50 %.

The cycle of a hypothetical engine with low work ratio. The delivered power is $\dot{W}_{\mathrm{net}}=\dot{W}_{\mathrm{compression}}+\dot{W}_{\mathrm{expansion}}= +90+(-100) = -10 W$, and the efficiency
:::

:::{math}
\eta _{\mathrm{engine}}= -\frac{\dot{W}_{\mathrm{net}}}{\dot{Q}_{\mathrm{in}}} = - \frac{-10}{20} = 50\%.
:::

*Diagram* CC-0 *Olivier Cleynen*

Let us now compare this case with an engine of the same efficiency, same power, but with a different cycle, as shown in figure 10.2. In that new engine, if the isentropic efficiency of the turbine went from $100 \%$ to $95 \%$, the net power would decrease from 10 to $9 W$ – a decrease of only $10 \%$.

We can see here that the larger the share of the turbine power in the net power delivered, and the less the cycle efficiency is affected by irreversibilities. We generalize and formalize this “turbine share” with the concept of *work ratio* $M_{w}$, defined as the ratio between the net power and the gross power of an engine:

:::{math}
:label: eq-10-1
:enumerator: 10/1
M_{w}\equiv \frac{\dot{W}_{\mathrm{net}}}{\dot{W}_{\mathrm{gross}}} = \frac{\dot{W}_{\mathrm{expansions}}}{\dot{W}_{\mathrm{expansions}}+\left|\dot{W}_{\mathrm{compressions}}\right|}
:::

where $M_{w}$ is the work ratio (dimensionless); $W_{\mathrm{expansions}}$ is the shaft power released during expansions;

and $W_{\mathrm{compressions}}$ is the shaft power received during compressions.

:::{figure} ../images/fig-10-2.jpg
:label: fig-10-2
:enumerator: 10.2
:alt: The cycle of a second (also hypothetical) engine, with a high work ratio. The delivered power$\dot{W}_{\mathrm{net}}= +10 + (-20) = -10 W$, and the efficiency $\eta _{\mathrm{engine}}=$

The cycle of a second (also hypothetical) engine, with a high work ratio. The delivered power$\dot{W}_{\mathrm{net}}= +10 + (-20) = -10 W$, and the efficiency $\eta _{\mathrm{engine}}=$
:::

$-\frac{-10}{20} = 50 \%$ are identical to those of the engine described in figure 10.1. *Diagram* CC-0 *Olivier Cleynen*

A machine with a large work ratio loses less of its efficiency when operating outside its optimal speed range: it is therefore more flexible in use. The work ratio is one of the indicators of a engine’s responsiveness, namely, its ability to change power and speed quickly. A parallel can be drawn with the concept of *net profit margin* in economics: all else being equal, it is more interesting to sell items bought at $2$AC for $3$AC than items bought at $100$AC for $101$AC, notably because the profit of $1$AC is then less sensitive to a change in price or cost imposed by the market.

The Carnot engine is the typical example of a thermodynamic cycle with high efficiency but low work ratio. By plotting the cycle on a pressure-volume diagram (figure 7.10 p. 188), this weakness is evident: the curves during the compression and expansion phases are very close to each other. Rankine, when he modified this cycle (§9.4.2), significantly increased the work ratio.

In general, obtaining high thermal efficiency requires a high compression ratio (so as to achieve a high temperature before heat transfer is initiated). Obtaining a high work ratio requires low compression work (so as to minimize the engine’s sensitivity to irreversibilities). These two objectives are often contradictory, and it will be up to the engineer to find the best compromise.

(sec-10-2-3)=
### 10.2.3 Specific thrust and specific power

We use the concepts of *specific thrust* $\frac{P\dot{}}{m}$ and *specific power* $w_{\mathrm{net}}$, in other words, the thrust and power of the engine divided by the mass flow rate of air passing through it, to compare engine cycles succinctly. Increasing these parameters is often desirable in applications where a high power-to-weight ratio is sought.

For example, a heavier aircraft must provide greater lift, which increases drag, and in turn the thrust, and finally and the power required to generate it – so in that case, an increase in efficiency is not always justified if it results in an increase in weight or size.

(sec-10-2-4)=
### 10.2.4 Other evaluation criteria

Many more criteria need to be considered in the design of an engine, which we will not explore in this book. They include:

• purchase cost, which is directly related to the complexity and size of the engine;

• ecological impact;

• ease of maintenance and reliability;

• responsiveness;

• the level of vibration generated.

Taking into account each of these factors can justify deliberately limiting the efficiency of the engine. Indeed, when the student acquires their first motor vehicle, they will likely attach more importance to the purchase cost than to the energy consumption – and in the same way, they may not choose to fit it with a racing engine requiring constant maintenance.

Truth be told, there is very little to add to what our eminent and favorite theorist already explained in 1824:

One must not flatter oneself for ever exploiting, in practice, the entirety of the motive power contained in combustibles. Attempts that one would make to to approach this result would prove more harmful than beneficial, if they led to the neglect of other important considerations. The economy of fuel is but one of the conditions to be fulfilled by fire machines; in many circumstances, it is but secondary, and must often yield precedence to the safety, the solidity, the durability of the machine, to the small amount of space that it must be made to occupy, the low cost of its establishment, etc. Knowing how to appreciate, in each case, at their true value, the considerations of convenience and economy that may present themselves; knowing how to discern the most important from those that are merely accessory, weighing them all properly against one another, so as to attain by the easiest means the best possible result, such must be the principal talent of the man [or woman] called upon to lead, to coordinate between them the labors of his [or her] fellow beings, to make them converge toward a useful end, of whatever nature it may be.

Sadi Carnot, 1824 [[4](#ref-4)]

(sec-10-3)=
## 10.3 Reciprocating Engines

Reciprocating engines, often called *piston engines*, take in a fin ite amount of air and perform their thermodynamic cycle on this mass. The cycle is repeated several times over time, and often several times in parallel, in order to provide continuous power. An automobile engine typically performs about ffity cycles per second.

(sec-10-3-1)=
### 10.3.1 Advantages of piston engines

From a thermodynamic perspective, the main advantage of these engines is that it is much easier to manipulate a fixed mass of air than a continuous flow. Manufacturing a cylindrical piston to fti tightly in a cylindrical bore is comparatively simple, and this allows the volume and pressure of the fluid to be precisely controlled. For example, it is possible to carry out combustion at a constant temperature (as prescribed by Carnot) by varying the volume during combustion. The same operation in a steady flow machine would require combustion to take place in a turbine (§4.4.4 p. 98), which is much more challenging.

Another advantage of piston engines is that the maximum temperature of the cycle is only reached sporadically (periodically, but always briefly ). During combustion, it is thus possible to reach gas temperatures that exceed the metallurgical limits of the engine, which, as we saw in chapter 7 (*the second law*), improves efficiency.

On the other hand, the weight and complexity of mechanisms of piston engines (connecting rods, crankshaft, valves, and the various circuitry to and from the cylinders) become major disadvantages in applications very high powers and rotational speeds are required.

(sec-10-3-2)=
### 10.3.2 The Otto cycle

The German engineer Nicolaus Otto is credited with the development of the engine known today as the *petrol* or *gasoline engine* in 1864. The basic cycle of this engine, called the *Otto cycle*, consists of two isentropic phases framed by two isochoric phases; it is described in figure 10.3.

:::{figure} ../images/art-p272-1.svg
:alt: Illustration from the original text
:::

The Otto cycle is designed to allow for a simple implementation of the heat addition phase. The fuel is mixed with air before being inserted into the engine, and a very rapid combustion is triggered with a spark when the volume in the cylinder is minimal: this is known as *spark ignition*. Otto originally intended his engine for stationary applications, but its relative simplicity and responsiveness would ensure its success in transportation (notably through his son Gustav Otto, an aircraft manufacturer whose company would later become bmw).

The efficiency of the theoretical Otto cycle is easily calculable. The heat input $q_{\mathrm{combustion}}= c_{v}(T_{\mathrm{C}}- T_{\mathrm{B}})$ is performed at constant volume (equation 4/22). The heat rejection, in practice, is done outside the engine, after exiting the exhaust pipe. From a thermodynamic point of view, the air continues its cycle in the atmosphere before re-entering the engine (§6.2.1), and thus the heat rejected is $q_{\mathrm{cooling}}= c_{v}(T_{\mathrm{A}}-T_{\mathrm{D}})$. Thus, since in theory no heat transfer takes place in the compression and expansion phases, and if we consider that the properties $(c_{v})$ of the gas do not change during combustion, the efficiency $\eta _{\mathrm{Otto}}$ of the theoretical cycle is simply given by:

:::{math}
:label: eq-10-2
:enumerator: 10/2
\eta _{\mathrm{Otto}}= \left|\frac{-q_{\mathrm{combustion}}- q_{\mathrm{cooling}}}{q_{\mathrm{combustion}}}\right| = 1 + \frac{q_{\mathrm{cooling}}}{q_{\mathrm{combustion}}} = 1 + (\frac{T_{\mathrm{A}}- T_{\mathrm{D}}}{T_{\mathrm{C}}- T_{\mathrm{B}}})
:::

By defining the *compression ratio* $\varepsilon$ as:

:::{math}
:label: eq-10-3
:enumerator: 10/3
\varepsilon \equiv v_{\mathrm{A}}
:::

:::{math}
v_{\mathrm{B}}
:::

it is possible to show that [Equation 10/2](#eq-10-2) can be reformulated to express the efficiency as:

:::{math}
:label: eq-10-4
:enumerator: 10/4
\eta _{\mathrm{Otto}}= 1 - \varepsilon ^{\gamma -1}1
:::

This equation indicates that the efficiency of the Otto engine depends solely on the compression ratio, and not on the amount of heat supplied during combustion. This may at first be surprising: why does $T_{\mathrm{C}}$, the maximum temperature of the cycle, no longer appear here? The answer is that in this cycle, as the amount of burned fuel is increased, the increase in the average temperature during heat addition is exactly offset by the increase in the average temperature during heat rejection.

[Equation 10/4](#eq-10-4) owes its simplicity to the the fact that we neglected the change in air properties during combustion, as well as the irreversibilities during compression and expansion. It should therefore be used with great caution; however, the trend it describes remains valid. Engineers are constantly seeking to increase the compression ratio of their engines to enhance efficiency. An immediate limit to this ratio is the temperature at which the air-fuel mixture spontaneously ignites, causing premature combustion.

(sec-10-3-3)=
### 10.3.3 The Diesel cycle

The *Diesel engine*, the child of his patient and hard-working inventor, German engineer Rudolf Diesel (§7.6), powers today the overwhelming majority of commercial road and marine transportation.

From a strictly thermodynamic point of view, the theoretical Diesel cycle differs from the Otto cycle only in its combustion mode: heat addition occurs at constant pressure and not at constant volume, as shown in figure 10.4.

:::{figure} ../images/fig-10-4.svg
:label: fig-10-4
:enumerator: 10.4
:alt: Theoretical Diesel cycle represented on pressure-volume and temperature-entropy diagrams. These diagrams depict the ideal path, without compression or expansion irreversibilities.

Theoretical Diesel cycle represented on pressure-volume and temperature-entropy diagrams. These diagrams depict the ideal path, without compression or expansion irreversibilities.
:::

*Diagrams* CC-0 *Olivier Cleynen*

Since the heat addition $q_{\mathrm{combustion}}= c_{p}(T_{\mathrm{C}}- T_{\mathrm{B}})$ (equation 4/17) is done simultaneously with the production of work, there is no simple expression for the efficiency $\eta _{\mathrm{Diesel}}$, which no longer depends solely on the compression ratio. It will need to be calculated by studying the cycle step by step. It will then be observed that all else being equal (same compression ratio and same maximum temperature), the Diesel cycle has a lower efficiency than the Otto cycle.

:::{aside}
« [What is needed is the] production of a very high temperature (much above the ignition temperature of the combustible) not by combustion, but by compression of the air… the combustible, therefore, must not be previously mixed with the air, but the latter must be compressed separately, otherwise, long before the required compression has been attained, ignition will be produced, and the cycle interrupted. »

Rudolf Diesel, 1893 [[23](#ref-23), [24](#ref-24)]
:::

In order to understand the interest of this cycle and the true difference between a Diesel engine and a gasoline engine, some historical context is needed. In 1892, Rudolf Diesel designed a “rational” engine to implement the Carnot cycle. He was looking for two characteristics:

• a high compression ratio, to increase the air temperature before combustion;

• combustion at a constant temperature.

To achieve this, Diesel had to wait until the end of compression to inject the fuel, in order to avoid premature ignition. The isothermal heat addition requires a progressive combustion. Thus, the original Diesel engine is inherently equipped with *direct fuel injection*, independent of air intake. The Diesel cycle is interesting because it *enables* a higher compression ratio and combustion quality compared to the Otto cycle.

Diesel’s engine evolved continuously from the impractical concept described in the 1893 *Theory and Construction of a Rational Heat Engine Intended to Replace the Steam Engines and Combustion Engines Known to Date* [[23](#ref-23), [24](#ref-24)] $(400 bar$ and isothermal combustion of coal powder) to the first production models he developed at the manufacturer man $(40 bar$ and isobaric combustion of petroleum). Like Otto, Diesel initially focused on stationary engines (his first prototypes were single-cylinder and over three meters high), but it was ultimately applications in commercial transportation, where its excellent efficiency and operating economics gave him the advantage over spark-ignition engines, that brought his work fame.

(sec-10-3-4)=
### 10.3.4 Implementation of the cycles

The two cycles described above are only idealizations – they serve as conceptual standards for comparing actual cycles. Their implementation in a real engine requires taking into account numerous factors, including:

• the need to purge the air and combustion products from inside the cylinder after the cycle, and the impossibility of doing it completely;

• the fact that the volume occupied by the gas is linked to the rotation of the engine shaft, and that it therefore is not possible to control it independently of the engine’s operating speed;

• irreversibilities during compressions and expansions caused by fast piston movements;

• heat transfers to and from the cylinders during the cycle;

• gas leaks (blow-by) in the clearances between pistons and cylinders.

Once these factors, as well as the pursuit of objectives related to user comfort and control of air pollution, are taken into account, the cycle obtained inside a cylinder of a practical engine may for example resemble the one represented in figure 10.5. In the automotive sector in particular, the adoption of direct injection and the increase in compression ratios for gasoline engines to reduce fuel consumption and emissions has blurred the gasoline/Diesel distinction – gasoline engines are now closer to Rudolf Diesel’s concept than to Nikolaus Otto’s.

:::{figure} ../images/fig-10-5.jpg
:label: fig-10-5
:enumerator: 10.5
:alt: A realistic representation of the pressure and volume changes during a cycle in a practical gasoline engine.

A realistic representation of the pressure and volume changes during a cycle in a practical gasoline engine.
:::

*Diagram* CC-0 *Olivier Cleynen*

(sec-10-3-5)=
### 10.3.5 Number of cylinders and turbocharging

An important drawback of reciprocating engines is that the irreversibility of compressions and expansions increases significantly with the piston speed in the cylinders. The traditional approach to overcome this issue is to increase the number of cylinders operating simultaneously in the engine (figure 10.6). This way, the stroke traveled by each piston for a given displacement volume can be reduced. An advantage associated with this approach is that the motion of mechanical parts is better balanced (and the engine sounds more harmonious!).

:::{figure} ../images/fig-10-6.png
:label: fig-10-6
:enumerator: 10.6
:alt: On the left, a 1950 Curtiss-Wright r-3350 *Duplex-Cyclone* of $3500 hp$ with 18 cylinders arranged in two successive rows. Four of these engines powered the long-range aircraft Lockheed *Super Constellation*. On the right, a 1991 Honda ra121e V12 engine. It powered the McLaren mp4/6 Formula 1 car.

On the left, a 1950 Curtiss-Wright r-3350 *Duplex-Cyclone* of $3500 hp$ with 18 cylinders arranged in two successive rows. Four of these engines powered the long-range aircraft Lockheed *Super Constellation*. On the right, a 1991 Honda ra121e V12 engine. It powered the McLaren mp4/6 Formula 1 car.
:::

*Photo of the Duplex-Cyclone* CC-by-sa *by Frank C. Müller Photo of the V12* ra121e CC-by-sa *by Commons User:Morio*

Unfortunately, the mechanical complexity, size, and manufacturing and maintenance costs of engines increase rapidly with the number of cylinders; therefore, in applications where these factors are crucial (such as the majority of the automotive sector, for example), usually only four, or even three or two cylinders are used. It is nevertheless expected that these engines operate efficiently over a wide range of power outputs.

A commonly adopted solution for this is *turbocharging*. It involves delegating some of the compression and expansion work to a small device called a *turbocharger* or simply *turbo*, which is compact and lightweight (figure 10.7). The turbo’s compressor is powered by its turbine, which operates with exhaust gases (we will study this system further in §10.5.2). Turbocharging helps increase the specific power (that is to say, it reduces the size and speed of an engine for a given power output).

Since the use of a turbocharger negatively affects the responsiveness of an engine, it is possible to allow the intake air to bypass it while the engine speed is changing. Furthermore, temperature changes in the turbo can be compensated for by cooling before insertion into the cylinders (this technique is studied further in §10.6.1). These processes make modern engines complex thermodynamic systems capable of performing a wide range of very different cycles depending on operating conditions.

Figure 10.7: A cutaway view of a turbo to show its internal arrangement. Atmospheric air enters from the right and is compressed as it is propelled outward by the centrifugal compressor; it is then fed into the engine. Exhaust gases enter from the center left and exit to the left after spinning the centripetal turbine, which powers the compressor via the central rotating shaft. Since the only moving part is very compact (about $20 cm$ here), very high rotation speeds can be achieved, typically exceeding $200 000 rpm$. *Photo* nasa *(public domain)*

(sec-10-4)=
## 10.4 Components of Gas Turbomachinery

Before delving into the cycles of turbine engines, we will briefly review the operation of their main components. Since turbomachines operate with steady fluid flow, we will consistently refer to the concepts of chapter 3 (*open systems*) from now on.

(sec-10-4-1)=
### 10.4.1 Compressor

:::{aside}
« In order to grant air a great expansion in volume, in order to produce through this expansion a large change in temperature, it would be necessary to take it first under a sufficiently high pressure […] This operation would require a special apparatus, an apparatus which does not exist in steam engines. In these, water is in the liquid state when it is made to enter the boiler; it requires, for its introduction, only a small force pump of small dimensions. »

Sadi Carnot, 1824 [[4](#ref-4)]
:::

The compression and expansion phases in engines are often adiabatic, and always irreversible. It is difficult to achieve high-quality flow in the compressor, moreso than in the turbine because the pressure gradient promotes boundary layer separation. It is a heavy, bulky component with complex geometry ([Figures 10.8](#fig-10-8) and 10.9). Most compressors are *axial*, meaning that the air passes through them parallel to the axis of rotation, but sometimes *centrifugal* compressors are used, which sling the air radially; regardless of the method used, the thermodynamic process undergone by the air remains the same.

:::{figure} ../images/fig-10-8.jpg
:label: fig-10-8
:enumerator: 10.8
:alt: The stator casing which houses the rotor (not shown) in the an axial compressor of a turbojet engine.

The stator casing which houses the rotor (not shown) in the an axial compressor of a turbojet engine.
:::

*Photo* CC-by-sa *Olivier Cleynen*

:::{figure} ../images/fig-10-9.jpg
:label: fig-10-9
:enumerator: 10.9
:alt: Schematic representation of an air compressor.

Schematic representation of an air compressor.
:::

*Diagram* CC-by-sa *Olivier Cleynen*

Just as we did for the turbine (9/6), we quantify the efficiency of a compressor by comparing its power with that of an ideal compressor (one that would be isentropic). We call this parameter the *isentropic efficiency* $\eta _{\mathrm{C}}$ of the compressor:

:::{math}
:label: eq-10-5
:enumerator: 10/5
\eta _{\mathrm{C}}\equiv \frac{\dot{W}_{\mathrm{isentropic} \mathrm{compressor}}}{\dot{W}_{\mathrm{actual} \mathrm{compressor}}}
:::

where$\dot{W}_{\mathrm{actual} \mathrm{compressor}}$ is the actual shaft power received by the compressor, and $W_{\mathrm{isentropic} \mathrm{compressor}}$ is the power of an isentropic compressor that would operate with the same mass flow rate and between the same pressures.

Like that of a turbine, the isentropic efficiency of a compressor is always less than 1. If this efficiency is known, we can compare the actual properties of the air at the inlet and outlet of the compressor with those that would be measured in the ideal case:

:::{math}
:label: eq-10-6
:enumerator: 10/6
w_{\mathrm{compressor}}= c_{p}(T_{\mathrm{actual}}- T_{\mathrm{A}}) = \frac{1}{\eta _{\mathrm{C}}} c_{p}(T_{\mathrm{ideal}}- T_{\mathrm{A}})
:::

where $w_{\mathrm{compressor}}$ is the specific power of the compressor $(J kg^{-1})$, $T_{\mathrm{ideal}}$ is the ideal outlet temperature (isentropic compressor) $(K)$,

and $T_{\mathrm{actual}}$ is the actual outlet temperature $(K)$.

````{prf:example}
:label: ex-10-1
:enumerator: 10.1

For air, we have $c_{p (\mathrm{air})}= 1005 J kg^{-1}K^{-1}, c_{v (\mathrm{air})}= 718 J kg^{-1}K^{-1}, R_{\mathrm{air}}= 287 J kg^{-1}K^{-1}$, and $\gamma _{\mathrm{air}}= 1.4$. The compressor of a turbofan jet engine has an isentropic efficiency of $85 \%$; it takes in air at a rate of $38 kg s^{-1}$ at 1 bar and $5^{\circ}C$. The outlet pressure is 40 bar. What is the required power?

The process can be qualitatively represented on a $T - s$ diagram as shown below.

We start by calculating the power of an ideal (isentropic) compressor; the outlet temperature in that case would be (4/37): $T_{\mathrm{B}^{'}}= T_{\mathrm{A}}(\frac{p_{\mathrm{B}}}{p_{\mathrm{A}}} ) ^{\frac{\gamma-1}{\gamma}}= (5 + 273.15) (40)^{\frac{0.4}{1.4}}= 798 K = 524.9^{\circ}C = 976.7 ^{\circ} F$. The ideal compressor would then receive $w_{\mathrm{isentropic} \mathrm{compressor}}= c_{p(\mathrm{air})}(T_{\mathrm{B}^{'}}-T_{\mathrm{A}}) = 1005 (798 - 278.15) = +5.225 \times 10^{5}J kg^{-1}= +522.5 kJ kg^{-1}$.

````

:::{figure} ../images/art-p279-1.jpg
:alt: Illustration from the original text
:::

````{prf:example}

With equation 10/5, the power of the compressor naturally comes as:$\dot{W}_{\mathrm{compressor}}=\dot{m} \frac{1}{\eta _{\mathrm{C}}} w_{\mathrm{isentropic} \mathrm{compressor}}= 38 \times \frac{1}{0.85} \times 5.225 \times 10^{5}= 2.336 \times 10^{7}W = 23.36 MW$.

Note that unlike for turbines, the actual power is *greater* than the theoretical power, and we must divide by the efficiency in the final calculation.

Equation 10/6 would allow us to calculate the actual outlet temperature: $T_{\mathrm{B} \mathrm{real}}= \frac{1}{\eta _{\mathrm{C}}} c_{p}(T_{\mathrm{B}^{'}}- T_{\mathrm{A}}) + T_{\mathrm{A}}= \frac{1}{0.85}(798 - 278.15) + 278.15 = 889.7 K = 616.6^{\circ}C = 1141.8 ^{\circ} F$. Here, the $92^{\circ}C (165 ^{\circ} F)$ difference from the isentropic case are the result of converting work into heat due to friction in the compressor, an unnecessary expense representing$\dot{m} c_{p}(T_{\mathrm{B}}- T_{\mathrm{B}^{'}}) = +3.5 MW$.

````

In practice, several air bleeds can be made within the compressor to feed other equipment and to cool the turbine (10.6.3). During transitional phases, the compressor can also be relieved of part of the mass flow by allowing air to leak through discharge valves.

(sec-10-4-2)=
### 10.4.2 Combustion chamber

The heat input of turbomachines takes place in one or more combustion chambers (figures 10.10 and 10.11). The air is heated at constant pressure by combustion; its temperature and specific volume greatly increase.

:::{figure} ../images/fig-10-10.jpg
:label: fig-10-10
:enumerator: 10.10
:alt: Section of an annular combustion chamber in which the flow was from left to right. The photo shows a section of a Rolls-Royce Turboméca Adour, a small turbofan engine designed in 1968.

Section of an annular combustion chamber in which the flow was from left to right. The photo shows a section of a Rolls-Royce Turboméca *Adour*, a small turbofan engine designed in 1968.
:::

*Photo* CC-by-sa *Olivier Cleynen*

:::{figure} ../images/fig-10-11.svg
:label: fig-10-11
:enumerator: 10.11
:alt: Schematic representation of a combustion chamber.

Schematic representation of a combustion chamber.
:::

*Diagram* CC-0 *Olivier Cleynen*

No work is done in the combustion chamber, and the pressure remains approximately constant. Since the heat input occurs within the gas itself, the maximum temperature of the cycle is not limited by heat transfer through a solid wall. The maximum temperature of the air can even exceed that of the melting point of the chamber walls, which are insulated with several layers of compressed air. Compared to steam power plants, this allows for a temperature increase of about $200 K$.

The power delivered in the combustion chamber is quantified rather easily by modifying equation 4/19 to account for the change in air properties during combustion, which increases the value of $c_{p}$ by about $10 \%$:

:::{math}
q_{\mathrm{chamber}}= h_{\mathrm{B}}- h_{\mathrm{A}}= c_{p(\mathrm{gases})}T_{\mathrm{B}}- c_{p(\mathrm{air})}T_{\mathrm{A}} (10/7)
:::

Fluid flow within the combustion chamber depends in a correlated manner on combustion chemistry and the spatial distribution of velocities and pressure: it is therefore difficult to model. In practice, a slight pressure drop is generated between the inlet and outlet of the chambers. The inful ence on the turbine power of the fuel mass flow rate$\dot{m}_{\mathrm{fuel}}$, always much lower than that of air, can be safely neglected.

(sec-10-4-3)=
### 10.4.3 Turbine

The primary role of the turbine (figures 10.12 and 10.13) is to power the compressor: it must therefore extract enough power from the air to operate the latter and compensate for any transmission losses. Depending on the configuration of the turbomachine, the turbine may then be designed to further extract energy from the gases in order to power other components, as we will see in §10.5 below.

Just like for liquids/vapors (eq. 9/6 p. 247), we measure the performance of a turbine by quantifying its *isentropic efficiency* $\eta _{T}$:

:::{math}
\eta _{T}\equiv \frac{\dot{W}_{\mathrm{actual} \mathrm{turbine}}}{\dot{W}_{\mathrm{isentropic} \mathrm{turbine}}} (10/8)
:::

The power extracted by the turbine is thus easily expressed in terms of the actual $T_{2 \mathrm{real}}$ and ideal $T_{2^{'}}$ temperatures at its outlet:

:::{math}
w_{\mathrm{turbine}}= c_{p(\mathrm{gases})}(T_{2 \mathrm{actual}}- T_{1}) = \eta _{T}c_{p(\mathrm{gases})}(T_{2^{'}}- T_{1}) (10/9)
:::

As the gases flow downstream through the turbine, they expand and their specific volume increases. The size of the blades (hence their weight and cost) must also increase, while the power they can extract decreases. Gases are often rejected at the outlet of a turbomachine with residual pressure because it is not economically viable to extract any more work from them.

(sec-10-4-4)=
### 10.4.4 Nozzle

:::{aside}
« When indeed two equally compressed fluids escape through two small equal orifices, their velocities are in inverse proportion to the square root of their densities. »

Louis Joseph Gay-Lussac, 1807 [[3](#ref-3)]
:::

:::{figure} ../images/fig-10-12.jpg
:label: fig-10-12
:enumerator: 10.12
:alt: Turbine of a gas generator. The photographed turbine, a Siemens sgt5, can accept an air and water flow rate of 690 kg s−1 (1521 lb/s). It delivers approximately 500 MW of shaft power.

Turbine of a gas generator. The photographed turbine, a Siemens sgt5, can accept an air and water flow rate of $690 kg s^{-1}(1521 lb/s)$. It delivers approximately $500 MW$ of shaft power.
:::

*Photo* CC-by-sa *Siemens Pressebild*

:::{figure} ../images/fig-10-13.jpg
:label: fig-10-13
:enumerator: 10.13
:alt: Schematic representation of a gas turbine.

Schematic representation of a gas turbine.
:::

*Diagram* CC-by-sa *Olivier Cleynen*

The *nozzle* is a simple conduit with no moving part (figures 10.14 and 10.15).

It allows the gas to expand, thereby accelerating towards the rear of the engine. It is this increase in gas velocity (difference between inlet and outlet velocities) that is the source of the thrust provided by an engine.

There is no heat or work input in the nozzle: the energy of the gas is conserved. The nozzle is the only element of the gas turbine engine for which the change in kinetic energy may not be neglected.

A quick return to equation 3/15 allows us to quantify the final speed of the gases as a function of the available pressure difference:

:::{math}
:label: eq-3-15-nozzle
q_{\mathrm{A}\rightarrow \mathrm{B}}+ w_{\mathrm{A}\rightarrow \mathrm{B}}= \Delta h + \Delta e_{\mathrm{mech}.}
:::

:::{math}
:label: eq-10-10
:enumerator: 10/10
h_{\mathrm{A}}+ \tfrac{1}{2} C_{\mathrm{A}}^{2}= h_{\mathrm{B}}+ \tfrac{1}{2} C_{\mathrm{B}}^{2}
:::

*Engineering Thermodynamics* by Olivier Cleynen

:::{figure} ../images/fig-10-14.jpg
:label: fig-10-14
:enumerator: 10.14
:alt: The nozzles of two General Electric f404 engines equipping a fighter aircraft. The geometry of the nozzle (not covered in this book) is programmed to adapt to the engine mass flow and whether or not afterburning is used.

The nozzles of two *General Electric* f404 engines equipping a fighter aircraft. The geometry of the nozzle (not covered in this book) is programmed to adapt to the engine mass flow and whether or not afterburning is used.
:::

*Photo* CC-by-sa *by Peng Chen*

:::{figure} ../images/fig-10-15.jpg
:label: fig-10-15
:enumerator: 10.15
:alt: Schematic representation of a nozzle.

Schematic representation of a nozzle.
:::

*Diagram* CC-0 *Olivier Cleynen*

In the case of an ideal nozzle, the expansion is isentropic, and we can relate the temperatures $T_{\mathrm{A}}$ and $T_{\mathrm{B}}$ just like in a turbine or a compressor, using the dreadful relations 4/36 to 4/38. Thus, knowing the inlet conditions $h_{\mathrm{A}}$ and $p_{\mathrm{A}}$, for a given outlet pressure $p_{\mathrm{B}}$ (atmospheric pressure), we can quantify the change in gas velocity:

:::{math}
C^{2}_{\mathrm{B}}- C^{2}_{\mathrm{A}}= -2 c_{p(\mathrm{gas})}(T_{\mathrm{B}}- T_{\mathrm{A}}) (10/11)
:::

Ideally, the nozzle expands the gases to ambient pressure and converts all the change in enthalpy of the gases into kinetic energy. In practice, of course, some of this energy is converted into heat due to friction. The efficiency of nozzles is quantified in a similar way to that of compressors and turbines, and is not studied in this book.

````{prf:example}
:label: ex-10-2
:enumerator: 10.2

For burnt gases, we have $c_{p (\mathrm{gases})}= 1150 J kg^{-1}K^{-1}, c_{v (\mathrm{gases})}= 823 J kg^{-1}K^{-1}, R_{\mathrm{gases}}= 327 J kg^{-1}K^{-1}$, and $\gamma _{\mathrm{gases}}= 1.333$. A nozzle is fed with a steady flow of combustion gases at $2 bar, 10 m s^{-1}$, and $400^{\circ}C (29 psi, 33 ft/s, 752 ^{\circ} F)$. At what speed can it accelerate these gases when they are rejected at 1 bar, if we neglect irreversibilities?

The process which would allow the highest ejection speed is an isentropic expansion; therefore, $T_{\mathrm{B}}= T_{\mathrm{A}}(\frac{p_{\mathrm{B}}}{p_{\mathrm{A}}} ) ^{\frac{\gamma-1}{\gamma}}= (400 + 273.15) (\frac{1}{2})^{\frac{0.333}{1.333}} = 566.1 K = 293^{\circ}C = 559 ^{\circ} F$. Such a process can be qualitatively represented on a $T - s$ diagram as follows:

````

:::{figure} ../images/art-p283-1.jpg
:alt: Illustration from the original text
:::

````{prf:example}

With equation 10/11, the outlet speed would therefore be:

:::{math}
C_{\mathrm{B}}= [-2 c_{p(\mathrm{gases})}(T_{\mathrm{B}}- T_{\mathrm{A}}) + C^{2}_{\mathrm{A}}]^{0.5}= [-2 \times 1150 \times (293 - 400) + 10^{2}]^{0.5} = 496.2 m s^{-1}= 1786 km/h = 1110 mph.
:::

In practice, the gases would never reach this speed. Indeed, a large part of the expansion takes place *downstream* of the nozzle, where it is very turbulent and therefore highly irreversible. This nevertheless does not inful ence the thrust generated by the nozzle, whose outlet orifcie pressure is in fact higher than atmospheric pressure. The speed calculation performed here remains a good thermodynamic “indicator” of the phenomena at play. A full description of the fluid dynamics of the nozzle is outside of the scope of this book.

In most cases, it is reasonable to consider that the kinetic energy of the gases at the outlet of the turbine (and therefore at the inlet of the nozzle) is negligible. The $10 m s^{-1}$ at A have no significant influence here.

````

Finally, we note that the *air intake* of aeronautical engines often serves as a diffuser: the mirror opposite of a nozzle in function. It thus slows down the air and increases its pressure. On supersonic aircraft, a well-designed inlet can generate a compression ratio of 2, with a corresponding temperature increase.

(sec-10-5)=
## 10.5 Gas Turbine Configurations

(sec-10-5-1)=
### 10.5.1 Advantages of gas turbines

Within the realm of *turbomachinery* (machines which transfer power between a fluid and a rotating shaft), we call *gas turbine* the complete internal-combustion, turbine-powered machine, and not merely the component of the same name. The word “gas” here refers to the working fluid, not to the fuel, which may be any kind of combustible liquid or gas. Gas turbines have two major advantages over piston engines:

• The power-to-weight ratio of turbomachines is approximately three times higher, since the number of moving parts is reduced, and their movement is very simple, allowing them to be lighter;

• In air propulsion, the working fluid can be used as a medium of propulsion itself. It is sufficient to let the air exit the turbine with a residual pressure and let it expand in a nozzle. This generates a thrust by reaction (equal to the mass flow rate multiplied by its speed): this is the working principle of the jet engine.

Thus, gas turbines are used in applications where high power is required with significant weight or space constraints.

:::{aside}
« As the steam turbine, without bringing an actual betterment of steam economy, has entered into the industry because of its constructive simplicity, so will it be with a gas turbine, which is constructively simpler than the gas motor, provided it will only exceed the steam motors in efficiency. »

Aurel Stodola, 1904, [[26](#ref-26), [27](#ref-27)]
:::

The major drawback of gas turbines is that their efficiency and responsiveness drop very quickly at low power levels. At partial load, the compression ratio and isentropic efficiency of turbines and compressors collapse, because it is hard to control fluid flow when the velocity of the rotor blades relative to stator blades is suboptimal. Gas turbines are therefore only useful in applications where high powers are required continuously. A gas turbine would be for example very poorly suited for road transport, because changes in power there are frequent and must be instantaneously acted on.

(sec-10-5-2)=
### 10.5.2 The gas generator

The heart of any gas turbine engine is called the *gas generator*. It contains only one shaft and one turbine (figure 10.16). This machine section has no use in itself, but the gases at its outlet, whose pressure is higher than at the inlet, can be used in a multitude of applications.

:::{figure} ../images/fig-10-16.svg
:label: fig-10-16
:enumerator: 10.16
:alt: A “gas generator” (schematic drawing and temperature-entropy diagram). This machine has no interest in itself but has many derived applications. One of them is the turbocharger, for which a piston engine acts as the combustion chamber, as described in §10.3.5.

A “gas generator” (schematic drawing and temperature-entropy diagram). This machine has no interest in itself but has many derived applications. One of them is the *turbocharger*, for which a piston engine acts as the combustion
:::

*Schematic* CC-by-sa *Olivier Cleynen* chamber, as described in §10.3.5. *Diagram* CC-0 *Olivier Cleynen*

In this configuration, the turbine extracts exactly enough power to power the compressor. At its outlet, the air is still compressed and can be used in a multitude of ways, as explored below.

(sec-10-5-3)=
### 10.5.3 Turbojet

The *turbojet* engine (figure 10.17) is the first application that has been made of gas generator. At the outlet of the turbine, the air is expanded in a nozzle, which accelerates it and provides net thrust. It is the working fluid itself that is used to generate thrust.

:::{figure} ../images/fig-10-17.svg
:label: fig-10-17
:enumerator: 10.17
:alt: Turbojet (schematic and temperature-entropy diagram). At the outlet of the turbine, the air is still pressurized; it is expanded in a nozzle in order to be accelerated.

Turbojet (schematic and temperature-entropy diagram). At the outlet of the turbine, the air is still pressurized; it is expanded in a nozzle in order to be accelerated.
:::

*Diagram* CC-by-sa *Olivier Cleynen Diagram* CC-0 *Olivier Cleynen*

Turbojet engines are extremely compact and mainly used in military aircraft.

(sec-10-5-4)=
### 10.5.4 Turboprop and turboshaft

Instead of using a nozzle as in a turbojet, it is possible to continue the expansion in the turbine until the gases reach atmospheric pressure. The power supplied by the turbine is then *greater* than the power supplied to the compressor.

This surplus work in the the engine shaft can then be used to power a propeller (in the case of a *turboprop*) or an external element such as a generator or a pump (in the case of a *turboshaft*), as shown in figure 10.18. The cycle of these machines is sometimes called *Brayton cycle*.

For a given engine mass flow, powering a propeller or the fan of a turbofan engine instead of merely expanding the gases in a nozzle increases thrust

:::{figure} ../images/fig-10-18.svg
:label: fig-10-18
:enumerator: 10.18
:alt: Schematics and temperature-entropy diagram of a turboprop (top) and a turboshaft engine (bottom). The power extracted by the turbine exceeds that absorbed by the compressor and is used to power the propeller or a generator.

Schematics and temperature-entropy diagram of a turboprop (top) and a turboshaft engine (bottom). The power extracted by the turbine exceeds that absorbed by the compressor and is used to power the propeller or a generator.
:::

*Schematics* CC-by-sa *Olivier Cleynen Diagram* CC-0 *Olivier Cleynen*

(this is quantified as the *propulsive efficiency*). The associated disadvantages are, of course, bulk and weight: the diameter of propellers and fans of modern engines often exceeds three meters, which translates into significant structural and mechanical constraints on the engine.

As for turboshaft engines, they find applications in helicopters, military ships, auxiliary electric generators, and gas turbine power plants. They are most often configured using the cycle modifications described in the following sections.

(sec-10-5-5)=
### 10.5.5 Turbofan

From a thermodynamic point of view, a *turbofan* (figure 10.19), is equivalent to a turboprop with a nacelle placed around it.

There are two separate air flows within a turbofan:

:::{figure} ../images/fig-10-19.jpg
:label: fig-10-19
:enumerator: 10.19
:alt: Schematic diagram of a turbofan. The engine’s thermodynamic core (A $\rightarrow$ E) mechanically powers the fan, which allows the bypass flow (A $\rightarrow$ G) to provide the majority of the thrust.

Schematic diagram of a turbofan. The engine’s thermodynamic core (A $\rightarrow$ E) mechanically powers the fan, which allows the bypass flow (A $\rightarrow$ G) to provide the majority of the thrust.
:::

*Diagram* CC-by-sa *Olivier Cleynen*

• the core flow is the flow through the thermodynamic engine. After combustion, it passes through a turbine whose power far exceeds that of the compressor. This excess power is transferred to the fan;

• the bypass flow is lightly compressed by the fan and directly expanded in the nozzle surrounding the hot core of the engine. It is never heated. It is this “cold” air which makes for the majority of the thrust. It can be shown that the greater the ratio of bypass to core air flow (the *bypass ratio*), and the more efficient the engine. The bypass ratio of modern engines is around $12$.

(sec-10-5-6)=
### 10.5.6 Free turbine and multiple turbines

Depending on the applications, various arrangements of turbines and compressors can be used.

In a *free turbine* (also called *free spool*) configuration, the mechanical power supplied by the engine is transmitted by a dedicated turbine (figure 10.20). This allows each of the two shafts to be maintained at different speeds.

Since the speed of the turbine/compressor shaft is not constrained by the load imposed on the free shaft, it can operate at speeds closer to its optimum point and accelerate more easily. This advantage compensates for the increased mechanical complexity in applications such as helicopter engines, where significant power changes are sometimes required.

In a configuration with *multiple spools*, the compressor and turbine are each divided into several parts, thus forming two co-axial systems incorporated one into the other (figure 10.21).

The high-pressure turbine drives the high-pressure compressor (high-speed spool), and the low-pressure turbine drives the low-pressure compressor (low-speed spool).

:::{figure} ../images/fig-10-20.svg
:label: fig-10-20
:enumerator: 10.20
:alt: Turboshaft engine with a free turbine (schematic and temperature-entropy diagram). The power supplied by the engine comes exclusively from the free turbine.

Turboshaft engine with a free turbine (schematic and temperature-entropy diagram). The power supplied by the engine comes exclusively from the free turbine.
:::

:::{figure} ../images/fig-10-21.svg
:label: fig-10-21
:enumerator: 10.21
:alt: Twin-spool turboshaft engine (schematic and temperature-entropy diagram). The two shafts rotate at different speeds.

Twin-spool turboshaft engine (schematic and temperature-entropy diagram). The two shafts rotate at different speeds.
:::

*Schematic* CC-by-sa *Olivier Cleynen Diagram* CC-0 *Olivier Cleynen*

*Schematic* CC-by-sa *Olivier Cleynen Diagram* CC-0 *Olivier Cleynen*

Just like for the free turbine, this arrangement allows each spool to operate at its own speed. Indeed, as the air pressure increases in the compressor, its density and temperature also increase. This configuration allows the blades to be operated at higher speeds, thus reducing their size.

(sec-10-6)=
## 10.6 Modification of Gas Turbine Cycles

(sec-10-6-1)=
### 10.6.1 Intercooling and reheat

It is sometimes desirable to increase the work ratio and specific power, even at the cost of a decrease in total efficiency, as mentioned in §10.2 above.

In order reduce the power absorbed by the compressor, *intercooling* is sometimes used. The compression is interrupted and the air is cooled before the compression process is completed (figure 10.22).

:::{figure} ../images/art-p289-1.jpg
:alt: Illustration from the original text
:::

:::{figure} ../images/fig-10-22.jpg
:label: fig-10-22
:enumerator: 10.22
:alt: A turboshaft generator with intercooler and reheat system (schematic and temperature-entropy diagram). Theintercoolercoolstheairinthemidstofcompression;whilethesecondcombustion chamber reheats the gases it in the midst of the expansion. The two modifications are independent of each other and each can be installed alone.

A turboshaft generator with intercooler and reheat system (schematic and temperature-entropy diagram). The intercooler cools the air in the midst of compression;while the second combustion chamber reheats the gases it in the midst of the expansion. The two modifications are independent of each other and each can be installed alone.
:::

*Schematic* CC-by-sa *Olivier Cleynen Diagram* CC-0 *Olivier Cleynen*

The compression of a gas between two given pressures imposes a *ratio* between the initial and final temperatures (4/36). On the other hand, the power required to compress a gas between these two pressures depends on the *difference* between these two temperatures (10/6). Therefore, the lower the initial temperature, and the lower the power required to reach a given pressure.

In the same vein, we can increase the specific power supplied by the turbine by carrying out a second combustion with the gases before the end of the expansion: this is called *reheat*. The process is similar to the reheating of steam in steam power plants (§9.4.4 p. 256).

It will not have escaped the student that the efficiency is inevitably reduced by the use of intercooling. Indeed, the combustion chamber must supply more heat, at a lower average temperature. This reduction in efficiency will be balanced against the reduction in the size of the compressor (usually the largest component of an engine) and the increase in specific power. Intercooling and reheat are typical of machines where the power-to-size ratio must be maximized.

In order to partially offset the loss of efficiency in stationary engines, it is sometimes possible to recover heat from the exhaust gases and use it to heat the air at the compressor outlet, thus relieving the combustion chamber. The heat exchanger is sometimes called *economizer* (figure 10.23); it is left to the student to trace the cycle followed on a temperature-entropy diagram and to find the conditions required for its operation.

:::{figure} ../images/fig-10-23.jpg
:label: fig-10-23
:enumerator: 10.23
:alt: Turboshaft generator with an intercooler and an economizer heat exchanger. The exhaust gases are redirected inside the engine to supply heat to the gases at the entrance of the combustion chamber. It is left to the student to determine the limits of the process.

Turboshaft generator with an intercooler and an economizer heat exchanger. The exhaust gases are redirected inside the engine to supply heat to the gases at the entrance of the combustion chamber. It is left to the student to determine the limits of the process.
:::

*Diagram* CC-by-sa *Olivier Cleynen*

(sec-10-6-2)=
### 10.6.2 Afterburning

*Afterburning* (or *reheat* in British English) is the addition of a second combustion phase in a jet engine, downstream of the turbine and upstream of the nozzle (figure 10.24). The principle is exactly the same as that of reheat: increase the specific thrust of the machine (at the expense of its efficiency).

Like reheat, afterburning alters the properties (specific volume in particular) of the gases and requires resizing of downstream components. The geometry of the nozzle is adapted according to whether the post-combustion is active or not. Adding an afterburner system to a turbojet engine merely requires the installation of burners and a system for varying the geometry of the

:::{figure} ../images/fig-10-24.svg
:label: fig-10-24
:enumerator: 10.24
:alt: Afterburner on a dual-flow turbojet engine (schematic and temperature-entropy diagram). States E and H are not necessarily merged in practice.

Afterburner on a dual-flow turbojet engine (schematic and temperature-entropy diagram). States E and H are not necessarily merged in practice.
:::

*Diagram 1* CC-by-sa*, Diagram 2* CC-0 *Olivier Cleynen* nozzle. The increase in weight is low compared to the increase in available power.

The outrageous loss of efficiency caused by the use of afterburners, as well as the deafening levels of noise and pollution they generate, limit their use to the military sector (especially on combat aircraft).

(sec-10-6-3)=
### 10.6.3 Turbine cooling

Because an increase in combustion temperature increases efficiency and specific power, engine designers are driven to develop technologies to maximize the temperature at the outlet of the combustion chamber (tet, for *turbine entry temperature*).

One of the used strategies is to cool the turbine with bleed air from the compressor (figure 10.25). The bleed air is passed through the turbine blades themselves, allowing for an increase in combustion temperature without risking damage to the blades. The most efficient and advanced cooling systems wrap the turbine blades with this cooler air. This allows, in modern engines, the tet temperature exceeds the melting temperature of the blades by more than $100^{\circ}C$, or $180 ^{\circ} F$!

Such turbine cooling comes at a significant cost. First, in a real engine, less work is recovered from the expansion of this bleed air than was required for its compression (in the limiting case where compression and expansion

:::{figure} ../images/fig-10-25.svg
:label: fig-10-25
:enumerator: 10.25
:alt: Turbine cooling using air taken from the compressor (schematic and temperature-entropy diagram). This air, at moderate temperature, bypasses the combustion chamber and never comes into contact with the fuel. Here the represented engine is a turboshaft, but turbine cooling can be used in any configuration.

Turbine cooling using air taken from the compressor (schematic and temperature-entropy diagram). This air, at moderate temperature, bypasses the combustion chamber and never comes into contact with the fuel. Here the represented engine is a turboshaft, but turbine cooling can be used in any configuration.
:::

*Schematic* CC-by-sa *Olivier Cleynen Diagram* CC-0 *Olivier Cleynen* are isentropic, this energy cost is zero). The circulation of this air therefore represents a burden that must be offset by the increase in efficiency it generates. Secondly, the compressor and the turbine must be oversized to accommodate a larger air flow.

Turbine cooling is a major research area in aeronautical propulsion. Techniques from a handful of fields (materials, fluid mechanics, mechanical design, combustion chemistry) are combined there in order to improve the thermodynamics of the engines.

On twin-engine aircraft qualified for etops flights, each engine must be able to alone maintain the aircraft flying while supplying many systems (pressurization, de-icing, heating, electrical and pneumatic generation) for several hours with demonstrated reliability.

:::{figure} ../images/fig-10-26.jpg
:label: fig-10-26
:enumerator: 10.26
:alt: Thermodynamic circuit of a modern turbofan engine. The machine combines multiple spools, mechanical and pneumatic power extractions, compressor bleeds for turbine cooling, and two main air flows. It is left to the student to trace the cycle on a temperature-entropy diagram.

Thermodynamic circuit of a modern turbofan engine. The machine combines multiple spools, mechanical and pneumatic power extractions, compressor bleeds for turbine cooling, and two main air flows. It is left to the student to trace the cycle on a temperature-entropy diagram.
:::

::::{admonition} A Bit of History
:class: note
:label: hist-10-13

**The Napier Nomad**

At the end of the Second World War, the British government issued a call for tenders for the development of a highly efficient, $6000 hp$ aeronautical engine, in order to foster the development of military and civilian aircraft. The British engine manufacturer Napier & Son then carried out research that led to the development of a curious and remarkable device: the *Napier Nomad*.

Based on a twelve-cylinder two-stroke Diesel engine with direct injection, the *Nomad* also featured all the elements of a turboprop engine. In order to increase the pressure and temperature at which heat was supplied, the two units were mounted *in series*; however, in order to allow for a high efficiency at all speeds, each drove one of the two contra-rotating propellers (Figures 10.27 and 10.28). Finally, in order to achieve high powers and increase responsiveness throughout the flight envelope, an intercooler and reheat system were added. The result: an astonishing and extravagant mechanical-thermal assembly seemingly produced by the out-of-control fantasy of thermodynamic engineers on a quest for efficiency.

:::{figure} ../images/fig-10-27.jpg
:label: fig-10-27
:enumerator: 10.27
:alt: Schematic diagram of the thermodynamic circuit of the Napier Nomad I. The shafts of the turboshaft and of the Diesel engine each drove one propeller. However, the two units were mounted in series: the air first passed through the compressors, then through the cylinders, and finally through the turbine(s). The engine power, as was customary in 1950, was controlled using a single mechanical control lever!

Schematic diagram of the thermodynamic circuit of the Napier *Nomad I*. The shafts of the turboshaft and of the Diesel engine each drove one propeller. However, the two units were mounted in series: the air first passed through the compressors, then through the cylinders, and finally through the turbine(s). The engine power, as was customary in 1950, was controlled using a single mechanical control lever!
:::

*Diagram by users* $\cdot$ *Commons Tataroko-common, Aaa3-other & Nimbus227 (public domain)*

:::{figure} ../images/fig-10-28.png
:label: fig-10-28
:enumerator: 10.28
:alt: The prototype of the Napier Nomad I. The displacement was $40 L$ and the weight exceeded 2 tons.

The prototype of the *Napier Nomad I*. The displacement was $40 L$ and the weight exceeded 2 tons.
:::

*Images edited from photos (1 and 2)* CC-by-sa *by Nigel Ish*

Napier & Son rapidly corrected course: the second prototype of the engine, the *Nomad II*, was greatly simplified. The intercooling, reheat, and centrifugal supercharger were all abandoned (figure 10.29). The two large mechanical units, one with pistons and the other with a turbine, were now connected to the same propeller. Both elements were connected with an ingenious but complex continuously-variable mechanical and hydraulic reducer that allowed each unit to operate at its optimal speed.

In an enlightening paper from 1954 [[28](#ref-28)], the engine designers showed a very clear vision and design approach. According to them, a simple turbocharged Diesel engine could only benefit from turbocharging over a very narrow power range — outside of this range, the turbine power would be either in surplus (and therefore lost) or insufficient to power the compressor. A different arrangement, in which the propeller would be driven solely by the turbine (with the Diesel engine then only providing supercharging and heat supply) would be far too inefficient at low power and unnecessarily strain the Diesel engine at high power. The simple turboprop, unable to reach the high pressures and temperatures of a Diesel engine, would be too inefficient. Only in the chosen arrangement, called *Diesel turbo-compound*, could the cylinder engine and the turboprop unit both contribute at all power levels, each always running at its optimal speed.

:::{figure} ../images/fig-10-29.jpg
:label: fig-10-29
:enumerator: 10.29
:alt: Schematic diagram of the thermodynamic circuit of the Napier Nomad II. A variable-ratio mechanical-hydraulic reducer connected the two units, which now drove the same propeller.

Schematic diagram of the thermodynamic circuit of the *Napier Nomad II*. A variable-ratio mechanical-hydraulic reducer connected the two units, which now drove the same propeller.
:::

*Diagram by users* $\cdot$ *Commons Tataroko-common, Aaa3-other & Nimbus227 (public domain)*

The performance of the *Nomad II* was indeed impressive —with its efficiency of $40 \%$, it used a third less fuel than its contemporaries— but its commercial failure was brutal: the project was abandoned in 1955 without a single sale. The engine was terribly heavy (with over $1600 kg$ for $2 MW$, its power-to-weight ratio was three times lower than that of a turboprop), which erased a large part of the fuel savings it could have generated. Also, it was both too complex for regional aircraft and far too slow for jet airliners, and aircraft manufacturers were never interested.

The curious arrangement conceived by Napier & Son fell into obscurity but, sixty years later, it made a thunderous comeback in racing cars. In 2014, the International Automobile Federation, organizer of the Formula One races, sought to make it easier for new teams to join the sport, by limiting development expenses, increasing technological spin-offs applicable to the industry, and finding itself a (new-found) ecological conscience. The regulations were thus modified: turbocharging would be allowed, but the cars' fuel consumption was limited to $100 L/h$. Most importantly, engine manufacturers would be allowed to use the turbocharger to recover energy in the form of electricity, as well as, conversely, accelerate the turbo by reinvesting this electrical energy into it (figure 10.30). Thus, the engine efficiency (and therefore, given the regulatory consumption limit, its power) can be increased at all speeds without sacrificing responsiveness. The system is poetically named mgu-h, but one could say that it is the unexpected revenge of the Anglo-Saxon *turbo-compounding*!

:::{figure} ../images/fig-10-30.jpg
:label: fig-10-30
:enumerator: 10.30
:alt: Thermodynamic circuit of the air in a 2014 Formula 1 engine. The shaft of the compressor (left) is not connected to the six-cylinder engine (center block) or the car's wheels. However, an electric motor/generator (named mgu-h) allows for extraction or addition of electrical energy. During high power phases, the power of the turbine (right) is in surplus and can be used to charge onboard batteries or drive the wheels with an electric motor. During low power phases, the turbine power is in deficit and the turbo can be driven by the generator to maintain the compression ratio and increase responsiveness.

Thermodynamic circuit of the air in a 2014 Formula 1 engine. The shaft of the compressor (left) is not connected to the six-cylinder engine (center block) or the car's wheels. However, an electric motor/generator (named mgu-h) allows for extraction or addition of electrical energy. During high power phases, the power of the turbine (right) is in surplus and can be used to charge onboard batteries or drive the wheels with an electric motor. During low power phases, the turbine power is in deficit and the turbo can be driven by the generator to maintain the compression ratio and increase responsiveness.
:::

*Diagram* CC-by-sa *Olivier Cleynen*

::::

## Problems

```{exercise}
:label: prob-10-1
:enumerator: 10.1

**Knowledge Recap Questions 1. Why do piston engines allow for higher combustion temperatures than gas turbines? 2. What advantage does the Diesel cycle have over the Otto cycle? 3. Draw the cycle undergone by the air in a single-turbine turbojet on a pressure-volume diagram and on a temperature-entropy diagram, qualitatively (that is, without showing numerical values). 4. Why are two concentric spools (two shafts each connecting a compressor and a turbine) used in some gas turbines? 5. Draw the cycle undergone by the air in an intercooled turboshaft engine with an economizer heat exchanger (figure 10.23) on a temperature-entropy diagram, qualitatively.**

```

```{exercise}
:label: prob-10-2
:enumerator: 10.2

**Gasoline Engine We propose to study the basic operation of the piston/cylinder engine of a private plane (figure 10.31). The engine is referred to as a “gasoline engine” and is based on the theoretical Otto cycle. • At the beginning of the cycle, the air is at $21^{\circ}C$ and $1 bar (70 ^{\circ} F$ and $14.5 psi)$; • The specific heat supplied during each cycle in cruise flight is $500 kJ kg^{-1}$; *Engine photo* CC-by-sa *by Commons User:FlugKerl2; Aircraft photo* CC-by-sa *by Commons User:Airman7474.* • The compression ratio $\varepsilon \equiv \frac{V_{\max}}{V_{\min}}$ is $7$. In this study, we consider that compression and expansion are isentropic and that heat addition and rejection occur at constant volume. 1. Draw the cycle followed on a pressure-volume or temperature-entropy diagram, qualitatively, indicating all heat and work transfers. 2. What are the air temperatures at the beginning and at the end of combustion? 3. What is the amount of heat rejected during cooling? 4. What is the efficiency of this theoretical engine cycle? 5. In practice, the process undergone by the air is very different from the cycle described by Otto. Propose two reasons explaining this. 6. It is observed that when the aircraft gains altitude, the power that the engine can provide decreases significantly. What modification can be made to the engine to compensate for this?**

:::{admonition} Answer
:class: dropdown

1) See figure 10.3 p. 273;
$(24)/3T6^{\mathrm{B}}) \mathrm{a}=\mathrm{nd} TT_{\mathrm{CA}}(=$^{\frac{v_{\mathrm{A}}}{v_{\mathrm{B}}}}$ \frac{q)_{\mathrm{co}}^{\gamma _{\mathrm{maibru}}-_{\mathrm{st}}1_{\mathrm{ion}}}}{c_{v (\mathrm{gaz})}} =+ \frac{c6_{v (}4_{\mathrm{air}}0_{)}}{c_{v (\mathrm{gaz})}}.T6_{\mathrm{B}}K==116366.37.K5^{\circ}=C 893.3^{\circ}C = 1640 ^{\circ} F$;
3) $T_{\mathrm{D}}= 610.16 K = 337^{\circ}C = 638.6 ^{\circ} F$ (equation 4/36) so
$q_{\mathrm{D}\rightarrow \mathrm{A}}= c_{v (\mathrm{gaz})}(T_{\mathrm{D}}- T_{\mathrm{A}}) = -260.1 kJ kg^{-1}$;
$4)\eta _{\mathrm{engine}}= \frac{q_{\mathrm{net}}}{q_{\mathrm{in}}} = 47.99\%(\mathrm{purely theoretical value},$
since compressions and expansions are reversible: in practice, expect around $35 \%)$; 5) See §10.3.4 p. 276; 6)Power decreases since the air density of the atmosphere decreases with altitude. In order to increase $m_{\mathrm{air}}$, one can, for example, install a turbocharging system (see §10.3.5) as shown in figure 10.31.

:::
```

   :::{figure} ../images/fig-10-31.svg
   :label: fig-10-31
   :enumerator: 10.31
   :alt: The six-cylinder gasoline fuel injection Continental io-550, in production since 1983. It equips among others the Cirrus sr22 aircraft. This
   
   The $300 hp$ six-cylinder gasoline fuel injection Continental io-550, in production since 1983. It equips among others the Cirrus sr22 aircraft. This photo shows the turbocharged version of the engine, with the intercooler visible in the top left corner.
   :::

```{exercise}
:label: prob-10-3
:enumerator: 10.3

**Diesel Engine A piston-cylinder engine used to propel a ship (figure 10.32) is turbocharged by a turbo that increases the pressure and temperature of the intake air using energy extracted from the exhaust gases (the turbocharger is a component that does not require any external input of energy in the form of work or heat, see §10.3.5 p. 276). The engine has the following operating characteristics: • the air admitted to the cylinders is at $115^{\circ}C$ and $3 bar (239 ^{\circ} F$ and $45.3 psi$; • the specific heat supplied each cycle is $1250 kJ kg^{-1}$; • the compression ratio $\varepsilon \equiv \frac{V_{\max}}{V_{\min}}$ is $17$. We consider the optimal operating case,thatis,following the Diesel cycle, according to the following characteristics: • isentropic compression and expansion; • combustion at constant pressure; • heat rejection at constant volume. 1. Draw the thermodynamic cycle undergone by the air on a pressure-volume or temperature-entropy diagram, qualitatively, indicating all heat and work transfers. 2. What is the air temperature at the end of the compression? *Photos 1 and 2* CC-by-sa *by Hervé Cozanet***

:::{admonition} Answer
:class: dropdown

.3**
2) $T_{\mathrm{B}}= 1205.5 K = 932.4^{\circ}C = 1710.2 ^{\circ} F$ (equation 4/36);
$3) T_{\mathrm{C}}= \frac{q_{\mathrm{combustion}}}{c_{p(\mathrm{gases})}} + \frac{c_{p(\mathrm{air})}}{c_{p(\mathrm{gases})}} T_{\mathrm{B}}= 2140.5K = 1867.3^{\circ}C = 3393.2 ^{\circ} F$;
4) $p_{\mathrm{C}}= p_{\mathrm{B}}= 158.4 bar = 2297.4 psi$;
$5) \mathrm{Using} \mathrm{equation} 4/36, \frac{T_{\mathrm{D}}}{T_{\mathrm{C}}} = (\frac{v_{\mathrm{D}}}{v_{\mathrm{C}}})^{\gamma _{\mathrm{gases}}-1}= (\frac{v_{\mathrm{A}}}{v_{\mathrm{B}}} \frac{v_{\mathrm{B}}}{v_{\mathrm{C}}})^{\gamma _{\mathrm{gases}}-1}= [\varepsilon \frac{R_{\mathrm{air}}}{R_{\mathrm{gases}}} \frac{T_{\mathrm{B}}}{T_{\mathrm{C}}}] \mathrm{Therefore} T_{\mathrm{D}}= \gamma _{\mathrm{gases}}-1 1053.6 K = 780.4^{\circ}C = 1436.8 ^{\circ} F$ (note that these
gases will still need to power the turbocharger’s turbine before being ejected into the atmosphere);
$6) \eta _{\mathrm{engine}}= \frac{q_{\mathrm{net}}}{q_{\mathrm{in}}} = 56.19\% (\mathrm{close} \mathrm{to} \mathrm{reality} \mathrm{since}$
these engines are very slow); 7) See sections §10.3.3 p. 274 and §10.3.4 p. 276.

:::
```

   :::{figure} ../images/fig-10-32.svg
   :label: fig-10-32
   :enumerator: 10.32
   :alt: The two Diesel engines of a oil tanker: a six-cylinder generator (top) and a seven-cylinder propulsion engine (bottom).
   
   The two Diesel engines of a $290.000 t$ oil tanker: a six-cylinder $1100 kW$ generator (top) and a seven-cylinder $25 MW$ propulsion engine (bottom).
   :::

3. What is the gas temperature at the end of the combustion?

4. What is the maximum pressure reached in the engine?

5. What is the temperature at the end of the expansion?

6. What is the engine cycle efficiency?

7. It is easy to show that at the same compression ratio, a Diesel cycle is less efficient than a so-called “gasoline”cycle(Otto cycle). Why is it used nevertheless?

```{exercise}
:label: prob-10-4
:enumerator: 10.4

**Turboprop Engine A regional airliner is powered by two turboprop engines (figure 10.34). In each of them, a single turbine drives an axial compressor, as well as the propeller through a gearbox (figure 10.33). During cruise, the air flow within the engine is $12.3 lb/s (5.6 kg s^{-1})$, and the circuit is as follows: • Air at ambient pressure and temperature $(7.98 psi$ and $23 ^{\circ} F$, or 0.55 bar and $-5^{\circ}C)$ is admitted into the compressor; • The compressor raises the air pressure to $110.2 psi (7.6 bar)$ with an isentropic efficiency of $80 \%$; • The air is then heated in the combustion chamber to $2400 ^{\circ} F (1315^{\circ}C)$; • The combustion gases are then expanded in the turbine and ejected into the atmosphere; the turbine has an isentropic efficiency of $80 \%$. The turbine drives the compressor (through a shaft with negligible losses) and the propeller (through a transmission box with an efficiency of $83 \%)$. We want to quantify the shaft power actually received by the propeller during flight. 1. Draw the cycle undergone by the air on a temperature-entropy diagram, qualitatively. 2. What is the compressor outlet temperature? 3. What is the turbine outlet temperature? 4. What is the power supplied to the propeller? *Diagram* CC-by-sa *by Olivier Cleynen* In order to de-ice the wings, a small gas bleed is carried out in the compressor. The extraction flow rate is $0.22 lb/s (0.1 kg s^{-1})$, and the air temperature is $392 ^{\circ} F (200^{\circ}C)$. 5. Propose and quantify a modification to the engine operation so that it may supply the propeller with the same power. *Engine photo derived from a photo* CC-by *by Flickr User:cliff1066; Aircraft photo* CC-by-sa *by Flickr User:Björn***

:::{admonition} Answer
:class: dropdown

1) See figure 3.17 p. 78;
2) $T_{\mathrm{B}}= 642.8 K = 369.6^{\circ}C = 697.4 ^{\circ} F$ (4/37 & 10/6);
3) $T_{\mathrm{D}}= 976.9 K = 703.8^{\circ}C = 1298.8 ^{\circ} F$ (4/37 &
10/9);
$4)\dot{W}_{\mathrm{propellers}}= -m\dot{\eta} _{\mathrm{transmission}}(w_{\mathrm{turbine}}+ w_{\mathrm{compressor}}) = +1.517 MW$ (with a thermal efficiency before transmission of $27.6 \%$, a value slightly lower than reality); 5) One possibility: increase$\dot{m}_{\mathrm{engine} \mathrm{air}}$ without modifying the temperatures. Then,$\dot{m}_{\mathrm{inlet} \mathrm{engine} 2}= 12.729 lb/s = 5.774 kg s^{-1}(+0.383 lb/s$ or
$+0.174 kg s^{-1})$.

:::
```

   :::{figure} ../images/fig-10-33.jpg
   :label: fig-10-33
   :enumerator: 10.33
   :alt: Internal arrangement of a turboprop.
   
   Internal arrangement of a turboprop.
   :::

   :::{figure} ../images/fig-10-34.png
   :label: fig-10-34
   :enumerator: 10.34
   :alt: A Pratt & Whitney Canada pwc123 turboprop engine powering a Bombardier Dash 8. Thepwc123 is configured with three concentric rotating assemblies
   
   A Pratt & Whitney Canada pwc123 turboprop engine powering a Bombardier*Dash 8*. Thepwc123 is configured with three concentric rotating assemblies, with the engine shaft powered by a free turbine, but its operation principle remains similar to that described in figure 10.33.
   :::

```{exercise}
:label: prob-10-5
:enumerator: 10.5

**Modification of a Turbojet A turbojet operates with a single engine spool (single compressor and single turbine). Its operating characteristics are as follows: • Air flow rate: $4 kg s^{-1}$ • Atmospheric temperature: $283 K$ • Atmospheric pressure: $0.969 kg_{f}/cm^{2}(0.95 bar)$ • Pressure ratio $\frac{p_{\max.}}{p_{\min.}}$: $25$ • Maximum temperature: $1300 K$ • Isentropic efficiencies of compressor and turbine: $85 \%$ We are looking to quantify its performance before it is modified. 1. Represent the components of the turbojet and the thermodynamic cycle undergone by the air on a temperature-entropy or pressure-volume diagram. 2. What is the pressure available at the turbine outlet? 3. What speed would the gases reach at the nozzle outlet if the expansion were isentropic? *Photo derived from a photo* CC-by *by Greg Goebel* The team of engineers in charge of designing the components proposes to modify the engine by using two spools instead of one (figure 10.35). The rotating assembly closest to the center of the engine can operate at higher speeds, increasing the isentropic efficiency of the components: • Isentropic efficiency of the low-pressure compressor and turbine (lp spool): $85 \%$ (pressure ratio: $2)$ • Isentropic efficiency of the high-pressure compressor and turbine (hp spool): $90 \%$ (pressure ratio: $12.5)$ All other operating characteristics of the engine remain unchanged. 4. What is the new available pressure at the turbine outlet? 5. What is the new theoretical exhaust gas velocity?**

:::{admonition} Answer
:class: dropdown

.5**
1) See figure 10.17 p. 286;
2) $T_{\mathrm{B}}= 785.2 K$, thus $T_{\mathrm{D}}= 861.1 K$ and $T_{\mathrm{D}^{'}}= 783.6 K$: $p_{\mathrm{D}}= 3.91 kg_{f}/cm^{2}= 3.13 bar$;
3) Neglecting $C_{\mathrm{D}}$, and with complete and reversible
expansion, $C_{\mathrm{E}}= 714.3 m s^{-1}$ (the same remarks as
in example 10.2 p. 283 apply here);
4)Thetemperatureatthestartofcombustiondrops
to $T_{3}= 774.2 K$, the temperature at the turbine outlet is $T_{6}= 870.7 K$, and thus the pressure at the nozzle inlet rises to $p_{6}= 4.776 kg_{f}/cm^{2}= 4.684 bar$;
5) Cover your ears: $C_{7}= 811.3 m s^{-1}$ (the same
remarks apply here as well).

:::
```

   :::{figure} ../images/fig-10-35.jpg
   :label: fig-10-35
   :enumerator: 10.35
   :alt: A turbojet with twin spools Pratt & Whitney j52 (or jt8a), built in units. It still equips the ea-6b Prowler.
   
   A turbojet with twin spools Pratt & Whitney j52 (or jt8a), built in $4500$ units. It still equips the ea-6b *Prowler*.
   :::

```{exercise}
:label: prob-10-6
:enumerator: 10.6

**Intercooled Turboshaft You are tasked by a small company to develop an engine that will be used to generate electricity in a factory. It is decided to base the engine on a turbofan jet engine from a retired commercial aircraft: it is a venerable General Electric cf6 (figures 10.36 and 10.37). The turbofan engine has two concentric spools: • The low-pressure spool connects the fan, a compressor section called the *booster*, and the low-pressure turbine; • The high-pressure spool connects the rest of the compressor to the high-pressure turbine. The turbofan engine has the following properties: Maximum pressure ratio: $29.3$ Booster pressure ratio: $1.2$ Fan pressure ratio: $1.2$ Maximum temperature: $1300^{\circ}C$ Isentropic efficiency of compressors: $85 \%$ *Diagram public domain U.S. FAA Diagram* CC-by-sa *Olivier Cleynen* Isentropic efficiency of turbines: $85 \%$ Exhaust gas discharge pressure: 1.1 bar In order to convert the turbofan into a turboshaft engine, you have the nacelle and the fan removed, and mechanically connect the low-pressure spool to the generator (figure 10.38). The turboshaft engine is started at atmospheric conditions of 1 bar and $18^{\circ}C$. At full throttle, it uses an air flow rate of $80 kg s^{-1}$. 1. Draw the thermodynamic cycle undergone by the air on a pressure-volume diagram, qualitatively. 2. What is the net power delivered by the machine? 3. What is its work ratio? 4. What is its efficiency? The client company receives your engine but wishes to increase its power. Since the engine is already operating at full capacity, you are unable to increase either the air mass flow rate or the combustion temperature. In order to increase the power,you install an intercooling system (figure 10.38). The air compression is interrupted at a pressure of 7 bar; the air is led into a large heat exchanger where it is cooled at constant pressure. Once its temperature has dropped back to $40^{\circ}C$, compression resumes in the compressor, which has not been modified.**

:::{admonition} Answer
:class: dropdown

.6**
$2)\dot{W}_{\mathrm{net}}=\dot{mc}_{p(\mathrm{gases})}(T_{\mathrm{D}}-T_{\mathrm{C}}) + c_{p(\mathrm{air})}(T_{\mathrm{B}}-T_{\mathrm{A}}) = -3.536 MW$ (approximately $3400 hp$, not too bad
for a machine first run in 1971... even after 15
years of service hung under a wing, a cf6 still sells
for several million euros);
3) $M_{w1}= 38.2 \%$;
4) $\eta _{1}= 31.49 \%$;
$6)\dot{W}_{\mathrm{net}2}= -3.325 MW$, that is a remarkable increase of $31 \%$;
7) $M_{w1}= 50 \%$, an increase of $+11.8 pt$;
8) Power increases by $98.8 kJ kg^{-1}$, while consumption increases by $332.6 kJ kg^{-1}$, resulting in
a marginal efficiency of $29.7 \%$. The overall efficiency decreases to $\eta _{2}= 31.04 \%$, only $-0.5 pt$...
an interesting compromise!
*Engineering Thermodynamics* by Olivier Cleynen
303
Appendix
**A1 Steam Tables 305 A2 Gauge Pressure and Real Pressure 314 A3 Additive Quantities 315 A4 State Quantities and Process Quantities 316 A5 Conversion of Units to SI 317 A6 Notation 319 A7 Mental Health For the Engineering Student 320 A8 Errata & Change Log 321 A9 Contributors 322 A10 Reusing This Book 323 A11 Citing This Book 324**
304
*Engineering Thermodynamics* by Olivier Cleynen

:::
```

   :::{figure} ../images/fig-10-36.jpg
   :label: fig-10-36
   :enumerator: 10.36
   :alt: Cutaway diagram of a General Electric cf6-6. The engine propelled all major long-haul aircraft families of the 1970s and 1980s.
   
   Cutaway diagram of a *General Electric* cf6-6. The engine propelled all major long-haul aircraft families of the 1970s and 1980s.
   :::

   :::{figure} ../images/fig-10-37.jpg
   :label: fig-10-37
   :enumerator: 10.37
   :alt: Schematic diagram of the arrangement of the General Electric cf6.
   
   Schematic diagram of the arrangement of the *General Electric* cf6.
   :::

5. Draw the new thermodynamic cycle on the pressure-volume diagram above, qualitatively.

6. What is the increase in net power?

7. What is the new work ratio?

8. What is the new efficiency?

   :::{figure} ../images/fig-10-38.jpg
   :label: fig-10-38
   :enumerator: 10.38
   :alt: Top: schematic diagram of a turboshaft based on the cf6 from which the fan has been removed. Bottom: the same turboshaft engine modified by
   
   Top: schematic diagram of a turboshaft based on the cf6 from which the fan has been removed. Bottom: the same turboshaft engine modified by the addition of an intercooling system.
   :::

*Diagrams* CC-by-sa *Olivier Cleynen*
