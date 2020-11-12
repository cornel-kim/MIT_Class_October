#an ATM Machine Function
def ATM(bank_balance, deposit_amount, withdrawal):
    pin = 2345
    Total_balance_deposit = bank_balance + deposit_amount
    Total_balance_withdrawal = Total_balance_deposit - withdrawal
    if deposit_amount:
        print("Your total balance is:", Total_balance_deposit)
        if withdrawal < Total_balance_deposit:
            print("withdrawal is successful", "new balance is", Total_balance_withdrawal)
        else:
            print("The balance is not enough")
    elif not deposit_amount:#else if deposit amount == null
        print(bank_balance)
        if withdrawal < Total_balance_deposit:
            print("withdrawal is successful")
        else:
            print("The balance is not enough")
    else:
        print("error please try again")


ATM(deposit_amount=3000, withdrawal=1000, bank_balance=4000)
ATM(deposit_amount=500, withdrawal=5000, bank_balance=4500)
ATM(deposit_amount=0, withdrawal=5000, bank_balance=0)

#BMI is calculated using this formula BMI = weight/height.Using python function create
#a python function with parameters and arguments to calculate BMI. Give recomendations
#for each index i.e obesse, underweight and healthy