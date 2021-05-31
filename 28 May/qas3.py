name=[]
age=[]
phonenumber=[]
address=[]
con="y"
while con=="y":
    name.append(input("inter the name"))
    age.append(input("enter your age"))
    phonenumber.append(input("enter your p_number"))
    address.append(input("enter your address"))
    print("enter y for continue or n for close")
    con=input()
student_data=[]
for b in range(len(name)):
    student_data.append({"name":name[b],"age":age[b],"phonenumber":phonenumber[b],"address":address[b]})
print(student_data)