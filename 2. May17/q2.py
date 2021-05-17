print ("Enter total number of classes held")
x= int(input())
print ("Enter number of classes attended by the student")
y= int (input())
z=(y/x)*100
print("The percentage of classes attended is ")
print(z)
if z<75:
    print("The student is not allowed to sit in the exam")
else:
    print("The student is allowed to sit in the exam")