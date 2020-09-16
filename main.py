import random

import turtle 

kon = turtle.Turtle()
h =  turtle.Turtle()
colours=["red", "black", "white","yellow","cyan", ]




for g in range(169):  # antal repetasjoner

  #color=random.choice(colour)
  lenght=random.randint(-100,100,)
  vestre=random.randint(1,359) 
  colour = random.choice(colours)  # Henter frarver fra colors variabelen til turtle.
  h.forward(lenght)  # henter variabelen fra linje 11
  h.left(vestre) # det bestemer retnigen av turtle
  h.color(colour)  # Setter frave på turtle
