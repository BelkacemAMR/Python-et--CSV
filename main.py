import csv
import datetime
from datetime import datetime

########################### Fonction  generate_csv   ################################################################

def generate_csv(data):
    keys = [key for key, value in data[0]]

    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()

        for row in data:
            row_data = {}
            for key, value in row:

                if key == 'date':
                    value = value.strftime('%m/%d/%Y')


                elif isinstance(value, (list, tuple)):
                    value = ",".join(value)
                row_data[key] = value
            writer.writerow(row_data)

#########################  Fonction parse_csv ##################################################


def parse_csv():
    students = []
    with open('students.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student = {}
            for key, value in row.items():
                if key == 'Birthdate':
                    student[key] = datetime.strptime(value, '%m/%d/%Y').date()
                elif key == 'Marks':
                    student[key] = [int(mark) for mark in value.split(',')]
                else:
                    student[key] = value
            students.append(student)
    return students
