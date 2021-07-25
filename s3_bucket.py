import boto3

client = boto3.client('s3',aws_access_key_id = "", aws_secret_access_key = "")

#list bucket-name

list_bkt = client.list_buckets()
for bkt_name in list_bkt['Buckets']:
    bkt_location = client.get_bucket_location(Bucket=bkt_name['Name'])
    print(bkt_name['Name'], bkt_location['LocationConstraint'])
