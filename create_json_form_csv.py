import csv, json

csv_file_name = 'C:\\Users\\admin\\Downloads\\meta2.csv'
json_file_name = 'C:\\Users\\admin\\Downloads\\meta.json'
json_data = {}


with open(csv_file_name,'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for row in csvReader:
        # print(row)
        FileName = row['RowKey']
        json_data = row
        with open('C:\\Users\\admin\\Downloads\\' + FileName +'.json','w') as jsonFile:
            jsonFile.write(json.dumps(json_data,indent=4))

