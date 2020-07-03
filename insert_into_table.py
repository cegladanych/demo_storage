from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

account_name = ''
accoun_key = ''
table_name = ''

def set_table_service():
    return TableService(account_name,accoun_key)

def get_table_service():
    return  ts.exists(table_name,10)

ts = set_table_service()

if get_table_service() == False:
    ts.create_table(table_name)

def load_csv(ts):
    csvFile = open(csvFile, 'r')
field_names = ('TimeStamp','Metadata')
reader = csv.DictReader(csvFile)
rows = [row for row in reader]
for row in rows:
    index = rows.index(row)
    row['PartitionKey'] = '1'
    row['RowKey'] = '%08d' % index
    ts.insert_or_replace_entity(table_name,row)

task = {'PartitionKey':'somevalkue','RowKey':'002',
        'description':'this is description text','priority':200}

ts.insert_entity(table_name,task)
