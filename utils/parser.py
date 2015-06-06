import csv
import json

with open('data/t17_02.dat','rb') as csvfile:
	datreader = csv.reader(csvfile,delimiter=' ',quoting=csv.QUOTE_NONE)
	with open('data/t17_02.json','w') as jsonfile:
		items = []
		for row in datreader:
			frow = [float(v) for v in row]
			items.append(frow)
		jsonfile.write(json.dumps(items))
		