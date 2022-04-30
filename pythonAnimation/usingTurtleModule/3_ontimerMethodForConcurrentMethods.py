# The problem with the time.sleep() method is that it pauses the whole program.
# So, concurrent processes are not acheivable with this.
# Hence we use the turtle.ontimer() method.
# (Other modules may have equivalent or similar methods)

# The ontimer function is called using a Screen object, window in our case.
# Its syntax: screen_object.ontimer(function_name, milliseconds)
# It repeatedly calls the function with the name function_name, pausing for the given number of milliseconds.
# However, it does not pause the whole program.
import turtle

window = turtle.Screen()
window.title("Animation Demo")
window.bgcolor("black")
player = turtle.Turtle()

# Initialising the player object
player.shape("square")
player.color("red")

def animate():
    if player.shape() == "square":
        player.shape("triangle")
        player.color("blue")
    elif player.shape() == "triangle":
        player.shape("square")
        player.color("red")
    
    # Setting timer
    window.ontimer(animate, 500)
    # This becomes like a recursive call.

animate()
# Calling the function once is enough, because it recursively calls itself continuously

i = 0
while True:
    i += 1

    window.update()
    # The update() method makes sure that the screen shows the latest changes in the screen-related objects.

    print(i)

# Now, the numbers will imcrement simultaneously with the animation, and will not pause with the animation.
window.mainloop()