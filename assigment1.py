print("how many class are held")
clas = int(input())

print("how many class were you attend")
attend = int(input())

percantage = attend/clas*100
print("your percantage is",percantage,"%")

if percantage >75:
    print("you are allow to set in exame \n Thank you")

else:
    print("your are not aloow to set in exame \n thank you")