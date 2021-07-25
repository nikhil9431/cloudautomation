import boto3
from datetime import date, datetime,timedelta,timezone
client = boto3.client('iam', aws_access_key_id = "", aws_secret_access_key = "")

#List users

listuser_response = client.list_users()
#print(listuser_response['Users'])
for i in listuser_response['Users']:
    iam_users=(i['UserName'])
    print(iam_users)


# access key date

list_access_key = client.list_access_keys(UserName=iam_users)
#print(list_access_key['AccessKeyMetadata'])   
for j in list_access_key['AccessKeyMetadata']:
    iam_users_created_date= j['CreateDate']
    print(iam_users, iam_users_created_date)


current_date= datetime.now(timezone.utc)
    #print(current_date)

age = (current_date-iam_users_created_date).days
print(iam_users,age)