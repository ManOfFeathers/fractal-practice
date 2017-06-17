from tkinter import *
from PIL import ImageGrab
import math

class Rug:
    object_name = "Square"
    object_num = 0

    def __init__(self, root, canvas, left, top, width, height,
    grid_color = "white", square_color = "black"):

        #attributes from parameters
        self.root = root
        self.c = canvas
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.grid_color = grid_color
        self.square_color = square_color

        #calculated attributes
        self.tag = Rug.object_name + str(Rug.object_num)
        Rug.object_num += 1
        self.right = self.left + self.width
        self.bottom = self.top + self.height
        self.center = (self.left + self.right) / 2.0
        self.middle = (self.top + self.bottom) / 2.0

        self.depth = 3

    def draw(self, top, bottom, left, right, depth = 0):

        if depth >= self.depth:
            return

        width = right - left
        height = bottom - top

        # coordinate guides
        grid = (    (left,top), (right,bottom)   )

        square = (   (left+(width/3),top+(height/3)),
                     (right-(width/3),bottom-(height/3))   )

        # draw commands
        self.grid_id = self.c.create_rectangle(grid, fill = self.grid_color, tag=self.tag)

        self.square_id = self.c.create_rectangle(square, fill = self.square_color, tag=self.tag)
        self.c.update()

        # go crazy
        self.draw(top, top+(height/3), left, left+(width/3), depth+1)
        self.c.update()

        self.draw(top, top+(height/3), left+(width/3), right-(width/3), depth+1)
        self.c.update()

        self.draw(top, top+(height/3), right-(width/3), right, depth+1)
        self.c.update()

        self.draw(top+(height/3), bottom-(height/3), right-(width/3), right, depth+1)
        self.c.update()

        self.draw(bottom-(height/3), bottom, right-(width/3), right, depth+1)
        self.c.update()

        self.draw(bottom-(height/3), bottom, left+(width/3), right-(width/3), depth+1)
        self.c.update()

        self.draw(bottom-(height/3), bottom, left, left+(width/3), depth+1)
        self.c.update()

        self.draw(top+(height/3), bottom-(height/3), left, left+(width/3), depth+1)
        self.c.update()

    def next_draw(self, top, bottom, left, right):

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

                self.grid_id = self.c.create_rectangle(grid, fill = self.grid_color, tag=self.tag)
                self.square_id = self.c.create_rectangle(square, fill = self.square_color, tag=self.tag)
                queue.append((top, top+(height/3), left, left+(width/3)))
                queue.append((top, top+(height/3), left+(width/3), right-(width/3)))
                queue.append((top, top+(height/3), right-(width/3), right))
                queue.append((top+(height/3), bottom-(height/3), right-(width/3), right))
                queue.append((bottom-(height/3), bottom, right-(width/3), right))
                queue.append((bottom-(height/3), bottom, left+(width/3), right-(width/3)))
                queue.append((bottom-(height/3), bottom, left, left+(width/3)))
                queue.append((top+(height/3), bottom-(height/3), left, left+(width/3)))
            self.c.update()
            self.c.after(1000)
            self.screenshot(self.c, "rug_{}.gif".format(depth))
            depth += 1

    # https://stackoverflow.com/questions/9886274/how-can-i-convert-canvas-content-to-an-image
    def screenshot(self, widget, filename):

        x = self.root.winfo_rootx() + widget.winfo_x()
        y = self.root.winfo_rooty() + widget.winfo_y()
        x1 = x + widget.winfo_width()
        y1 = y + widget.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
            
