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
                 obj_color = "black", trema_color = "white"):
        
        #attributes from parameters
        self.root = root
        self.c = canvas
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.obj_color = obj_color
        self.trema_color = trema_color 

        #calculated attributes
        self.tag = Triangle.objectName + str(Triangle.objectNum)
        Triangle.objectNum += 1
        self.right = self.left + self.width
        self.bottom = self.top + self.height
        self.center = (self.left + self.right) / 2.0
        self.middle = (self.top + self.bottom) / 2.0

        #self.depth = 5
        

##    def draw(self):
##
##        queue = [((self.left,self.bottom), (self.right,self.bottom), (self.center,self.top))]
##
##        depth = 0
##
##        while queue:
##            for i in range(3 ** depth):
##
##                (left_tup, right_tup, top_tup) = queue.pop(0)
##
##                (left_x, left_y) = left_tup
##                (right_x, right_y) = right_tup
##                (top_x, top_y) = top_tup
##
##                width = right_x - left_x
##                height = (width * math.sqrt(3)) / 2.0 
##
##                center = (left_x + right_x) / 2.0
##
##                bottom = height
##
##                triangle = (    (center,top_y), (right_x,bottom), (left_x,bottom)  )
##
##                trema = (   (left_x+(width/2),bottom-(height/2)),
##                            (right_x-(width/2),bottom-(height/2)),
##                            (width/2, bottom)    )
##
##                self.triangle_id = self.c.create_polygon(triangle, fill = self.obj_color, tag=self.tag)
##
##                self.trema_id = self.c.create_polygon(trema, fill = self.trema_color, tag=self.tag)
##
##                queue.append((
##                            (left_x+(width/8),bottom-(height/4)),
##                            (center-(width/8),bottom-(height/4)),
##                            (width/4, bottom)
##                            ))
##
####                queue.append((top+(height/3), bottom-(height/3), right-(width/3), right))
####                queue.append((bottom-(height/3), bottom, right-(width/3), right))
####                queue.append((bottom-(height/3), bottom, left+(width/3), right-(width/3)))
####                queue.append((bottom-(height/3), bottom, left, left+(width/3)))
####                queue.append((top+(height/3), bottom-(height/3), left, left+(width/3)))
##
##            self.c.update()
##            self.c.after(1000)
##            self.screenshot(self.c, "tri_{}.gif".format(depth))
##            depth += 1

    def draw(self, top, left, right):

        queue = [(top, left, right)]
        depth = 0
        while queue:
            for i in range(3 ** depth):
                (top, left, right) = queue.pop(0)

                width = right - left

                height = (width * math.sqrt(3)) / 2.0

                center = (left + right) / 2.0

                bottom = height

                triangle = (    (center,top), (right,bottom), (left,bottom)   )

                trema = (   (left+(width/4),height/2),
                            (right-(width/4),height/2),
                            (center, bottom)   )

                self.triangle_id = self.c.create_polygon(triangle, fill = self.obj_color, tag=self.tag)

                self.trema_id = self.c.create_polygon(trema, fill = self.trema_color, tag=self.tag)

                queue.append((
                            (left+(width/2),bottom-(height/2)),
                            (center-(width/2),bottom-(height/2)),
                            (width/2, bottom)
                            ))
                
            self.c.update()
            self.c.after(1000)
            self.screenshot(self.c, "tri_{}.gif".format(depth))
            depth += 1
                

    # https://stackoverflow.com/questions/9886274/how-can-i-convert-canvas-content-to-an-image
    def screenshot(self, widget, filename):

        x = self.root.winfo_rootx() + widget.winfo_x()
        y = self.root.winfo_rooty() + widget.winfo_y()
        x1 = x + widget.winfo_width()
        y1 = y + widget.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
            
