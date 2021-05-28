def list_to_dict(a,b):
    j=0
    c=[]
    for i in a:        
        d={"name":i,"age":b[j]}
        j=j+1
        c.append(d)
    return c


names= ["alan", "john", "tania", "ahmad", "ali", "muddassar", "raheel", "hamza"]
age= [12,13,14,15,17,16,13,13]
dic = list_to_dict(names,age)
print(dic)