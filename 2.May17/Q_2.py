#          No.of classes attend and held.......
a = int(input("Enter no. of classes held:"));
b = int(input("Enter no. of classes attend:"));

#          c is the percentage of the attend classes.........
c = (b*100)/a;
print(c);

if(c < 75):
    print("You are not allowed to sit in class because your attendance is not above than 75");
else:
    print("Your are allowed to sit in class");
