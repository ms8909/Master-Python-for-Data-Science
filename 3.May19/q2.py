#a)
print("a)")
for x in range(4):
  print("*"*(x+1))

#b
print("b)")
h=5
for x in range(h):
    print(" "*(h-x),"*"*(x*2+1))
for z in range(x):
    print(" "*(z+2),"*"*(x*2-1))
    x=x-1

#c)
print("c)")
a=1010101
for x in range(7-int(7/2)):
    print(" "*x,a)
    a=int(a/100)