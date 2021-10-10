# Backups EC2 volumes with tag environment:prod every day

import boto3
import schedule

work_region = "ca-central-1"

ec2_client  = boto3.client("ec2", region_name = work_region)


def create_volume_snapshots():
    volumes = ec2_client.describe_volumes(
#        Filters=[
#            {
#                "Name"  : "tag:environment",
#                "Values": ["prod"]
#            }
#        ]
    )
    for volume in volumes["Volumes"]:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId = volume["VolumeId"]
        )
        print(new_snapshot)


schedule.every().day.do(create_volume_snapshots)

while True:
    schedule.run_pending()
