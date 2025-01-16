
def get_year(patient_id):
    year = int(patient_id[1:5])
    return year

def is_valid_id(patient_id):
    if len(patient_id) != 13:
        return False

    if not patient_id[0].islower() or not patient_id[-1].isupper():
        return False

    if not patient_id[1:12].isdigit():
        return False

    return True

def check_id(patient_ids = []):
    return all(is_valid_id(patient_id) for patient_id in patient_ids)
