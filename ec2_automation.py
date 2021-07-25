import boto3

client = boto3.client('ec2',aws_access_key_id = "", aws_secret_access_key = "")
response = client.describe_instances()
#print(response['Reservations'])
for ec2_id in response['Reservations']:
   # print(ec2_id['Instances'])
    for ec2_instance_id in ec2_id['Instances']:
       # print(ec2_instance_id['InstanceId'])
        ec2_instanceid=ec2_instance_id['InstanceId']



image_id = client.create_image(
    InstanceId=ec2_instanceid,
    Name='secondiamge6'
)
print(image_id)
