import csv, json

csv_file_name = 'C:\\Users\\admin\\Downloads\\projectx2.csv'
json_file_name = 'C:\\Users\\admin\\Downloads\\meta.json'
json_data = {}


with open(csv_file_name,'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    field_names = ('PartitionKey','RowKey','TimeStamp','UpdatedOn','ID','Priority')
    for row in csvReader:
        # print(row)
        FileName = row['RowKey']
        json_data['PartitionKey']= row['PartitionKey']
        json_data['RowKey'] = row['RowKey']
        json_data['TimeStamp'] = row['TimeStamp']
        json_data['UpdatedOn'] = row['UpdatedOn']
        json_data['ID'] = row['ID']
        json_data['Priority'] = row['Priority']

        #json_data = row
        with open('C:\\Users\\admin\\Downloads\\json\\' + FileName +'.json','w') as jsonFile:
            jsonFile.write(json.dumps(json_data,indent=4))

