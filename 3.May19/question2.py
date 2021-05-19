
# part a

def print_triangle(length):
    i = 0
    j = 0
    limit = length
    limit2 = 1
    while j < limit:
        while i < limit2:
            print('*', end=' ')
            i = i + 1
        print("")
        i = 0
        j = j + 1
        limit2 = limit2 + 1
    print("\n")


print_triangle(4)

#partb
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