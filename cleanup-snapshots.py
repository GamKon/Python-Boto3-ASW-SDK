# Deletes old snapshots but last two for each EC2 instance

import boto3
from operator import itemgetter

work_region = "ca-central-1"

ec2_client  = boto3.client("ec2", region_name = work_region)

volumes     = ec2_client.describe_volumes(
    Filters = [
        {
            "Name":   "tag:environment",
            "Values": ["prod"]
        }
    ]
)

for volume in volumes["Volumes"]:
    snapshots    = ec2_client.describe_snapshots(
        OwnerIds = ["self"],
        Filters  = [
            {
                "Name":   "volume-id",
                "Values": [volume["VolumeId"]]
            }
        ]
    )

# Sort by date
    sorted_by_date = sorted(snapshots["Snapshots"], key=itemgetter("StartTime"), reverse=True)

# Delete all but first two
    for snap in sorted_by_date[2:]:
        response = ec2_client.delete_snapshot(
            SnapshotId=snap["SnapshotId"]
        )
        print(response)
