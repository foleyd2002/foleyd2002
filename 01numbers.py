print("Enter a number:")
n = int(input())
number = n
sum = 0

print(number)
while number > 0:
    sum = sum + number
    number = number -1
    print(number)
print("")
print(sum)