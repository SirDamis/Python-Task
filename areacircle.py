from math import pi, pow
def area_of_circle(radius):
	return pi * pow(radius, 2)

radius = float(input('Enter radius: '))
print(f'Area of circle: {area_of_circle(radius)}')