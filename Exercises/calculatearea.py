# Takes user input
# Calculates area of a circle using math module and using imports
# round() and type casting functions

import math

rad = float(input("Enter a radius: \n"))
calculate_area = math.pi * (math.pow(rad, 2))
area = round(calculate_area, 4)
print("Area of a circle with radius " + str(rad) + " is: \n" + str(area))