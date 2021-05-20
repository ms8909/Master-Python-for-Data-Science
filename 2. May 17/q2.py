total_class=int(input("Enter the total number of classes"))
attended_class=int(input("Enter the number of attended classes : "))
percentage_of_classes=(attended_class/total_class)*100
print("percentage of classes is:")
print(percentage_of_classes)
if percentage_of_classes<75:
  print("NO!..He/She will not attowed to sit in the exam")
else:
    print("Yes!..He/She is attowed to sit in the exam")