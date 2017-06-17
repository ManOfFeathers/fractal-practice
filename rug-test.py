from rug import Rug
from tkinter import *
import math

width = 729
height = 729

root = Tk()

c = Canvas(root, width = width, height = height, bg = "black")
c.pack(expand = YES, fill = BOTH)

grid = Rug(root, c, left = 0, top = 0, width = width, height = height,
           grid_color = "white", square_color = "black")

##grid.draw(0, height, 0, width)
##c.update()

grid.next_draw(0, height, 0, width)
c.update()
