#Change Data Structures




names= ['alan', 'john', 'tania', 'ahmad', 'ali', 'muddassar', 'raheel', 'hamza']
age= [12,13,14,15,17,16,13,13]



length = len(names)

new = [{}]*len(names)

for i in range(length):
    # print(i)
    dic = {"name":names[i],"age":age[i]}
    new[i] = dic


print(new)


