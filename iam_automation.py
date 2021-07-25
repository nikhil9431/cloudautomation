import boto3
from datetime import date, datetime,timedelta,timezone
import csv
import os
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def access_key_age( writer):
    iam_report={}
    client = boto3.client('iam', aws_access_key_id = "", aws_secret_access_key = "")

#List users

    listuser_response = client.list_users()
    print(listuser_response['Users'])
    for i in listuser_response['Users']:
     iam_users=(i['UserName'])

# access key date

     list_access_key = client.list_access_keys(UserName=iam_users)
#print(list_access_key['AccessKeyMetadata'])   
     for j in list_access_key['AccessKeyMetadata']:
       iam_users_created_date= j['CreateDate']

    current_date= datetime.now(timezone.utc)
    #print(current_date)

    age = (current_date-iam_users_created_date).days
    print(iam_users,age)

    if(age>1):
        #print(iam_users,age)
        iam_report["UserName"]=iam_users
        iam_report["Age"]=age
        iam_report["Created_date"]=iam_users_created_date
        writer.writerow(iam_report)

def sending_email(file_name):
    SENDER = "qualitysweet19@gmail.com"
    RECIPIENT =""
    SUBJECT=""
    ATTACHMENT=""
    BODY_HTML= """
    <html>
    <head></head>
    <body>
    <h3>Hi all</h3>
    <p>please see the attachement of days access key</p>
    </body>
    </html>
    """
    

    
    def main():
        fieldnames = ["UserName","Age","Created_date"]
        file_name = "iam_report.csv"
        with open (file_name,"w",newline='') as csv_file:
            writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
            writer.writeheader()

        access_key_age( writer)
        sending_email(file_name)

    main()

