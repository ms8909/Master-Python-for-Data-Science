cheld=int(input("Number of classes held: "))
cattend=int(input("Number of classes attended: "))
percentage=int((100*cattend)/cheld)
print("percentage of class attended is: ", percentage,"%")
if percentage<75:
    print("you are not allowed to sit in exam")
else:
    print("you are allowed to sit in exam")