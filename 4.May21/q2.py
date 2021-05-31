def rectangle(l,w):
    for i in range(l):
        print("*"*w)
def flag_pole(l_pole,w_pole):
    for i in range(l_pole):
        print("*"*w_pole)
l = int(input("How long is your flag? "))
w = int(input("How wide is your flag? "))
flag_pole_height = int(input("How long is your flagpole? "))
flag_pole_width = int(input("How wide is your flagpole? "))
rectangle(l,w)
flag_pole(flag_pole_height,flag_pole_width)