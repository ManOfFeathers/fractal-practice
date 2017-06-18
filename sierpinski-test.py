from sierpinski import Triangle
from tkinter import *
import math

root = Tk()

c = Canvas(root, width = 500, height = 500, bg = "white")
c.pack(expand= YES, fill = BOTH)

triangle = Triangle(root, c, left = 0, top = 0, width = 500, height = 500,
                    obj_color = "black", trema_color = "white")

triangle.draw()
c.update()
