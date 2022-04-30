import turtle
import time

window = turtle.Screen()
window.title("Animation Demo")
window.bgcolor("black")
player = turtle.Turtle()

def animate():
    player.shape("square")
    player.color("red")
    time.sleep(0.5)
    
    player.shape("triangle")
    player.color("blue")
    time.sleep(0.5)

i = 0
while True:
    i += 1
    print(i)
    animate()
window.mainloop()