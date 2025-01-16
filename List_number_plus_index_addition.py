# A script that returns a list but with each elements index in the list added to itself

list = [0, 3, 5, 9, 12, 13]
new_list = []

i = 0
while i < len(list):
    number = int(list[i]) + i
    new_list.append(number)
    i = i + 1

print(new_list)