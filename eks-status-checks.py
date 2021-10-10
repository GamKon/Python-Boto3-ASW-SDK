# Prints information about all EKS clusters

import boto3

work_region   = "us-west-1"

client        = boto3.client("eks", region_name = work_region)
clusters      = client.list_clusters()["clusters"]

# Print info about all EKS clusters
for cluster in clusters:
    response = client.describe_cluster(
        name = cluster
    )
    cluster_info     = response    ["cluster"]
    cluster_status   = cluster_info["status"]
    cluster_endpoint = cluster_info["endpoint"]
    cluster_version  = cluster_info["version"]

    print(f"Cluster {cluster} status is {cluster_status}")
    print(f"Cluster endpoint: {cluster_endpoint}")
    print(f"Cluster version:  {cluster_version}")
    print("---------------------------------------")
