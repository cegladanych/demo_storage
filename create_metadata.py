import csv
import uuid
from datetime import datetime
from random import random

file_name = 'C:\\Users\\admin\\Downloads\\meta.csv'

with open(file_name,'w',newline='') as file:

    for r in range(300000):
        PartitionKey = "File_%s" %r
        RowKey = uuid.uuid4().hex
        TimeStamp = datetime.now()
        UpdatedOn = TimeStamp.timestamp()
        ID = '00%s'%r
        Priority = random()  
        writer = csv.writer(file)
        writer.writerow([PartitionKey,RowKey,TimeStamp,UpdatedOn,ID,Priority])

