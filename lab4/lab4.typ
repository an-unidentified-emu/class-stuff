#import "@preview/postercise:0.1.0": *

#import themes.boxes: *

#set page(width: 48in, height: 36in)
#set par(justify: true)
#set text(size: 42pt)

#show: theme.with(
  primary-color: rgb("#131246"), // Dark blue
  background-color: rgb("#c0c0c0"),
  accent-color: rgb("#ffffff"), // Yellow
  titletext-color: white,
  titletext-size: 2em,
)
#poster-content(
)[
  #poster-header(
    title: [Is Air Resistance Negligable in the Lab?],
    authors: [Micah Mast, Issac Greenleaf, Ben Huyard, Dylan Diener],
  )
  #normal-box[
    = Introduction
    When measuring projectiles in the lab, air resistance is often neglected in the name of simplicity. However it has long been known that drag force does exist and it affects objects. The equation for drag is $F_d = 1/2 rho u^2 c_d A $[1]. The purpose of this lab is to determine whether a measured distance is close enough to a theoretical distance calculated with the inital velocity to be accurate in a controlled environment.
  ]
  #normal-box[
    = Methods
   To determine if air resistance causes a measureable difference in distance traveled, an initial velocity is measured by a calibrated photogate. A theoretical distance is then calculated using the inital height and that velocity using kinematic equations. A second theoretical distance is also calculated using the measured time between launch and impact. The actual distance traveled is then measured using carbon paper to mark the landing spot and a tape measure pulled between the leading edge of the landing mark and the spot directly below the spot where the ball is no longer accelerated by the launch apparatus. Error is calculated using the standard deviation of the differences between measured distance and the mean theoretical distance. There is a shift of $n-2$ due to using two methods to calculate a theoretical distance.
    \ 
    #align(center, block[
    Error $= sqrt(sum(x_i - mu )^2 / (n-2))$
    #set text(size: 36pt)
    
    Where $x_i =$ difference between measured and theoretical and $mu$ is the mean difference between theoretical and measured])
  ]

  #focus-box[
    = Results
    #figure(image("TimeVelDist.svg", width: 100%))

  ]

  #normal-box[
    = Discussion
    This experiment shows that in a lab setting, air resistance is not negligable. At each angle measured, every measured value was consistently either above or below it's expected value. However, in many of the trials, the errorbars overlap, especially in the 30 degree and 60 degree trial. Due to the consistency mentioned earlier it seems probable that with more trials and therefore lower error, the 30 and 60 degree trials could likely reflect similar results to the 45 degree trials where air resistance is confidently non-negligable. Another way to improve this experiment would be to perform it at STP instead of an uncontrolled environment which would affect the drag coefficient [2]. The 45 degree trials were performed on a different day than the other two sets of trials so differences in temperature and air pressure could have affected the results in ways not refected in the graphs. These results also align with physics principals as it is known that air resistance does affect objects, this experiment simply shows that it is notable and non-negligable in a lab setting. 
  ]
  #normal-box()[
    = References
    #set par(hanging-indent: 80pt)
   Hall, N. (2022, July 28). Drag Equation. Glenn Research Center | NASA. https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-equation/

    tec-science. (2020, May 31). Drag coefficient (friction and pressure drag). Tec-Science. https://www.tec-science.com/mechanics/gases-and-liquids/drag-coefficient-friction-and-pressure-drag/

  ]
]