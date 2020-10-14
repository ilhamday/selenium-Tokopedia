import csv

with open('result_toped.csv', 'r') as csv_file:
    # csv_read = csv.reader(csv_file)
    csv_read = csv.DictReader(csv_file)

    for line in csv_read:
        # print(line[1])
        print(line['Product Name'])