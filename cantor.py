import numpy as np
#import matplotlib.pyplot as plt
from tkinter import *


# make a few good points

root = Tk()

width = 600
height = 600

c = Canvas(root, width = width, height = height)
c.pack()

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
        
##    for i in range(max_i):
##
##        mat_left = [(x_start,y),
##                    (x_start + (mat_r / 3.0),y)] 
##        mat_right = [(x_end - (mat_r / 3.0),y),
##                     (x_end,y)] 
##
##        
##        mat_left_out = [(x_start + (2*(mat_r / 9.0)),y),
##                        (x_start + (3*(mat_r / 9.0)),y)]
##        mat_right_out = [(x_end - (3*(mat_r / 9.0)),y),
##                         (x_end - (2*(mat_r / 9.0)),y)]
##
##        
##        mat_left_in = [(x_start + (8*(mat_r / 27.0)),y),
##                       (x_start + (9*(mat_r / 27.0)),y)]
##        mat_right_in = [(x_end - (9*(mat_r / 27.0)),y),
##                        (x_end - (8*(mat_r / 27.0)),y)]
##
##        mat_r = mat_r / 3.0 
##
##
##        mat.append(mat_left)
##        mat.append(mat_right)
##        mat.append(mat_left_out)
##        mat.append(mat_right_out)
##        mat.append(mat_left_in)
##        mat.append(mat_right_in)

    
##    return mat

##print(cantor(1,0,6,2))

# draw

##def draw_cantor():
##
##

##
##    max_i = 5
##    x_start = 0
##    x_end = width
##    y = 2
##
##
##    instructions = cantor(max_i, x_start, x_end, y)
##
##    print(instructions)
##
##    for coord in instructions:
##        c.create_line(coord[0][0],coord[0][1], coord[1][0],coord[1][1], fill = "black")
##    c.update()

cantor(4, 0, width, 2)
