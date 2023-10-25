import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)  # Set the drawing speed to the maximum (0)
bgcolor("black")

# Add "I Love You" message at the top of the heart
penup()
goto(0, 180)  # Adjust the Y-coordinate to move the text to the top
pendown()
color("pink")  # Change the font color to pink
write("I Love You", align="center", font=("Arial", 24, "normal"))
hideturtle()

# Draw the heart
for i in range(6000):
    goto(hearta(i) * 20, heartb(i) * 20)
    for j in range(5):
        color("#f73487")
        goto(hearta(i) * 20, heartb(i) * 20)

done()
