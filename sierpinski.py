##from graphics import GraphicsImage, GraphicsWindow
##from color_utils import *
from tkinter import *
import math

SHOULD_DISPLAY_IMAGE = False

class Triangle:
    objectName = "Triangle"     # Object title
    objectNum = 0               # Number of instances created

    def __init__(self, canvas, left, top, width, height, objColor = "black", tremaColor = "white"):

        #attributes from parameters
        self.c = canvas
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.objColor = objColor
        self.tremaColor = tremaColor

        #calculated attributes
        self.tag = Triangle.objectName + str(Triangle.objectNum)
        Triangle.objectNum += 1
        self.right = self.left + self.width
        self.bottom = self.top + self.height
        self.center = (self.left + self.right) / 2.0
        self.middle = (self.top + self.bottom) / 2.0

    def draw(self):

        # X-coordinate guide list
        xspaces = 500
        xgridwidth = 1.0 * self.width / xspaces
        x = []
        for i in range(xspaces + 1):
            x.append(self.left + i * xgridwidth)

        # Y-coordinate guide list
        yspaces = 500
        ygridwidth = 1.0 * self.height / yspaces
        y = []
        for i in range(yspaces + 1):
            y.append(self.top + i * ygridwidth)

        # Triangle guides
        triangle = (  (x[10],y[490]) , (x[490],y[490]) , (x[250],y[int(490 - ((480 * math.sqrt(3)) / 2))])  )

        # Trema guides
        trema = (  (x[10],y[490]) , (x[490],y[490]) , (x[250],y[int(490 - ((480 * math.sqrt(3)) / 2))])  )

        # Draw triangle
        self.triangleID = self.c.create_polygon(triangle, fill = self.objColor, tag = self.tag)

        self.c.update()

    def set_properties(self, objColor = "default", tremaColor = "default"):

        if objColor != "default":
            self.objColor = objColor
            self.c.itemconfig(self.objID, fill = self.objColor)
            self.c.update()
        if tremaColor != "default":
            self.tremaColor = tremaColor
            self.c.itemconfig(self.tremaID, fill = self.tremaColor)
            self.c.update()

    def shrink(self, delay = 5, xscale = 1.0, yscale = 1.0):

        assert self.height == (self.width * math.sqrt(3)) / 2, "Triangle needs to be equilateral."

        self.c.after(delay)
        self.c.scale(self.tag, self.center, self.middle, xscale, yscale)
        self.width = self.width / xscale
        self.height = self.height / yscale
        self.c.update()
        
