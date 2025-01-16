name = input("What is your name?")
number = int(input("What is your phone number?"))
DOB = input("What is your date of birth (format is ddmmyyyy)?")
while len(DOB) != 8 or not DOB.isdigit():
    print("Incorrect format")
    DOB = input("What is your date of birth (format is ddmmyyyy)?")

id_output = ""
id_output += name[0].lower()

id_output += DOB

#phone number
number = str(number)
last_three_num_phone_number = ""
i = -1
while i > -4:
    last_three_num_phone_number += number[i]
    i = i - 1

id_output += last_three_num_phone_number[::-1]

# first letter last name
name = name.split()
last_name = name[1]
id_output += last_name[0].upper()

print("Your patient id is "+ id_output)




