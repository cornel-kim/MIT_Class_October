def simpleInterest(base_value, rate, time):#parameters-base_value, rate and time
    # base_value = int(input("Input your principle amount: ksh "))
    # rate = int(input("Input your banks rates per annum: "))
    # time = int(input("input the duration for the loan: "))
    simple_interets = (base_value * rate * time)/100
    print("Simple interest is ksh", simple_interets)


simpleInterest(base_value=3000, rate=8, time=2)#base_value=3000, rate=8,
# time=2 are all arguments