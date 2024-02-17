# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math

def area_circumference(radius):
    area =  math.pi * radius ** 2
    circum = 2 * math.pi * radius
    return area,circum

a,c = area_circumference(2)

print("Area:",round(a), "Circumference:",round(c))