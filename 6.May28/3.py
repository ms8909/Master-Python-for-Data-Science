#  Linear Search

# This Will Search the Number in list and will return the index's
# at which number is.
def Find_Index(Number,List):
    index=[]
    for i in range(len(List)):
       if(List[i]==Number):
            index.append(i)
    return index

# Main Function
List=[1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
print("List: ",List)
No=int(input("Enter a number to find it's Index: "))
Answer=Find_Index(No,List)
print("Your Number is at Index No(s): ",Answer)
