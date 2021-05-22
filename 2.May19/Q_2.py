#  Part a.......................................
print("a:");

# Function to demonstrate printing pattern
def pattern(n):
	
	# outer loop to handle number of rows
	# n in this case
	for i in range(0, n):
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ",end="")
	
		# ending line after each row
		print("\r")


n = 5
pattern(n)
#     Part b..................................................
print("b:");

rows = int(input("Enter The Number Of Rows: "))
columns = 2*rows -1
i = 0
while i < rows:
    j = 0
    while j < columns :
        if( (columns//2)-i <= j <= (columns//2)  +i):
            print("*",end = "")
        else:
            print(" ",end = "")
        
        j+=1
    print(" ")
    i+=1
    
i = 0
while i < rows:
    j = 0
    while j < columns :
        if( i <= j <= columns-1 -i):
            print("*",end = "")
        else:
            print(" ",end = "")
        
        j+=1
    print(" ")
    i+=1

	# part c.............................................................
print("c:")

def invert(n):
    if n ==1:
            return 0
    else:
        return 1
n = 1
linerange = 7
for a in range(4):
    print(" "*a, end="")
    for b in range(linerange):
        print(n,end="")
        n = invert(n)
    n = invert(n)
    linerange -=2
    print() 
