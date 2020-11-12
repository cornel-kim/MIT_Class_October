#an ATM Machine Function
def ATM():
    bank_balance = 5000
    pin = 2345
    deposit_amount = 4000
    withdrawal = 2000
    Total_balance_deposit = bank_balance + deposit_amount
    Total_balance_withdrawal = bank_balance - withdrawal
    if deposit_amount:
        print("Your total balance is:", Total_balance_deposit)
        if withdrawal < Total_balance_deposit:
            print("withdrawal is successful")
        else:
            print("The balance is not enough")
    elif not deposit_amount:
        print(bank_balance)
        if withdrawal < Total_balance_deposit:
            print("withdrawal is successful")
        else:
            print("The balance is not enough")
    else:
        print("error please try again")


ATM()