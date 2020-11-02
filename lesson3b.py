#nested if else statements
Account = input("Please input the account number:")
Amount = int(input("Please input the amount or airtime:"))
Pin = int(input("Input valid pin:"))
if Amount > 0:
    if Pin == 3000:
        print("You have bought the airtime successfuly")
    else:
        print("invalid pin")

else:
    print("input valid amount")
