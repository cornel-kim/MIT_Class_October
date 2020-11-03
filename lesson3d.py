subject = int(input("Input your marks"))
if subject == 100:
    print("excellent")
elif 80 <= subject < 100:
    print("very good")

elif 60<= subject <80:
    print("good")
    #do for 50-60 -fair
    #<50 - fail
else:
    print("invalid marks")