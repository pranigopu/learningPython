import turtle

window = turtle.Screen()
window.title("Animation Demo")
window.bgcolor("white")
player = turtle.Turtle()

# Registering images into the Screen object, window
window.register_shape("tiger1.gif")
window.register_shape("tiger2.gif")

player.shape("tiger1.gif")
player.frame = 0
# frame is an attribute of the Turtle object that can be used to keep track of the current shape of the Turtle object.
# You cannot refer to an image with the frame, or assign an image to a frame directly.
# It is used similar to a counter or flag.

def animate():
    if player.frame == 0:
        player.shape("tiger1.gif")
        player.frame = 1
    elif player.frame == 1:
        player.shape("tiger2.gif")
        player.frame = 0
    
    # Setting timer
    window.ontimer(animate, 500)
    # This becomes like a recursive call.

animate()
# Calling the function once is enough, because it recursively calls itself continuously

while True:
    window.update()

window.mainloop()