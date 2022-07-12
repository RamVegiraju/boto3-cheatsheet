import boto3
s3 = boto3.resource('s3')

def upload_file():
  return response = s3.meta.client.upload_file('file.txt', 'bucket-name', 'key/file.txt')
