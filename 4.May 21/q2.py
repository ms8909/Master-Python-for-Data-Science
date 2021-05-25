flong = 6
fwide = 4
plong = 2
pwide = 3

print (flong)
print (fwide)
print (plong)
print (pwide)

print ("*"*flong)
print ("*"*fwide)
print ("*"*plong)
print ("*"*pwide)

for a in range (fwide):
    print ("*"*flong)
for a in range (pwide):
    print ("*"*plong)
