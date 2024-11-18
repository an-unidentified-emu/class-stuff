#set rect(
  width: 100%,
  height: 100%,
  inset: 4pt,
)
//https://www.britannica.com/science/friction
#set page(
  paper: "a4",
  number-align: center,
)

#show figure: set text(size: 10pt, rgb("#0029dd"))

#set align(center)
#set text(font: "FreeSans", size: 12pt)
#set text(top-edge: 0.7em, bottom-edge: -0.3em)
#set par(leading: 1.2em)
\ \ \ \ \ \ \
Friction\ Micah Mast\ Partners: Noah Sanderson, Carter Cashin\ Daniel King\ November 18, 2024 \ Physics Lab\ Eastern Mennonite University

#pagebreak()

#set align(left)
#set par(
  first-line-indent: 3em,
  spacing: 0.65em,
  justify: true,
)
== Introduction
Friction is a force encountered in almost all physics experiments. It is a "force that resists the sliding or rolling of one solid object over another" [1]. Friction is a macroscopic summation of many microscopic forces acting between two surfaces. Friction is proportional to the normal force on an object and can be expressed as $f = mu F_N$ where $f$ is the force of friction, $F_N$ is the normal force and $mu$ is the _coefficient of friction_. The purpose of this lab is to find the coefficient of friction between two pieces of wood.

== Methods
Accepted theory states that there are two different coefficients of friction, one for static friction, $f_s = mu_s F_N$ and one for kinetic friction $f_k = mu_k F_N$. To find these coefficients, A board was pulled across another board tangentally. The force required to move the board from a static start was measured as well as the force require to move it at a constant speed. This was done using a spring scale. These forces were measured for four different masses at an angle of zero, where the normal force is directly proportional to the mass times the force of gravity: $f = mu m g$, and up a slope of $7.89 degree$ where the friction force is $f = mu cos(theta) m g $.
== Results
#figure(image("flat-both.svg", width: 90%), caption: [
  Static and Kinetic Forces on a flat surface
])
#figure(image("angled-both.svg", width: 90%), caption: [
  Static and Kinetic Forces on an angle
])
#figure(image("histo.svg", width: 90%), caption: [
  Spread of Pull Force required to move 556.4 grams at $0 degree$
])
#figure(image("histo2.svg", width: 90%), caption: [
  Spread of Pull Force required to move 5556.4 grams at $0 degree$
])
#pagebreak()
== Discussion
The data shows that between the two pieces of wood on a flat plane, the coefficient of friction is $0.36 plus.minus 0.01$ for static friction and $0.22 plus.minus 0.02$ for kinetic. On an incline, the slope of the lines were $0.46$ and $0.32$ respectively, however, these are not the coefficients of friction because of the incline. To find the coefficients, the values are multipled by $cos(7.86 degree)$ to compensate for the angle leaving us with $0.45 + 0.043$ and $0.31 + 0.0219$. These numbers are very different, however, different scales were used to measure higher force values. If a linear regression is only applied to the smallest two masses, the new calculated coefficient is $0.39 +$ (do your math). This still shows a difference but the error is larger with only these points. The larger scales used for the heaviest masses were much less precise, potentially causing this error. 