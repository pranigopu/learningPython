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

# Initialising the shape of the Turtle object
player.shape("tiger1.gif")

# Making a list of frames, using the registered shapes
player.frames = ["tiger1.gif", "tiger2.gif"]
player.frame = 0
# Here, frame will actually by an index for an element in frames.
# This will simply reference to different shapes more flexible.

def animate():
    player.frame += 1
    player.frame %= len(player.frames)
    # This will make sure the index doesn't exceed the list's upper limit.
    
    # Assigning the shape using the list and index
    player.shape(player.frames[player.frame])

    # Setting timer
    window.ontimer(animate, 500)
    # This becomes like a recursive call.

animate()
# Calling the function once is enough, because it recursively calls itself continuously

while True:
    window.update()

window.mainloop()