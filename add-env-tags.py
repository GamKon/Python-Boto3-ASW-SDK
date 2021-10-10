# Add environment tags to EC2 servers depends on region they are in

import boto3

work_region_1         = "us-west-1"
work_region_2         = "ca-central-1"

ec2_client_region_1   = boto3.client  ("ec2", region_name = work_region_1)
ec2_resource_region_1 = boto3.resource("ec2", region_name = work_region_1)

ec2_client_region_2   = boto3.client  ("ec2", region_name = work_region_2)
ec2_resource_region_2 = boto3.resource("ec2", region_name = work_region_2)

instance_ids_region_1 = []
instance_ids_region_2 = []

reservations_region_1 = ec2_client_region_1.describe_instances()["Reservations"]
for res in reservations_region_1:
    instances = res["Instances"]
    for ins in instances:
        instance_ids_region_1.append(ins["InstanceId"])


response = ec2_resource_region_1.create_tags(
    Resources = instance_ids_region_1,
    Tags = [
        {
            "Key":   "environment",
            "Value": "prod"
        },
    ]
)

reservations_region_2 = ec2_client_region_2.describe_instances()["Reservations"]
for res in reservations_region_2:
    instances = res["Instances"]
    for ins in instances:
        instance_ids_region_2.append(ins["InstanceId"])


response = ec2_resource_region_2.create_tags(
    Resources = instance_ids_region_2,
    Tags = [
        {
            "Key"  : "environment",
            "Value": "dev"
        },
    ]
)
