#DNA Reverse Complement

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


def complement(s):
    length = len(s)
    newst = ""
    for i in range(length):
        if s[i]=='A':
            newst = newst + 'T'
        elif s[i]=='T':
            newst = newst + 'A'
        elif s[i]=='C':
            newst = newst + 'G'
        else:
            newst = newst + 'C'
    
    return newst


def DRC():
    print("Enter the DNA string ", end="")
    st = input()
    for c in st:
        if c=='A' or c=='C' or c=='G' or c=='T':
            continue
        else:
            print("Please enter valid DNA string")
            return
    
    new_st = reverse(st)

    new_st = complement(new_st)

    print("DNA after complement is", new_st)




DRC()