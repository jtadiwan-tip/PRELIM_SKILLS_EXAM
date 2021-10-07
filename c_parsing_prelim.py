import json
import pandas

read_json = open('covid_cases.json',)

conv_file = json.load(read_json)

for i in conv_file['records']:
    parsed_file = (i['dateRep'], i['countriesAndTerritories'], i['cases'], i['deaths'])
    print(parsed_file)



    
read_json.close()

