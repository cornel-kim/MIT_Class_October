#function to check if number is positive or negative
def number():
    my_number = int(input("Insert your number:"))
    if my_number > 0:
        print("number is positive")
    elif my_number == 0:
        print("Number is zero")
    else:
        print("Number is negative")


number()


def myList():
    towns = ["Nairobi", "Kisumu", "Eldoret", "Mombasa", "Machakos"]
    for town in towns:
        print(town)

myList()