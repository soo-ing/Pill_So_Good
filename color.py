import numpy as np 
import cv2 
import csv
from PIL import Image

def color(fname, word):
    im = Image.open(fname)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((300, 200))
    data="none"

    print(r, g, b)
    f=open('pill.csv','w',newline='')
    wr=csv.writer(f)

    if 200<g and 200<r and b<255:
        print("yellow")
        data="yellow"

    if 139<g<255 and r>0 and r<200  and b<200:
        print("green")
        data="green"

    if 150<b<255:
        print("blue")
        data="blue"

    if r==255 and g==255 and b==255:
        print("white")
        data="white"

    if 160<r<255 and g<150 and b<150:
        print("red")
        data="red"

    print(data)
    wr.writerow([word,data])
    
    return data
