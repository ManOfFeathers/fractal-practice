#                 Sierpinski Triangle
#
#  Programmed by Jean Flaherty and Griffin Myers (06-24-2017)
#
#  A couple of ways to draw the Sierpinski triangle, another image with
#  an infinitely recursive pattern
#
#  Functions:
#       __init__  -- introduce attributes
#       draw      -- recursive fuction that draws the original triangle,
#                    as well as each trema, layer by layer
#


from tkinter import *
from PIL import ImageGrab
import math

class Triangle:
    objectName = "Triangle"     # Object title
    objectNum = 0               # Number of instances created

    def __init__(self, root, canvas, left, top, width, height,
                 tri_color = "black", trema_color = "white"):
        
        #attributes from parameters
        self.root = root
        self.c = canvas
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.tri_color = tri_color
        self.trema_color = trema_color

        #calculated attributes
        self.tag = Triangle.objectName + str(Triangle.objectNum)
        Triangle.objectNum += 1
        self.right = self.left + self.width
        self.bottom = self.top + self.height
        self.center = (self.left + self.right) / 2.0
        self.middle = (self.top + self.bottom) / 2.0

    def draw(self, top, left, right):

        width = right - left

        height = (width * math.sqrt(3)) / 2.0

        center = (self.left + self.right) / 2.0        

        triangle = (    (center,top), (right,height), (left,height)   )

        self.triangle_id = self.c.create_polygon(triangle, fill = self.tri_color, tag=self.tag)

        self.c.update()

    def draw_trema(self, left, right, top, bottom):

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

                self.trema_id = self.c.create_polygon(trema, fill = self.trema_color, tag=self.tag)

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
               
            self.c.update()
            self.c.after(2000)
            self.screenshot(self.c, "output/tri_{}.gif".format(depth))
            depth += 1
                

    # https://stackoverflow.com/questions/9886274/how-can-i-convert-canvas-content-to-an-image
    def screenshot(self, widget, filename):

        x = self.root.winfo_rootx() + widget.winfo_x()
        y = self.root.winfo_rooty() + widget.winfo_y()
        x1 = x + widget.winfo_width()
        y1 = y + widget.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
            
