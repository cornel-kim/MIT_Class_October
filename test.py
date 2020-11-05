# return sum
def sum_list():
    list = [5,6,5,2,8]
    totals = sum(list)
    print("The sum of five items is  is", totals )


sum_list()



def num_range():
    numbers = 0
    while numbers <= 100:
        print(numbers)
        numbers = numbers + 1
        total = sum(numbers)
        if total%2 != 0 and total%3 != 0:
            print("The total is unique")

        else:
            print("number is not unique")



num_range()


