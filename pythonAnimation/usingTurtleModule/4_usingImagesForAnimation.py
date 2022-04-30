# You can register an image as a shape into a Screen object.
# The image should be in .gif format.
import turtle

window = turtle.Screen()
window.title("Animation Demo")
window.bgcolor("white")
player = turtle.Turtle()

# Registering images into the Screen object, window
window.register_shape("tiger1.gif")
window.register_shape("tiger2.gif")

player.shape("tiger1.gif")

def animate():
    if player.shape() == "tiger1.gif":
        player.shape("tiger2.gif")
    elif player.shape() == "tiger2.gif":
        player.shape("tiger1.gif")
    
    # Setting timer
    window.ontimer(animate, 500)
    # This becomes like a recursive call.

animate()
# Calling the function once is enough, because it recursively calls itself continuously

while True:
    window.update()

window.mainloop()