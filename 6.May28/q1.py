l=[]
num=int(input("Enter the number of students "))

for i in range(num):
    name=input("Enter name: ")
    age=int(input("Enter age: "))
    pnum=input("Enter Phone number: ")
    add=input("Enter Address: ")
    print()
    d={"name":name,"age":age,"Phonenumber":pnum,"address":add}
    l.append(d)
print(l)