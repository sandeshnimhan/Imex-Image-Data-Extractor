'''
Authors - Pranav Velamakanni, Sandesh Nimhan
    Version 0.1 - first revision
'''

import pytesseract
import PIL
from PIL import Image
import sqlite3
import os
import sys

connection = sqlite3.connect("Company.db")

while True:
    try:
        x = int(input("How many bills do you have today?\n"))
        break
    except ValueError:
        print("Invalid input, please retry\n")
    except ZeroDivisionError:
        print("Invalid input, please retry\n")

bills = []

while x != 0:

    bills.append(str(input("Enter the file name\n")))
    x -= 1

billsx = tuple(set(bills))
x2 = len(billsx)
x3 = len(billsx)
i = 0
i2 = 0

while x2 != 0:
    data = pytesseract.image_to_string(Image.open(billsx[i]))
    name = str(i) + '.txt'
    fw = open(name, 'w')
    fw.write(data)
    fw.close()
    x2 -= 1
    i += 1

n = 0
myList = []

#Test

while x3 != 0:
    name = str(i2) + '.txt'
    fr = open(name, 'r')
    while True:
        frx = fr.readline()
        if n == 1:
            myList.append(frx)
        if n == 4:
            myList.append(frx)
        if n == 11:
            frt = frx.split(" ")
            myList.append(frt[0])
            myList.append(frt[1])
            myList.append(frt[2])
        if n == 17:
            frt = frx.split(" ")
            myList.append(frt[2])
        n += 1
        if not frx:
            break
    x3 -= 1

print("On " + myList[2] + " " + myList[3] + " " + myList[4] + " You spent " + "$" + myList[5] + "at " + myList[0] + myList[1])