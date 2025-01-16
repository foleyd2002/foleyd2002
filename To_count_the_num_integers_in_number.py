# Write a script to count the number of integers in a number, without using strings

n = int(input())

if n <= -1:
    n = n * -1

i = 0
while n >= 1:
    n = n // 10
    i = i + 1

print(i)
