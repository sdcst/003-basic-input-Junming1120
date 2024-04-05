#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912
import math
height = int(input("give me a value for height"))
radius = int(input("give me a value for radius"))
sa = math.pi*radius*(radius+((height**2+radius**2)**0.5))
print("sa="+str(sa))
