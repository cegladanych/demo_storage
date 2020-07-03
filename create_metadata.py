import csv
import uuid
from datetime import datetime

for r in range(10):
    PartitionKey = "File_%s" %r
    RowKey = uuid.uuid4().hex
    TimeStamp = datetime.now()
    Metadata = {'PartitionKey':'somevalkue','RowKey':'002',
        'description':'this is description text','priority':200}
    print(Metadata)