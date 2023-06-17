import math

def calculate_area(radius):
    area = math.pi * radius * radius
    return area

radius = float(input("Enter the radius of the circle: "))

area = calculate_area(radius)

print(area)
