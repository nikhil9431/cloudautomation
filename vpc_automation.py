# Python Code to automate AWS VPC full setup
import boto3

client = boto3.client('ec2', region_name="us-east-1", aws_access_key_id = "", aws_secret_access_key = "")

# VPC Creation
print ("Enter the VPC CIDR Value: ")
vpc_cidr = input()
VPC_response = client.create_vpc(
	TagSpecifications=[
        {
            'ResourceType': 'vpc',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'VPC-HT'
                },
            ]
        },
    ],
    CidrBlock=vpc_cidr)
vpc_ID = VPC_response['Vpc']['VpcId']
print ("VPC ID is: ", vpc_ID)

# Subnet-01 Creation
print ("Enter the Subnet-01 CIDR Value: ")
Subnet_cidr = input()
Subnet_response = client.create_subnet(
    TagSpecifications=[
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Subnet-01-HT'
                },
            ]
        },
    ],
    CidrBlock=Subnet_cidr,
    VpcId=vpc_ID)
subnet01_id = Subnet_response['Subnet']['SubnetId']
print ("Subnet-01 ID is: ", subnet01_id)

# Subnet-02 Creation
print ("Enter the Subnet02 CIDR Value: ")
Subnet02_cidr = input()
Subnet_response = client.create_subnet(
    TagSpecifications=[
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Subnet-01-HT'
                },
            ]
        },
    ],
    CidrBlock=Subnet02_cidr,
    VpcId=vpc_ID)
subnet02_id = Subnet_response['Subnet']['SubnetId']
print ("Subnet ID is: ", subnet02_id)


# Internet gateway
IGW_response = client.create_internet_gateway()
igw_id = IGW_response['InternetGateway']['InternetGatewayId']
print ("IGW ID is: ", igw_id)

# Attach IGW into VPC
AIGW_response = client.attach_internet_gateway(
    InternetGatewayId=igw_id,
    VpcId=vpc_ID
)
print ("IGW Attached successfully")

# Route table 
route_response = client.create_route_table(
    VpcId=vpc_ID,
    TagSpecifications=[
        {
            'ResourceType': 'route-table',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Route_01'
                },
            ]
        },
    ]
)
route_id = route_response['RouteTable']['RouteTableId']
print ("route_table ID is: ", route_id)


# Route Table association

routeass_response = client.associate_route_table(RouteTableId = route_id)
print ("Route Table association created")

# Route table Routing entry

# Ec2 Instance