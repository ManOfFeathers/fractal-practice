from sierpinski import Triangle
from tkinter import *
import math

c = Canvas(width = 500, height = 500, bg = "red")
c.pack(expand= YES, fill = BOTH)

triangle = Triangle(c, left = 0, top = 0, width = 500, height = (500 * math.sqrt(3)) / 2,
                    objColor = "black", tremaColor = "white")

triangle.draw()
c.update()

for i in range(250):
    triangle.set_properties()
    c.update()
    triangle.shrink()
    c.update()
