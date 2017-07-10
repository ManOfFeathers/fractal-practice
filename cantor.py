#  Cantor Set
# 
#  Programmed by Griffin Myers
#  7/8/2017
#
#  Functions:
#       cantor    -- infinitely draws lines with coordinates based on tuple variables
#

import numpy as np
from tkinter import *
from PIL import ImageGrab

root = Tk()

width = 600
height = 600

c = Canvas(root, width = width, height = height, bg = "white")
c.pack()

# make a few good points

def cantor(max_i, x_start, x_end, y):
    queue = [[(x_start,y),
            (x_end,y)]]
    mat_r = x_end - x_start 

    depth = 0
    while queue:
        coord = queue.pop(0)
        c.create_line(coord[0][0],coord[0][1], coord[1][0],coord[1][1], width = 2, fill = "black")
        c.update()
        r = coord[1][0] - coord[0][0]
        coord1 = [(coord[0][0],coord[0][1] + 10),(coord[0][0] + (r / 3),coord[1][1] + 10)]
        coord2 = [(coord[1][0] - (r / 3),coord[0][1] + 10),(coord[1][0], coord[1][1] + 10)]
        queue.append(coord1)
        queue.append(coord2)
        c.update()
##        c.after(1000)
        screenshot(c, "cantor_{}.gif".format(depth))
        depth += 1

# https://stackoverflow.com/questions/9886274/how-can-i-convert-canvas-content-to-an-image
def screenshot(widget, filename):

    x = root.winfo_rootx() + widget.winfo_x()
    y = root.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save(filename)

cantor(4, 0, width, 6)  # call the function without the old tester code
c.update()
