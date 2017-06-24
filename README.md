# fractal-practice

##### These are the rudiments of a collection of fractal images. It will expand as I learn more about them and the functions that create them.

##### The first of these, and the easiest for me to understand, is the Sierpinski carpet. It recurs as the Sierpinski triangle does, but in a more square-shaped way. I call it "rug".

![](output/rug_0.gif)
![](output/rug_1.gif)
![](output/rug_2.gif)
![](output/rug_3.gif)
![](output/rug_4.gif)
![](output/rug_5.gif)

##### This collection of images resulted from a function that prints the big black square in the center, then multiplies exponentially smaller versions of that square by powers of 8. The solid black image indicate that the squares have multiplied so many times as to round out the white background.

##### Before the images displayed layer by layer, the program ran so that each of the eight cells in the layer second from the top would fill with smaller squares before moving to the next cell. The output looked something like this:

![](output/old_rug_4096.gif)
![](output/old_rug_12288.gif)
![](output/old_rug_20480.gif)
![](output/old_rug_28672.gif)
![](output/old_rug_32768.gif)

##### The above images came from a modification made to the draw function that took a screenshot at every new square drawn. That modification produced 32,768 screenshots.

![](rug.gif)

##### As with any fractal, the function that draws this is recursive, and won't stop running unless the user manually closes it.

![](output/old_rug_32155.gif)
