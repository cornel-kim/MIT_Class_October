def simpleInterest():
    base_value = int(input("Input your principle amount: ksh "))
    rate = int(input("Input your banks rates per annum: "))
    time = int(input("input the duration for the loan: "))
    simple_interets = (base_value * rate * time)/100
    print("Simple interest is ksh", simple_interets)


simpleInterest()