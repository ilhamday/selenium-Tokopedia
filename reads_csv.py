import csv
import pandas as pd

# with open('result_toped.csv', 'r') as csv_file:
#     # csv_read = csv.reader(csv_file)
#     csv_read = csv.DictReader(csv_file)
#
#     for line in csv_read:
#         # print(line[1])
#         print(line['Product Name'])

data = pd.read_excel('parameter.xlsx')
df = pd.DataFrame(data, columns=['Barang'])
print(data['Barang'])