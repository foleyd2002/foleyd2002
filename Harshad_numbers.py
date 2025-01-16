# A number is said to be Harshad if it is divisible by the sum of its digits

number = input()
number_list = []

i = 0
while i < len(number):
    number_list.append(number[i])
    i = i + 1

original = int(number)

total = 0
for char in number_list:
    total = int(char) + total

if original % total == 0:
    print("True")
else:
    print("False")
