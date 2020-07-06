from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
import csv


account_name = ''
accoun_key = ''
table_name = 'projectx'
file_name = 'C:\\Users\\admin\\Downloads\\meta.csv'

def set_table_service():
    return TableService(account_name,accoun_key)

def get_table_service():
    return  ts.exists(table_name,10)

ts = set_table_service()

if get_table_service() == False:
    ts.create_table(table_name)


csvFile = open(file_name, 'r')
field_names = ('PartitionKey','RowKey','TimeStamp','UpdatedOn','ID','Priority')
reader = csv.DictReader(csvFile)
rows = [row for row in reader]
for row in rows:
    index = rows.index(row)
    ts.insert_or_replace_entity(table_name,row)

