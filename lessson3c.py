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