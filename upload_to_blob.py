from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

connect_str = 'BlobEndpoint=https://devopscegladanychsa.blob.core.windows.net/?sv=2019-10-10&ss=bfqt&srt=sco&sp=rwdlacupx&se=2020-07-10T13:47:24Z&st=2020-07-08T05:47:24Z&spr=https&sig=oYflf4cQqqJrwQaDOPGt7ZcePFaSWNa1hxLM6CJKDvY%3D'
container_name = 'projectx'
# local_file_name = '00d8ee562ff3436aa5ce0c5c41f4826d.json'
local_path = 'C:\\Users\\admin\\Downloads\\json'

# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string(connect_str)


# Create the container
container_client = blob_service_client.create_container(container_name)

directory = os.fsencode(local_path)

for file in os.listdir(directory):
    local_file_name = os.fsdecode(file)
    # # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    full_path_to_file = os.path.join(local_path, local_file_name)

    #upload files
    with open(full_path_to_file, "rb") as data:
        blob_client.upload_blob(data)