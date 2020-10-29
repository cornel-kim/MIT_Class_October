#student marks
english = int(input("Please input your English marks:"))
kiswahili = int(input("Please input your Kiswahili marks:"))
math = int(input("Please input your mathemathics marks:"))
TotalMarks= english + kiswahili + math
print("The student scored",TotalMarks,"marks")

#simple interest-= (rate * time * amount)/100
Amount = int(input("Please input the principle amount:"))
time = float(input("Please input the period/time:"))
rate = int(input("Please input the rate:"))/100
simpleInterest = (Amount * rate * time)/100
print("Simple interest is",simpleInterest)