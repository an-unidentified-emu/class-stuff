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
   #lorem(100)
  ]

  #focus-box[
    = Results
    #figure(image("start.svg", width: 100%))

  ]

  #normal-box[
    = Discussion
    #lorem(150)
  ]
  #normal-box()[
    = References
    #lorem(34)
  ]
]