import csv
import datetime


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



