#import "@preview/postercise:0.1.0": *

#import themes.boxes: *

#set page(width: 48in, height: 36in)
#set text(size: 43pt)

#show: theme.with(
  primary-color: rgb("#0c2513"), // Dark blue
  background-color: rgb("#c0c0c0"),
  accent-color: rgb("#7d7e8b"), // Yellow
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
    #lorem(50)
  ]
  #normal-box[
    = Methods
   #lorem(100)
  ]

  #focus-box[
    = Results
    #lorem(40)

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