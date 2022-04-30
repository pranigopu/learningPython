# This method will make the program flexible.
# You will be able to use any number of frames, and the program will still work.
import turtle

window = turtle.Screen()
window.title("Animation Demo")
window.bgcolor("white")
player = turtle.Turtle()

# Registering images into the Screen object, window
window.register_shape("tiger1.gif")
window.register_shape("tiger2.gif")

class Player(turtle.Turtle):
# Here, the class turtle.Turtle is the parent.
# This is how inheritance is done in Python.

    # Definiting the initialising function i.e. the class constructor i.e. the method that, when called, will instantiate the class i.e. create an object of the class, and initialise the created object
    # In Python, this method, when defined, is denoted as __init__(self)
    # It may or may not have arguments.
    # When called, it is denoted by the class name, followed by parantheses.
    # Every class that can be intantiated as an object has this method.
    def __init__(self):
    # It is important to put "self" in the argument space, if you are not accepting any arguments.
        turtle.Turtle.__init__(self)
        # Instantiating the parent class as a part of the child class

        # Initialising the attributes
        self.penup()
        # The penup attribute indicates whether the lines of the motion of the object will be shown or not.
        # If this method is called, then the "pen" is "raised" i.e. the current object's motion will not be visibly traced.

        self.shape("tiger1.gif")
        self.frames = ["tiger1.gif", "tiger2.gif"]
        self.frame = 0

        # self here refers to the current object i.e. the object calling this constructor i.e. the object being created.
        # It is similar to the "this" keyword in Java.

    # Defining the animate method in the class, i.e. as a method callable by a Player class object.
    def animate(self):
    # It is important to put "self" in the argument space, if you are not accepting any arguments.
        self.frame += 1
        self.frame %= len(self.frames)
        # This will make sure the index doesn't exceed the list's upper limit.
        
        # Assigning the shape using the list and index
        self.shape(self.frames[self.frame])

        # Setting timer
        window.ontimer(self.animate, 500)
        # This becomes like a recursive call.

player1 = Player()
player1.goto(100, 0)
player1.animate()

player2 = Player()
player2.goto(-100, 0)
player2.animate()

while True:
    window.update()

window.mainloop()