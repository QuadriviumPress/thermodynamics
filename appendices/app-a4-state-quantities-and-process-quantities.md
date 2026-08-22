---
title: "A4. State Quantities and Process Quantities"
short_title: "Appendix A4"
label: app-a4-state-quantities-and-process-quantities
---

# A4. State Quantities and Process Quantities

316 Appendix A4

**Definition**

Thermodynamic quantities can be classified into the following categories:

• A quantity is called a *state quantity* if its value depends only on the current state of the system. Temperature $T$ is an example of a state quantity.

• A quantity is called a *path quantity* or if its value depends on the path taken. Heat transfer $Q$ and work $W$ are the only two path quantities used in this book.

Using the example provided by Rogers & Mayhew [[37](#ref-37)], one can illustrate the distinction as follows: a cyclist travels from A to B. Their altitude at the start $z_{\mathrm{A}}$ and at the end $z_{\mathrm{B}}$ are state quantities $(z$ being a *state function*), and we can quantify $\Delta z \equiv z_{\mathrm{B}}- z_{\mathrm{A}}$ without knowing anything about the route. However, the work $W_{\mathrm{A}\rightarrow \mathrm{B}}$ expended to go from A to B depends on the process: it will be larger, for example, if the route is longer or if there is wind. Quantifying $W$ (a *path function*) requires knowledge of all intermediate states between A and B.

Quantities are sometimes referred to as *variables*; state quantities are sometimes referred to as *physical properties*. Process quantities and functions are sometimes also called *transfer* or *path* quantities.

**Notation**

Infinitesimal changes in state quantities are denoted by the symbol $d$; these are *exact*

*differentials* and can be integrated by only knowing their initial and final values. For

example, for temperature $T$:

B

:::{math}
dT = \Delta T = T_{\mathrm{B}}- T_{\mathrm{A}} (A4/1)
:::

:::{math}
\int
:::

A

Infinitesimal transfers of path quantities are denoted by the symbol δ; these are *inexact*

*differentials* and their integral can only be quantified by knowing all states encountered

along the path. For example, for work $W$, one cannot write “$W_{\mathrm{B}}-W_{\mathrm{A}}$”, or “$\Delta W$”, but only:

B

:::{math}
δ W = W_{\mathrm{A}\rightarrow \mathrm{B}} (A4/2)
:::

:::{math}
\int
:::

A

This notation can be confusing, since it is $d$ and not δ that becomes $\Delta$ upon integration. It may also appear as a complicated way to avoid using partial derivatives. Clifford Truesdell [[36](#ref-36)] mischievously remarks that because of this notation, equation 8/1 on page 211 might make us believe that some types of differentials are larger than others... Although this notation is widely used in French literature (which is why it is adopted in this book, which is translated from French [[51](#ref-51)]), it must be recognized that one can fully cover the field of engineering thermodynamics [[37](#ref-37), [38](#ref-38)] or physical thermodynamics and its history [[36](#ref-36)] without ever having to use the symbol δ in the above sense.
