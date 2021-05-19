

print("Number Of Classes held")
classes_held= int (input())
print("Number Of Classs atten")
classes_attend= int (input())

print("Percentage of classes attend")
percentage = float ((classes_attend/classes_held)*100)
print(percentage)

if percentage >= 75:
    print("Student can sit in examination hall")
else:
    print("Student can not sit in examination hall")


