import csv
import json
import copy
import simplejson

csvfile = open('../data/incomeCounties.csv','rb')
csvreader = csv.DictReader(csvfile)

csvfile2 = open('../data/conreport2013.csv','rb')
csvreader2 = csv.DictReader(csvfile2)


jsonfile = open('../data/incomeCounties.json','w')

items = []

for row in csvreader:
	if row["Postal Code"] == "CA":
		items.append(row)
jsonfile.write(json.dumps(items))


csvfile.close()
jsonfile.close()

jsonfile = open('../data/airCounties.json','wb')

items = []
for row2 in csvreader2:	
	countyCode = int(row2["County Code"])
	if countyCode >= 6000 and countyCode < 7000:			
		row2["County Code"] = row2["County Code"].lstrip("6")
		for kv in row2:
			#print kv
			if row2[kv] == ".":
				row2[kv] = row2[kv].replace(".","0")
		items.append(row2)
jsonfile.write(json.dumps(items,False,))


csvfile2.close()
jsonfile.close()

geojsonfile = open("../js/filteredcounties.geojson","rb")
airjsonfile = open("../data/airCounties.json","r")
incomejsonfile = open("../data/incomeCounties.json","rb")
combinedjsonfile = open("../js/filteredCAdata.geojson","w")

airdata = simplejson.loads(airjsonfile.read())
incomedata = simplejson.loads(incomejsonfile.read())
geodata = json.loads(geojsonfile.read())

for item in geodata["features"]:
	if item["type"] == "Feature" and item["properties"] != None:
 		county = int(item["properties"]["COUNTY"])
 		for air in airdata:
 			if int(air["County Code"]) == county:
 				item["properties"].update(air)		
 		for income in incomedata:
 			if int(income["County FIPS Code"]) == county:
 				item["properties"].update(income)
 
combinedjsonfile.write(json.dumps(geodata))

geojsonfile.close()
airjsonfile.close()
incomejsonfile.close()
combinedjsonfile.close()