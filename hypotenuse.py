# Write a script that calculates the hypotenuse
#  of a right-angled triangle given 
# the other two sides. Use the sqrt() function.
# c = squareroot(a**2+ b**2)
import math
a = float(input("enter length of side a"))
b = float(input("enter length of side b"))
c =math.sqrt(a**2 +b**2)
print("hypotenuse is ",c)
