age_input = int(input("Please enter your age:"))
basic_price = 0.75
price = 0
if age_input < 5:
    print("You go free!")
elif age_input >=5 and age_input <= 16:
    price += basic_price
    print(f"Your fare is: {price} euro.")
elif age_input >= 17 and age_input <= 20:
    price = basic_price + 0.5
    print(f"Your fare is: {price} euro.")
elif age_input >= 21 and age_input <= 64:
    price = basic_price + 0.75
    print(f"Your fare is: {price} euro.")
else:
    print("You go free!")