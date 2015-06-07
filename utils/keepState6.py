import json

with open("../js/counties.geojson","rb") as jsonfile:
	jsonresult = json.loads(jsonfile.read())
	
	jsonresult["features"] = [feature for feature in jsonresult["features"] if feature["properties"]["STATE"] == "06"]
	
	with open("../js/filteredcounties.geojson","w") as outfile:
		outfile.write(json.dumps(jsonresult))