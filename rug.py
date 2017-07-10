#                 Sierpinski Carpet (AKA rug)
#
#  Programmed by Jean Flaherty and Griffin Myers (06-24-2017)
#
#  A couple of ways to draw the Sierpinski carpet, an image with
#  a fractal pattern
#
#  Functions:
#       next_draw -- more intelligent function that draws each layer of
#                    squares in a for loop
#

from tkinter import *
from PIL import ImageGrab
import math

def next_draw(top, bottom, left, right):

    queue = [(top,bottom,left,right)]
    depth = 0
    while queue:
        for i in range(8 ** depth):
            (top,bottom,left,right) = queue.pop(0)
            width = right - left
            height = bottom - top
            grid = (    (left,top), (right,bottom)   )

            square = (   (left+(width/3),top+(height/3)),
                         (right-(width/3),bottom-(height/3))   )

            grid_id = c.create_rectangle(grid, fill = "white")
            square_id = c.create_rectangle(square, fill = "black")

            queue.append((top, top+(height/3), left, left+(width/3)))

            queue.append((top, top+(height/3), left+(width/3), right-(width/3)))

            queue.append((top, top+(height/3), right-(width/3), right))

            queue.append((top+(height/3), bottom-(height/3), right-(width/3), right))

            queue.append((bottom-(height/3), bottom, right-(width/3), right))

            queue.append((bottom-(height/3), bottom, left+(width/3), right-(width/3)))

            queue.append((bottom-(height/3), bottom, left, left+(width/3)))

            queue.append((top+(height/3), bottom-(height/3), left, left+(width/3)))

        c.update()
        c.after(1000)
        screenshot(c, "output/rug_{}.gif".format(depth))
        depth += 1

# https://stackoverflow.com/questions/9886274/how-can-i-convert-canvas-content-to-an-image
def screenshot(widget, filename):

    x = root.winfo_rootx() + widget.winfo_x()
    y = root.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save(filename)

# draw the function

width = 729
height = 729

root = Tk()

c = Canvas(root, width = 727, height = 727, bg = "black")
c.pack()

next_draw(0, height, 0, width)
c.update()
