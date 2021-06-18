def linear_search(L,n):
    index_storage = ""
    for i in range(len(L)):
        if n == L[i]:
            str_i = str(i)
            index_storage = index_storage + str_i + ","
    
    return index_storage

list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
number = 2

Searched = linear_search(list1,number)
discard_comma = len(Searched) - 1

if Searched == "" :
    print("Your number is not exist in the list")
else: 
    print("Your searched number index(es) is/are ", Searched[:discard_comma])
