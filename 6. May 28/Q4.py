def sub_cipher(m,o):
    msg = []
    for i in m :
        
        sub = ord(i)
        sub = sub + o
        sub = chr(sub)
        msg.append(sub)

    cipher = "".join(msg)
    return(cipher)


message = input("Enter your message : ")
offset = int (input("Enter the number of offset : "))

print("Your cipher substitution is : ",sub_cipher(message,offset))

