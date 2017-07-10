#                 Sierpinski Triangle
#
#  Programmed by Jean Flaherty and Griffin Myers (06-24-2017)
#
#  A couple of ways to draw the Sierpinski triangle, another image with
#  a fractal pattern
#
#  Functions:
#       draw       -- simply draws the base triangle
#       draw_trema -- recursively draws self-similar triangles
#


from tkinter import *
from PIL import ImageGrab
import math

def draw(top, left, right):

    width = right - left

    height = (width * math.sqrt(3)) / 2.0

    center = (left + right) / 2.0

    triangle = (    (center,top), (right,height), (left,height)   )

    triangle_id = c.create_polygon(triangle, fill = "black")

    c.update()

def draw_trema(left, right, top, bottom):

    width = right - left

    height = (width * math.sqrt(3)) / 2.0

    center = (left + right) / 2.0

    trema = (   (left+(width/4),height/2),
                (right-(width/4),height/2),
                (center,height)   )

    queue = [trema]
    depth = 0
    while queue:
        for i in range(3 ** depth):
            (left_tup, right_tup, bottom_tup) = queue.pop(0)

            (left_x, left_y) = left_tup
            (right_x, right_y) = right_tup
            (bottom_x, bottom_y) = bottom_tup

            width = right_x - left_x

            height = (width * math.sqrt(3)) / 2.0

            center = (left_x + right_x) / 2.0

            trema = (   (left_x, left_y),
                        (right_x, right_y),
                        (bottom_x, bottom_y)   )

            trema_id = c.create_polygon(trema, fill = "white")

            queue.append((
                        (left_x-(width/4),bottom_y-(height/2)),
                        (left_x+(width/4),bottom_y-(height/2)),
                        (left_x,bottom_y)
                        ))

            queue.append((
                        (bottom_x-(width/4),left_y-(height/2)),
                        (bottom_x+(width/4),right_y-(height/2)),
                        (bottom_x,left_y)
                        ))

            queue.append((
                        (right_x-(width/4),bottom_y-(height/2)),
                        (right_x+(width/4),bottom_y-(height/2)),
                        (right_x,bottom_y)
                        ))

        c.update()
        c.after(2000)
        screenshot(c, "output/tri_{}.gif".format(depth))
        depth += 1


# https://stackoverflow.com/questions/9886274/how-can-i-convert-canvas-content-to-an-image
def screenshot(widget, filename):

    x = root.winfo_rootx() + widget.winfo_x()
    y = root.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save(filename)

width = 729
height = 729

root = Tk()

c = Canvas(root, width = 729, height = 729, bg = "white")
c.pack()

draw(0,0,width)
c.update()
draw_trema(0,width,0,height)
c.update()
