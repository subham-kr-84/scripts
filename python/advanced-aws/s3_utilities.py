import boto3

s3 = boto3.client('s3')   #creating a client for s3 so that it can call api
response = s3.list_buckets()

# print(type(response))

for bucket in response["Buckets"]:
  print(f'  {bucket["Name"]}')

