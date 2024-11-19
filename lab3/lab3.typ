#set rect(
  width: 100%,
  height: 100%,
  inset: 4pt,
)
//https://www.britannica.com/science/friction
#set page(
  paper: "a4",
  number-align: center,
  numbering: "1"
)

#show figure: set text(size: 10pt, rgb("#0029dd"))

#set align(center)
#set text(font: "FreeSans", size: 12pt)
#set text(top-edge: 0.7em, bottom-edge: -0.3em)
#set par(leading: 1.2em)
\ \ \ \ \ \
*Friction Force*\ \ Micah Mast\ Partners: Noah Sanderson, Carter Cashin\  Dr. Daniel King\ November 18, 2024 \ PHYS 253: Physics Laboratory\ School of Sciences, Engineering, Art and Nursing\ Eastern Mennonite University

#pagebreak()

#set align(left)
#set par(
  first-line-indent: 3em,
  spacing: 1.2em,
  justify: true,
)
== Introduction
Friction is a force encountered in almost all physics experiments. It is a "force that resists the sliding or rolling of one solid object over another" #cite(<zeidan_2019_friction>). Friction is a macroscopic summation of many microscopic forces acting between two surfaces. Friction is proportional to the normal force on an object and can be expressed as $F_f = mu F_N$ where $F_f$ is the force of friction, $F_N$ is the normal force and $mu$ is the _coefficient of friction_. The purpose of this lab is to find the coefficient of friction between two pieces of wood.

== Methods
Accepted theory states that there are two different coefficients of friction, one for static friction, $f_s = mu_s F_N$ and one for kinetic friction $f_k = mu_k F_N$. To find these coefficients, A board was pulled across another board tangentally. The force required to move the board from a static start was measured as well as the force require to move it at a constant speed. This was done using a spring scale. These forces were measured for four different masses at an angle of zero, where the normal force is directly proportional to the mass times the force of gravity: $F_f = mu m g$, and up a slope of $7.86 degree$ where the friction force is $F_f = mu F_N $. However, because neither the normal force nor the friction force can be measured directly, the force of gravity acting on the board is measured as well as the pulling force and their relative components are summed. This leaves us with $F_p - m g sin(theta) = mu cos(theta) m g$ where $F_f = F_p - m g sin(theta)$ and $F_N = cos(theta) m g$. By doing these transformations, it is possible to plot the normal force on the x axis and the friction force on the y axis, thereby permitting a linear regression to find the coefficient of friction. The angle was measured using trigonometry to assure an accurate angle with negligable error.
== Results
#figure(image("static-both.svg", width: 90%), caption: [
  Relation between Normal Force and Static Friction Force on a flat surface and a $7.86 degree$ angle
])
#figure(image("kinetic-both.svg", width: 90%), caption: [
  Relation between Normal Force and Kinetic Friction Force on a flat surface and a $7.86 degree$ angle
])
#figure(image("histo.svg", width: 90%), caption: [
  Spread of Pull Force required to move 556.4 grams at $0 degree$
])
#figure(image("histo2.svg", width: 90%), caption: [
  Spread of Pull Force required to move 5556.4 grams at $0 degree$
])
//#show figure: set text(size: 12pt, rgb("#000000"))
//#figure(table(columns: 4, align: auto, "Gravity Force", "Normal Force", "Pull Force", "Friction Force", "1.76", "1.76","2.91","2.91", "15.3","15.3","39.2","39.2" ))
//#show figure: set text(size: 10pt, rgb("#0029dd"))
#pagebreak()
== Discussion
The data shows that between the two pieces of wood on a flat plane, the coefficient of friction is $0.36 plus.minus 0.01$ for static friction and $0.22 plus.minus 0.02$ for kinetic. When friction force was measured on an incline, the coefficients were found to be $0.32 plus.minus 0.03$ and $0.19 plus.minus 0.03$ respectively. These are within error for each other showing that between two materials, there is an unchanging friction coefficient relating the normal force and the friction force.

This coefficient between two materials is different for static situations and kinetic ones. It must also be noted that this relates the normal force and and friction force, not the acting force of gravity and the pulling force. (For gravity and pulling force relations see Figures 5 and 6). However, the force of gravity and normal force are related. The normal force is the $Y$ component of $m g$ in this situation or $F_N = cos(theta) m g $ and friction force is related to the pulling force by $F_f = F_p - m g sin(theta)$. 

The histograms (Figures 3 and 4) are roughly normal demonstrating consistency of the relationship between pulling force and normal force and therefore between friction force and normal force. 

The coefficients found (0.34 static and 0.20 kinetic) align with standard values between two pieces of wood which fall between 0.25 and 0.5 for static friction #cite(<engineeringtoolbox_2004_friction>) and 0.2 for kinetic friction @coefficients. This experiment also aligns with Newtons second law as on a flat surface, the friction force is directly proportional to the pulling force which gives a net force of 0 which is what is expected as the acceleration in all the tests was 0. The net forces on the slope also sum to 0 as shown earlier with the relation of $F_N = cos(theta) m g $ and $F_f = F_p - m g sin(theta)$.

== Conclusion
The coefficient of friction between two materials is constant regardless of other forces applied to the objects. This is proved by the overlapping coefficients found when measuring on a slope of $7.86 degree$ and $0 degree$. The static and kinetic coefficients of friction between the two pieces of wood used are $0.34 plus.minus 0.018$ and $0.20 plus.minus 0.028$ respectively. To make this experiment more accurate and thorough, digital scales should be used, multiple angles should be measured as well as pulling the scale along a rail to prevent forces acting non-tangentally.

#pagebreak()

#bibliography("works.bib")

#pagebreak()
== Appendix - Additional Graphs
#figure(image("flat-both.svg", width: 90%), caption: [
  Static and Kinetic forces on a flat plane
])
#figure(image("angled-both.svg", width: 90%), caption: [
  Static and Kinetic forces on a $7.86 degree$ plane
])
#figure(image("angled-mod.svg", width: 90%), caption: [
  Static and Kinetic forces on a $7.86 degree$ plane. Same data used as Figure 6 but adjusted to Normal and Friction Force.
])