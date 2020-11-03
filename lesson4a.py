#loops-while loop, for loop.
#number from 0 to 50
# number = 0
# while number <= 50:
#     print(number)
#     number = number + 3#incrementing factor for while loop



attemps = 0
while attemps < 3:
    attemps = attemps + 1
    password = int(input("input your password:"))

    if password == 1234:
        print("login successful")
        break;
    else:
        print("wrong password")
        continue;



