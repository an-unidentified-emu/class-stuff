#import "@preview/postercise:0.1.0": *

#import themes.boxes: *

#set page(width: 48in, height: 36in)
#set text(size: 43pt)

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
    authors: [Micah Mast],
  )
  #normal-box[
    = Introduction
    When measuring projectiles in the lab, air resistance is often neglected in the name of simplicity. However it has long been known that drag force does exist and it affects objects. The equation for drag is $accent(F, arrow)_D = -F_D accent(v, hat)$. The purpose of this lab is to determine whether a measured distance is close enough to a theoretical distance calculated with the inital velocity to be accurate in a controlled environment.
  ]
  #normal-box[
    = Methods
   To determine if air resistance causes a measureable difference in distance traveled an initial velocity is measured by a calibrated photogate. A theoretical distance is then calculated using the inital height and that velocity using kinematic equations. _Put equations here_ The distance traveled is then measured using carbon paper to mark the landing spot and a tape measure pulled between the leading edge of the landing mark and the spot directly below the spot where the ball is no longer accelerated by the launch apparatus. This is repeated at three angles. The time is also estimated using kinematic equations and measured by counting the frames in a video of the trial. 
  ]

  #focus-box[
    = Results
    #figure(image("TimeVelDist.svg", width: 100%))

  ]

  #normal-box[
    = Discussion
    This experiment shows that in the majority of cases, air resistance is negligable. 
  ]
  #normal-box()[
    = References
    #lorem(34)
  ]
]