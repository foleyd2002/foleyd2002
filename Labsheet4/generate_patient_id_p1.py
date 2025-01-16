def patient_id(name, number, DOB):
    id_output = ""
    id_output += name[0].lower()

    #Date of Birth

    id_output += DOB

    # Last digits phone number
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

    return f"Your patient id is {id_output}"



name_patient = input("What is your name?")
phone_number = int(input("What is your phone number?"))
date_of_birth = input("What is your date of birth (format is ddmmyyyy)?")
print(patient_id(name_patient, phone_number, date_of_birth))