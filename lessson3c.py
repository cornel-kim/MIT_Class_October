#if else and elif statements
student_marks = int(input("please input your marks:"))
if student_marks > 90 and student_marks < 100:
    print("Excellent")
elif student_marks > 75 and student_marks <=90:
    print("Good")
elif student_marks > 60 and student_marks <=75:
    print("Fair")
elif student_marks > 50 and student_marks <= 60:
    print("pass")
elif student_marks <=50 and student_marks > 0:
    print("Fail")
else:
    print("input valid marks")

#create a program, i. e an ATM machhine thats checks user pin and card number
#create a program using student marks to give recomendation for choice of highschool
#i.e over 380 marks join national, over 320 marks join extra county, over 250 marks
# join county schools and less than 250 join local