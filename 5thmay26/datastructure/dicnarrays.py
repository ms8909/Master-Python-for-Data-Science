#  Let’s store data in dictionaries and arrays

# This will take Inputs From User And will insert that inputs Into Dictionary
# And Will Insert That Dictionary Into Array.
def Inputs(no):
    List_students=[]
    for i in range(no):
        print()
        print("Entry no:",i+1)
        Name=input("Name: ")
        Age=int(input("Age: "))
        PhoneNumber=int(input("Phone No: "))
        Address=input("Address: ")
        Dic={"Name":Name,"Age":Age,"PhoneNumber":PhoneNumber,"Address":Address}
        List_students.insert(i,Dic)
    return List_students

# Main Function
no=int(input("Number Of Students You Wanna Enter: "))
List_Of_All_Students=Inputs(no)
print("List Of All Students: ",List_Of_All_Students) 