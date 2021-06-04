print("Enter a DNA string")
x=input()
my_list=[]
for i in range(len(x)):
    if x[i]=="A":
        my_list.append(x[i])
    elif  x[i]=="C":
        my_list.append(x[i])
    elif  x[i]=="G":
        my_list.append(x[i])
    elif  x[i]=="T":
        my_list.append(x[i])
    else:
        print("It is not a valid string")
def reverse(s):
    reversed_list=[]
    for i in range(len(my_list)):
        reversed_list.append(my_list[len(my_list)-1-i])
    return reversed_list
def complement(s):
    complemented_list=[]
    for i in range(len(s)):
       if s[i]=="A":
           complemented_list.append("T")
       if s[i]=="C":
            complemented_list.append("G")
       if s[i]=="G":
            complemented_list.append("C")
       if s[i]=="T":
            complemented_list.append("A")
    return complemented_list
a=reverse(my_list)
print(complement(a))