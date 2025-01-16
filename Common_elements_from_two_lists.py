# Write a script that reads two lists and returns a list of common elements

List_1 = [-1, 3, 4, 6, 7, 9]
List_2 = [-1, 2, 7]
common = []

for number in List_1:
    if number in List_2:
        common.append(number)

print(common)
