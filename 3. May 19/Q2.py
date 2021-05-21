# part A
h=3
for i in range(h):

    print( "*" * (i * 2 + 1 ))
    
#===================================================================
# part  B
print()
h=3
for i in range(h):

    print(" " *(h-i), "*" * (i * 2 + 1 ))

for i in range(h-2, -1, -1):
    print(" "*(h-i), "*" *(i*2+1))

#===================================================================
#Part C
print("")
num=7

for i in range((num // 2) + 1, num+1):
    for j in range(i - (num // 2) + 1):
        print(" ", end="")
    for k in range(1, ((num+1-i) * 2-1) +1):        
        print(k % 2, end="")
    print("")