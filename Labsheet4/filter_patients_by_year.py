import sys


def filter_patients_by_year(patients_file, year_file):
    # Read the patient IDs from the first file
    with open(patients_file, 'r') as f:
        patient_ids = f.read().splitlines()

    # Read the year from the second file
    with open(year_file, 'r') as f:
        year = f.read().strip()

    # Filter patient IDs born in the specified year
    patients_born_in_year = [patient_id for patient_id in patient_ids if patient_id[5:9] == year]

    # Print the results
    if patients_born_in_year:
        print("Here are all the patients born in {0}:".format(year))
        print(patients_born_in_year)
    else:
        print("There are no patients born that year.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python filter_patients_by_year.py <patients_file> <year_file>")
        sys.exit(1)

    patients_file = sys.argv[1]
    year_file = sys.argv[2]

    filter_patients_by_year(patients_file, year_file)
