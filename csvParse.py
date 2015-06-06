import csv
import json

csvfile = open('incomeCounties.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("StateFIPS","CountyFIPS","PostalCode","MedianIncome")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')