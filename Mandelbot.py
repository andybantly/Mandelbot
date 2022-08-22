#
# Mandelbot.py a Python script to generate a random 320 x 200 mandelbrot image
# Developed by Andy Bantly
# Version 1.0.1
#
import threading
import glob
import praw
from PIL import Image
import random
import time

def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.png")]
    frame_one = frames[0]
    frame_one.save("R:\\Mandelbot.gif", format="GIF", append_images=frames,
               save_all=True, duration=100, loop=0)

def Mandelfunc(nthread,max_iterations,max_size,maxcol,max_colors,deltap,p,row1,row2,pixels,pixelcolormap,red=[],green=[],blue=[],freq=[],q=[]):
    print("Thread=",nthread," cols=",maxcol," r1=",row1," r2=",row2,"\n")
    i = 1
    for col in range(maxcol):
        print("Thread=",nthread," ",(i + 1)/(maxcol*(row2-row1)))
        for row in range(row1,row2):
            x = 0.0
            y = 0.0
            xsquare = 0.0
            ysquare = 0.0
            color : int = 1
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
            pixelcolormap[col,row] = (color, color, color)
            freq[color] = freq[color] + 1;
        p = p + deltap

def Mandelbrot():
    global xmin
    global xmax
    global ymin
    global ymax

    cxmin = []
    cxmax = []
    cymin = []
    cymax = []
    cxmin.append(-0.717997)
    cxmax.append(-0.592801)
    cymin.append(0.395415)
    cymax.append(0.505444)
    cxmin.append(-0.707981)
    cxmax.append(-0.627856)
    cymin.append(0.477937)
    cymax.append(0.367908)
    cxmin.append(-0.702973)
    cxmax.append(-0.642879)
    cymin.append(0.374785)
    cymax.append(0.395415)
    cxmin.append(-0.691060)
    cxmax.append(-0.690906)
    cymin.append(0.387103)
    cymax.append(0.387228)
    cxmin.append(-0.793113)
    cxmax.append(-0.723005)
    cymin.append(0.037822)
    cymax.append(0.140974)
    cxmin.append(-0.745465)
    cxmax.append(-0.745387)
    cymin.append(0.112896)
    cymax.append(0.113034)
    cxmin.append(-0.745464)
    cxmax.append(-0.745388)
    cymin.append(0.112967)
    cymax.append(0.113030)
    cxmin.append(-0.745432471875)
    cxmax.append(-0.74542493125)
    cymin.append(0.113005267578125)
    cymax.append(0.113012588867188)
    x1 : float = -2.0
    x2 : float = 1.2
    y1 : float = -1.0
    y2 : float = 1.2
    maxcol : int = 1920
    maxrow : int = 1080
    max_colors : int = 1024
    max_iterations : int = 1024
    max_size : int = 8
    random.seed()
    img = Image.new("RGB", (maxcol, maxrow), "black")
    pixels = img.load()
    imgidx = Image.new("RGB", (maxcol, maxrow), "black")
    pixelcolormap = imgidx.load()
    red = []
    green = []
    blue = []
    freq = []
    for col in range(0, max_colors):
        colorr : int = random.randint(0,255)
        colorg : int = random.randint(0,255)
        colorb : int = random.randint(0,255)
        red.append(colorr)
        blue.append(colorg)
        green.append(colorb)
        freq.append(0);
    if random.randint(1,100) >= 66:
        if random.randint(1,100) >= 50:
            red.sort(reverse=True)
        else:
            red.sort(reverse=False)
    else:
        if random.randint(1,100) >= 66:
            if random.randint(1,100) >= 50:
                green.sort(reverse=True)
            else:
                green.sort(reverse=False)
        else:
            if random.randint(1,100) >= 66:
                if random.randint(1,100) >= 50:
                    blue.sort(reverse=True)
                else:
                    blue.sort(reverse=False)
            else:
                v = random.randint(1,3)
                if v == 1:
                    if random.randint(1,100) >= 50:
                        blue.sort(reverse=True)
                    else:
                        blue.sort(reverse=False)
                elif v==2:
                    if random.randint(1,100) >= 50:
                        green.sort(reverse=True)
                    else:
                        green.sort(reverse=False)
                else:
                    if random.randint(1,100) >= 50:
                        red.sort(reverse=True)
                    else:
                        red.sort(reverse=False)

    for col in range(1, max_colors):
        colorr : int = random.randint(0,255)
        colorg : int = random.randint(0,255)
        colorb : int = random.randint(0,255)
        if colorr == red[col]:
            red[col] = random.randint(0,255)
        if colorg == green[col]:
            green[col] = random.randint(0,255)
        if colorb == blue[col]:
            blue[col] = random.randint(0,255)
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
        ymax = ((y2 - y1) / (x2 - x1)) * (xmax - xmin) # aspect ratio correction, always do this...
        n = random.randint(1,100)
        if (n >= 90):
            n = random.randint(1,len(cxmin)) - 1
            xmin = cxmin[n]
            xmax = cxmax[n]
            ymin = cymin[n]
            ymax = cymax[n]

        deltap = (xmax - xmin) / maxcol
        deltaq = (ymax - ymin) / maxrow
        q.append(ymax)
        for col in range(1, maxcol):
            q.append(q[col - 1] - deltaq)
        p = xmin

        i = 1
        for col in range(maxcol):
            print("{:0.3f}".format(i/(maxcol*maxrow)))
            for row in range(maxrow):
                i = i + 1
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
                pixelcolormap[col,row] = (color, color, color)
                freq[color] = freq[color] + 1;
            p = p + deltap
        Again = False
        for color in range(0, max_colors):
            if freq[color] >= (maxrow * maxcol * .75):
                Again = True
                break
        if Again == False:
            break;

    for frame in range(0, max_colors):
        fname = "R:\\Mandelbot{:04d}.png".format(frame)
        img.save(fname)
        tempred = red[0]
        tempblue = blue[0]
        tempgreen = green[0]
        for color in range(0, max_colors - 1): # 0 TO N-1 INCLUSIVE 
            red[color] = red[color + 1]
            blue[color] = blue[color + 1]
            green[color] = green[color + 1]
        red[max_colors - 1] = tempred;
        blue[max_colors - 1] = tempblue;
        green[max_colors - 1] = tempgreen;
        for col in range(maxcol):
            for row in range(maxrow):
                pixels[col,row] = (red[pixelcolormap[col,row][0]], green[pixelcolormap[col,row][1]], blue[pixelcolormap[col,row][2]])
    make_gif("R:\\")
Mandelbrot()
