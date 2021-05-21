def rectangle(l,b):
    for i in range(l):
        for j in range(b):
            print("*", )
        print()

def flagpole(l,b):
    for i in range(l):
        for j in range(b):
            print("*", )
        print()        

print("How long is your flag?")
x=int(input())
print("How wide is your flag?") 
y=int(input())    
print("How long is your flagpole?") 
x1=int(input())
print("How wide is your flagpole?")
y1=int(input())     

rectangle(x,y)
flagpole(x1,y1)

