# count all character 
# to replace specify count

# st = 'TGGCCCAAAA'
# s=st.replace('A','T',4)
# s1=s.replace('C','G',3)
# s2=s1.replace('G','C',2)
# s3=s2.replace('T','A',1)

def reverse(s):
    st=''
    for i in s:
        st=i+st
    return st

def complement(s):
    li = list(s)
    count=0
    for i in li:
        if i=='T':
            li[count]='A'
        elif i=='G':
            li[count]='C'
        elif i=='C':
            li[count]='G'
        elif i=='A':
            li[count]='T'            
        count+=1
    st=''

    return st.join(li)


st = input("Enter a DNA String : ")
invalid=False
for i in st:
    if i!='A' or i!='G' or i!='C' or i!='T':
            invalid=True
            break
if invalid==True:
    st=reverse(st)
    print(complement(st))
else:
    print("The string is invalid")    