def rectangle(l,b):
    for i in range(l):
        for j in range(b):
            print("*", end="")
        print()

def flagpole(l,b):
    for i in range(l):
        for j in range(b):
            print("*", end="")
        print()        

print("How long is your flag?")
x=int(input())
print("How wide is your flag?") 
y=int(input())    
print("How long is your flagpole?") 
a=int(input())
print("How wide is your flagpole?")
b=int(input())     

rectangle(x,y)
flagpole(a,b)
