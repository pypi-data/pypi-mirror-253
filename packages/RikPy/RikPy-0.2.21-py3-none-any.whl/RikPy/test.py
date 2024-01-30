from commonheroku import heroku_upload_file_from_url, heroku_list_files_in_folder, heroku_download_files_in_folder, heroku_delete_file
from commonshopify import Shopify_get_metaobject_gid, Shopify_update_metaobject
from commons3 import s3_list_files_in_folder, s3_environment, s3_upload_local_file, s3_delete_file, s3_upload_file_from_url
import boto3

s3_config_dict = s3_environment()
objects = s3_list_files_in_folder(folder_name="public", s3_config_dict=s3_config_dict)

file_url="https://cloud-cube-eu2.s3.amazonaws.com/wwmx700brb7g/public/dogs/16264433-d3aa-4dbd-8318-722bde7ca2bb.png"

local_file_path = '.gitignore'
folder_name="public/wine"
#response=s3_upload_local_file(file_name=local_file_path, folder_name=folder_name, s3_config_dict=s3_config_dict)
#print(response)
#object_key=folder_name+"/"+local_file_path
#s3_delete_file(object_key=object_key, s3_config_dict=s3_config_dict)

object_key = s3_upload_file_from_url(file_url=file_url, folder_name=folder_name, s3_config_dict=s3_config_dict, bnewname=True, make_public=False)
print(object_key)
exit()

shop = '9d9853'
access_token = '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'
metaobject_type = 'product_banner'
handle = 'aiir-banner'

heroku_config_dict={
    'CLOUDCUBE_ACCESS_KEY_ID': 'AKIA37SVVXBH5W3TYBNK', 
    'CLOUDCUBE_SECRET_ACCESS_KEY': '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', 
    'CLOUDCUBE_URL': 'https://cloud-cube-eu2.s3.amazonaws.com/wwmx700brb7g', 
    'HEROKU_API_KEY': '7c90a74f-3971-4f51-a0cc-d343775e11a7', 
    'HEROKU_APP_NAME': 'aiir', 
    'CUBE_NAME': 'wwmx700brb7g', 
    'CUBE_PUBLIC': 'wwmx700brb7g/public/', 
    'BUCKET_NAME': "cloud-cube-eu2"
}

folder = "Marieprivate"
file_key ="wwmx700brb7g/public/Marieprivate/20240118120918_d26979bb.png"

bucket_name = heroku_config_dict['BUCKET_NAME']
file_key ="/public/Marieprivate/20240118120918_d26979bb.png"
CLOUDCUBE_ACCESS_KEY_ID= heroku_config_dict['CLOUDCUBE_ACCESS_KEY_ID']
CLOUDCUBE_SECRET_ACCESS_KEY= heroku_config_dict['CLOUDCUBE_SECRET_ACCESS_KEY']

s3_client = boto3.client(
            's3',
            aws_access_key_id=CLOUDCUBE_ACCESS_KEY_ID,
            aws_secret_access_key=CLOUDCUBE_SECRET_ACCESS_KEY
        )
print(s3_client)

response = s3_client.get_object_acl(Bucket=bucket_name, Key=file_key)

# Print the object's current access control
print(f"Access control for '{file_key}' in bucket '{bucket_name}':")
for grant in response['Grants']:
    print(grant)

exit()

response = s3_client.delete_object(Bucket=bucket_name, Key=file_key)
print(response)

# files=heroku_list_files_in_folder(folder_name=folder, heroku_config_dict=heroku_config_dict)

# heroku_download_files_in_folder(folder_name=folder, heroku_config_dict=heroku_config_dict, bdelete=True)
# response = heroku_delete_file(file_key=file_key, heroku_config_dict=heroku_config_dict)
print(response)


# Test the function with your URLs
# dallefile = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-4crfjbsW4FCdUgyk3a8GcUvR/user-ECHPMxvKeRuTQtLTHCu5qaAU/img-RRsviiNw6uHPUbA9sdabkJOy.png?st=2024-01-17T11%3A00%3A43Z&se=2024-01-17T13%3A00%3A43Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-01-16T22%3A43%3A45Z&ske=2024-01-17T22%3A43%3A45Z&sks=b&skv=2021-08-06&sig=qHOicaZMXphFlcsjPsyESiCGqkmmb9n5T44VzxlkeXw%3D"
# leonardofile = "https://cdn.leonardo.ai/users/d71165a1-5a13-415e-af90-543e909ea431/generations/bb54ed78-07cd-4de1-8578-512584c07e0b/Leonardo_Diffusion_XL_Create_an_abstract_image_featuring_lusci_0.jpg"
# leonardofile = "https://cdn.leonardo.ai/users/d71165a1-5a13-415e-af90-543e909ea431/generations/ce677c1a-f1da-4fa8-a607-b81779800fef/Leonardo_Diffusion_XL_Create_an_oil_paintingstyle_image_inspir_0.jpg"

# heroku_upload_file_from_url(file_url=leonardofile, folder="borrar", bnewname=True)

# product_post_image="https://files.canvas.switchboard.ai/4ea249ec-1808-4a19-afd7-0a251a8d8aaf/dea12574-80f5-4b72-a853-8c9a8d40fc9f.png"
# profile_topic="wine"
# response=heroku_upload_file_from_url(product_post_image, profile_topic, heroku_config_dict)
# print(response)
