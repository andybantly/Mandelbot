#
# Mandelbot.py a Python script to generate a random 320 x 200 mandelbrot image
# Developed by Andy Bantly
# Version 1.0.0
#
from PIL import Image
import random

x1 = -2.0
x2 = 1.2
y1 = -1.0
y2 = 1.2
maxcol = 320
maxrow = 200
max_colors = 256
max_iterations = 256
max_size = 4
random.seed()
img = Image.new("RGB", (maxcol, maxrow), "black")
pixels = img.load()
while True:
    Again = False
    red = []
    green = []
    blue = []
    freq = []
    for col in range(0, maxcol):
        red.append(random.randrange(0, max_colors + 1, 1))
        blue.append(random.randrange(0, max_colors + 1, 1))
        green.append(random.randrange(0, max_colors + 1, 1))
        freq.append(0);
    q = []
    v1 = random.uniform(x1,x2)
    v2 = random.uniform(x1,x2)
    while v2 == v1:
        v2 = random.uniform(x1,x2)
    if v1 > v2:
        xmax = v1
        xmin = v2
    else:
        xmax = v2
        xmin = v1
    v1 = random.uniform(y1,y2)
    v2 = random.uniform(y1,y2)
    while v2 == v1:
        v2 = random.uniform(y1,y2)
    if v1 > v2:
        ymax = v1
        ymin = v2
    else:
        ymax = v2
        ymin = v1
    ymax = ((y2 - y1) / (x2 - x1)) * (xmax - xmin) # aspect ratio correction
    deltap = (xmax - xmin) / maxcol
    deltaq = (ymax - ymin) / maxrow
    q.append(ymax)
    for col in range(1, maxcol):
        q.append(q[col - 1] - deltaq)
    p = xmin
    for col in range(maxcol):
        for row in range(maxrow):
            x = 0.0
            y = 0.0
            xsquare = 0.0
            ysquare = 0.0
            color = 1
            while True:
                xsquare = x * x
                ysquare = y * y
                y = 2 * x * y + q[row]
                x = xsquare - ysquare + p
                color = color + 1
                if (color >= max_iterations) or ((xsquare + ysquare) >= max_size):
                    break
            color = color % max_colors
            pixels[col,row] = (red[color], green[color], blue[color])
            freq[color] = freq[color] + 1;
        p = p + deltap
    for col in range(0, maxcol):
        if freq[col] >= 48000:
            Again = True
            break
    if Again == False:
        break;
img.save("R:\\mandelbot.png")