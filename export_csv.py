import csv

def export_csv():

    with open('result_toped.csv', 'w', newline='') as csvfile:
        # using csv writer ---
        # writer = csv.writer(csvfile)
        # writer.writerow(['Index','Product Name'])

        # using csv Dictwriter ---
        fieldnames = ['Index', 'Product Name']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        csv_writer.writeheader()