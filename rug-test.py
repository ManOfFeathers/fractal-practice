#                 Sierpinski Carpet (AKA rug)
#
#  Programmed by Jean Flaherty and Griffin Myers (06-24-2017)
#
#  The means of implementing the functions from rug.py in a
#  TkInter canvas
#

from rug import Rug
from tkinter import *
import math

width = 729
height = 729

root = Tk()

c = Canvas(root, width = 727, height = 727, bg = "black")
c.pack(expand = YES, fill = BOTH)

grid = Rug(root, c, left = 0, top = 0, width = width, height = height,
           grid_color = "white", square_color = "black")

grid.draw(0, height, 0, width)
c.update()

##grid.next_draw(0, height, 0, width)
##c.update()


