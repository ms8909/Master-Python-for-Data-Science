print('Please enter Total Number of Classes Held')
Classes_held= int (input())
print('Please enter Total Number of Classes Attended')
Classes_attended= int(input())

attendance = int((Classes_attended/Classes_held)*100)
if attendance >= 75 and attendance <= 100:
    print ('You Have Attended '+ str(attendance) + '% of the Classes. You Can sit in the Exam.')
elif attendance > 100:
    print('Please enter valid number for Classes Attended')
elif attendance < 75:
    print ('Have you applied for Medical leave? Type Yes/ No')
    Medical_leave = str (input())
    print ('You Have Attended only '+ str (attendance) + '% of the Classes. But, you are conditionally allowed to sit in the Exam')
else:
    print('You Have Attended only '+ str (attendance) + '% of the Classes. You Cant sit in the Exam.')