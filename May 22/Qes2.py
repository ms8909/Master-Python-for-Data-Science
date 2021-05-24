def flag(a,b,c,d):
    for i in range(a):
        print("*"*b)
    for g in range(c):
        print("*"*d)


flong=int(input("how long is your flag:"))
fwide=int(input("how wide is your flag:"))

plong=int(input("how long is your flagpoles:"))
pwide=int(input("how wide is your flagpoles:"))
flag(flong,fwide,plong,pwide)
