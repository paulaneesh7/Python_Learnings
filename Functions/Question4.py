
import math

def area_circumferece(r):
    area = math.pi * r *r
    cirumference = 2 * math.pi * r

    return area, cirumference

r = float(input("Enter the radius of the circle: "))

area, circumference = area_circumferece(r)

print(f"Area of the circle is: {area}")
print(f"Circumference of the circle is: {circumference}")