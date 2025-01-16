number = 0
list_nums = []

while number != -1:
    number = int(input("Please enter a number (-1 to stop):"))
    if number != -1:
        list_nums.append(number)
    else:
        occurrences = {}

        for num in list_nums:
            if num in occurrences:
                occurrences[num] += 1
            else:
                occurrences[num] = 1

        unique_numbers = list(set(list_nums))
        print(list(occurrences.keys()))

        for num in unique_numbers:

            print(f"{num} occurred {occurrences[num]} times")