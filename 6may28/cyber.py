# Cyber Security: substitution cipher

def Sub_Cypher(Offset,Message):
    Shift=""
    for i in Message:
        g=ord(i)
        g=g+Offset
        # This will check if ascii if greater then z so i will bring ascii back to a
        if(g>ord("z")):
            g=g-26
        # This will check if ascii if greater then Z and less then a so i will bring ascii back to A
        elif(g>ord("Z") and g<97):
            g=g-26
        g=chr(g)
        Shift=Shift+g
    return Shift

#Main Function
Offset=int(input("Numeric Offset: "))
M=input("Message: ")
Msg=Sub_Cypher(Offset,M)
print("Shifted Message: ",Msg)