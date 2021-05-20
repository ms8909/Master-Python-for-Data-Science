print("number of classes held")
classes_held= int(input())
print("Number of classes attend")
classes_attend= int(input())

print("percentage of classes attend")
percentage = float ((classes_attend/classes_held)*100)
print(percentage)

if percentage >=43:
    print("student can sit in examination hall")
else:
    print("student can not sit in examination hall")
