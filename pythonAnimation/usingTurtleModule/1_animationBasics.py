import turtle
import time

window = turtle.Screen()
# window is an object of the class Screen, which is available in the turtle module.
window.title("Animation Demo")
window.bgcolor("black")
player = turtle.Turtle()
# player is an object of the class Turtle, which is available in the turtle module.
while True:
    player.shape("circle")
    player.color("red")
    time.sleep(0.5)
    # time.sleep() is a method that pauses the program for a given amount of seconds.
    
    player.shape("square")
    player.color("orange")
    time.sleep(0.5)
    
    player.shape("triangle")
    player.color("white")
    time.sleep(0.5)
    
    player.shape("arrow")
    player.color("green")
    time.sleep(0.5)
    
    player.shape("turtle")
    player.color("blue")
    time.sleep(0.5)
    
    player.shape("classic")
    player.color("magenta")
    time.sleep(0.5)
    # The above shapes are the five available shapes in the Turtle class.

window.mainloop()
# The mainloop() method is called by a Screen object.
# Not adding window.mainloop() produced no output.
# This method keeps the window open, and not using it means the program ends without the window opening.
# Running it n number of times opens n windows.
# This method needs to be put at the end of the code for the window, so that relevant the code is executed and shown.