def rectangle(FL, FB, PL, PB):

    for i in range(FL): #for loop for flag length
        print("")
        for k in range (FB): #for loop for flag breadth
            print("*",end="")
    for i in range(PL): #for loop for pole length
        print("")
        for k in range (PB): #for loop for pole breadth
            print("*",end="")
#input from users
Input_FL = int(input("How long is your flag? - "))
Input_FB = int(input("How wide is your flag? - "))
Input_PL = int(input("How long is your flagpole? - "))
Input_PB = int(input("How wide is your flagpole? - "))
rectangle(Input_FL,Input_FB,Input_PL,Input_PB)  # calling of function