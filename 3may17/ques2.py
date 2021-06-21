def stars(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*"*i)
    print("\n".join(myList))
 
# Driver Code
n = 4
stars(n)



p = input("first value : ")
q = input("second value : ")
j = 0
k = int(input("rows you want? : "))
while k >= 1:
    print(" "*j + (k-1)*(p+q) +p+ " "*j)
    k = k-1
    j=j+1


def pattern(n):
      for i in range(0, n):
           for j in range(0, i + 1):
                print("* ", end="")
           print("\r")
      for i in range(n, 0 , -1):
          for j in range(0, i + 1):
               print("* ", end="")
          print("\r")
 
pattern(3)