#
# cantor.py
# Programmed by Griffin Myers
# 7/8/2017
#

import numpy as np
from tkinter import *

root = Tk()

width = 600
height = 600

c = Canvas(root, width = width, height = height)
c.pack()

# make a few good points

def cantor(max_i, x_start, x_end, y):
    queue = [[(x_start,y),
            (x_end,y)]]
    mat_r = x_end - x_start 

    while queue:
        coord = queue.pop(0)
        c.create_line(coord[0][0],coord[0][1], coord[1][0],coord[1][1], width = 2, fill = "black")
        c.update()
        r = coord[1][0] - coord[0][0]
        coord1 = [(coord[0][0],coord[0][1] + 10),(coord[0][0] + (r / 3),coord[1][1] + 10)]
        coord2 = [(coord[1][0] - (r / 3),coord[0][1] + 10),(coord[1][0], coord[1][1] + 10)]
        queue.append(coord1)
        queue.append(coord2)             

cantor(4, 0, width, 2)
