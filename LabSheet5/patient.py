
class Patient:
    def __init__(self, name, phone, dob):
        self.name = name
        self.phone = phone
        self.dob = dob

    def generate_id(self):
        id_output = ""
        id_output += self.name[0].lower()

        # Date of Birth

        id_output += self.dob

        # Last digits phone number
        number = str(self.phone)
        last_three_num_phone_number = ""
        i = -1
        while i > -4:
            last_three_num_phone_number += number[i]
            i = i - 1

        id_output += last_three_num_phone_number[::-1]

        # first letter last name
        name = self.name.split()
        last_name = name[1]
        id_output += last_name[0].upper()

        return id_output

    def get_age_bracket(self):
        year = int(self.dob[-4:])
        if year > 2006:
            return "minor"
        elif year < 1959:
            return "senior"
        else:
            return "adult"

# name = input('Enter name:')
# phone_no = input('Enter phone no:')
# dob = input('Enter date of birth:')
# patient = Patient(name,phone_no,dob)
# print('Patient id is ' + patient.generate_id())
# print('Age bracket is ' + patient.get_age_bracket())