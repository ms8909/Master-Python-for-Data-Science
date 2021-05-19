#Factorial Calculator
 
n=int(input("Enter No To Get Factorial: "))
answer=1
for i in range(n):
    answer=answer*(i+1)
print("Answer: ",answer)