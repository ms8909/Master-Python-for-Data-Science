# def insertionsort

list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

n=int(input("Enter the number of elements"))

print("Enter the elements of list:" )
for item in range(n):
  a=int(input(" "))
  list1.append(a)

  print ("list is:", list1)

  for i in range(len(list1)):
    for j in range(0,i):
      if (list1[i]<list1[j]) :
        temp=list1[i]
        list1[i]=list1[j]
        list1[j]=temp

print("Sorted list is:", list1)
