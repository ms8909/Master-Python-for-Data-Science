# Python Program to find Volume and Surface Area of Cuboid
length = float(input('Please Enter the Length of a Cuboid: '))
width = float(input('Please Enter the Width of a Cuboid: '))
height = float(input('Please Enter the Height of a Cuboid: '))
# Calculate the Surface Area
SA = 2 * (length * width + length * height + width * height)
# Calculate the Volume
Volume = length * width * height


print("\n The Surface Area of a Cuboid" ,SA)
print(" The Volume of a Cuboid " ,Volume)
