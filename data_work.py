import csv

def save_data(data, file_name):

    print('SAVING TO FILE:', file_name)

    with open(file_name, mode='w', encoding='utf8') as csv_file:

        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())

        writer.writeheader()

        for row in data:
            writer.writerow(row)