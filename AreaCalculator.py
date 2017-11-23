"""
my program will ask youser for geometrical shape
program will calculate area of the shape
program will print area of the shape
"""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
print
"Area Calculator"
print
"Current time %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)
sleep(1)
hint = "Don't forget to include the correct units! \nExiting..."
option = input("Enter C for Circle or T for Triangle:")
option = option.upper()
if option == 'C':
    radius = float(input("Enter radius: "))
    area = pi * radius ** 2
    print
    "The pie is baking..."
    sleep(1)
    print("Area: %.2f. \n%s" % (area, hint))

elif option == 'T':
    base = float(input("Enter base:  "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print
    "Uni Bi Tri..."
    sleep(1)
    print("Area: %.2f \n%s" % (area, hint))

else:
    print
    "Error! Invalid shape selector specified. Exiting."