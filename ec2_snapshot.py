import boto3

client = boto3.client('ec2',aws_access_key_id = "", aws_secret_access_key = "")
response = client.describe_snapshots()
print(response)