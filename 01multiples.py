# i = 1
# while i <= 100:
#     if i % 3 == 0 and i % 5 == 0:
#         print("ThreeFive")
#     elif i % 3 == 0:
#         print("Three")
#     elif i % 5 == 0:
#         print("Five")
#     else:
#         print(i)
#     i = i + 1

for i in range(1, 101):
    if i % 3 == 0:
        if i % 5 == 0:
            print("ThreeFive")
        else:
            print("Three")
    else:
        if i % 5 ==0:
            print("Five")
        else:
            print(i)
