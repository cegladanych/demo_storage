from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.core.exceptions import ResourceNotFoundError
import os

connect_str = ''
container_name = 'projectx'
local_path = 'C:\\Users\\admin\\Downloads\\json'

# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string(connect_str)


# Create the container
try:
    container_client = blob_service_client.create_container(container_name)
except Exception:
    pass

directory = os.fsencode(local_path)

for file in os.listdir(directory):
    local_file_name = os.fsdecode(file)
    # # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    full_path_to_file = os.path.join(local_path, local_file_name)

    #upload files
    with open(full_path_to_file, "rb") as data:
        blob_client.upload_blob(data)