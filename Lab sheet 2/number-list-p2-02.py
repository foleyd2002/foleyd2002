
number = 0

Dups_list = []
while number != -1:
    number = int(input("Please enter a number (-1 to stop):"))
    if number != -1:
        Dups_list.append(number)
    else:
        print(sorted(list(set(Dups_list))))



