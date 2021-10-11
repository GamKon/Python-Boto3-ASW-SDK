# Add environment tags to EC2 servers depends on region they are in
# prod in region_prod, dev in region_dev
import boto3

work_region_prod         = "ca-central-1"
work_region_dev          = "us-west-1"

ec2_client_region_prod   = boto3.client  ("ec2", region_name = work_region_prod)
ec2_resource_region_prod = boto3.resource("ec2", region_name = work_region_prod)

ec2_client_region_dev   = boto3.client  ("ec2", region_name = work_region_dev)
ec2_resource_region_dev = boto3.resource("ec2", region_name = work_region_dev)

instance_ids_region_prod = []
instance_ids_region_dev = []

reservations_region_prod = ec2_client_region_prod.describe_instances()["Reservations"]
for res in reservations_region_prod:
    instances = res["Instances"]
    for ins in instances:
        instance_ids_region_prod.append(ins["InstanceId"])


response = ec2_resource_region_prod.create_tags(
    Resources = instance_ids_region_prod,
    Tags = [
        {
            "Key":   "environment",
            "Value": "prod"
        },
    ]
)

reservations_region_dev = ec2_client_region_dev.describe_instances()["Reservations"]
for res in reservations_region_dev:
    instances = res["Instances"]
    for ins in instances:
        instance_ids_region_dev.append(ins["InstanceId"])


response = ec2_resource_region_dev.create_tags(
    Resources = instance_ids_region_dev,
    Tags = [
        {
            "Key"  : "environment",
            "Value": "dev"
        },
    ]
)
