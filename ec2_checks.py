# Prints out status of all EC2 instances in a region
# Every {check_interval} seconds

import boto3
import schedule

work_region    = "us-west-1"
check_interval = 5 # in seconds

ec2_client     = boto3.client  ("ec2", region_name = work_region)
ec2_resource   = boto3.resource("ec2", region_name = work_region)

# Request status and form output
def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances = True
    )
    for status in statuses["InstanceStatuses"]:
        ins_status  = status["InstanceStatus"]["Status"]
        sys_status  = status["SystemStatus"]["Status"]
        state       = status["InstanceState"]["Name"]
        print(f"Instance {status["InstanceId"]} is {state} with instance status {ins_status} and system status {sys_status}")
    print("---------------------------------------\n")

# Run every 10 sec
schedule.every(check_interval).seconds.do(check_instance_status)

while True:
    schedule.run_pending()