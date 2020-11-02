subject = int(input("Input your marks"))
if subject == 100:
    print("excellent")
elif subject >= 80 and subject <100:
    print("very good")
elif subject >= 60 and subject< 80:
    print("good")
    #do for 50-60 -fair
    #<50 - fail
else:
    print("invalid marks")