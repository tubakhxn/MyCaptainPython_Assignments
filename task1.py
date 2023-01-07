#Writing a Python program which accepts the radius of a circle from the user and computes area

from math import pi

r = float(input ("Enter radius of circle : "))

print ("Area of the circle is: " + str(pi * r**2))
