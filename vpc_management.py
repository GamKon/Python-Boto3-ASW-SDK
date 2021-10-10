# working with VPC, subnets
# Read info, create resources

import boto3
work_region   = "us-west-1"

# create new VPC
ec2_resource  = boto3.resource("ec2", region_name = work_region)
new_vpc       = ec2_resource.create_vpc(
    CidrBlock = "10.0.0.0/16"
)

# Add tags to the VPC
new_vpc.create_tags(
    Tags = [
        {
            "Key":   "Name",
            "Value": "VPC from Python"
        },
        {
            "Key":   "Owner",
            "Value": "GamKon"
        },
    ]
)

# Create subnets in the new VPC
new_vpc.create_subnet(
    CidrBlock = "10.0.1.0/24"
)
new_vpc.create_subnet(
    CidrBlock = "10.0.2.0/24"
)

# Print all VPCs and cidrs in a given region
ec2_client         = boto3.client("ec2", region_name = work_region)
all_available_vpcs = ec2_client.describe_vpcs()
vpcs               = all_available_vpcs["Vpcs"]

for vpc in vpcs:
    print(vpc["VpcId"])
    cidr_block_sets = vpc["CidrBlockAssociationSet"]
    for cidr_block in cidr_block_sets:
        print(cidr_block["CidrBlock"])
    print("---------------------------------------")
