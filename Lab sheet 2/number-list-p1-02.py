number = 0
list = []
while number != -1:
    number = int(input("Please enter a number (-1 to stop):"))
    if number != -1:
        list.append(number)
    else:
        print(list)