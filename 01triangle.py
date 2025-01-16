a = int(input())
b = int(input())
c = int(input())
input_list = [a, b, c]

if len(set(input_list)) == 1:
    print("equilateral")
elif len(set(input_list)) == 2:
    print("isosceles")
else:
    print("neither")