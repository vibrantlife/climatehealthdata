import csv
import json

with open('../data/incomeCounties.csv','rb') as csvfile:
	csvreader = csv.DictReader(csvfile)
	with open('../data/incomeCountiesCA.json','w') as jsonfile:
		items = []
		for row in csvreader:
			if row["Postal Code"] == "CA":
				items.append(row)
		jsonfile.write(json.dumps(items))