# azure_sdk_list_resource_groups.py
# This script uses the Azure SDK for Python to list all resource groups.
# It automates resource management tasks and integrates with Azure DevOps pipelines for monitoring.

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Acquire a credential object using DefaultAzureCredential
credential = DefaultAzureCredential()
subscription_id = "YOUR_SUBSCRIPTION_ID"

# Create a ResourceManagementClient
resource_client = ResourceManagementClient(credential, subscription_id)

# List resource groups
print("Listing resource groups:")
for rg in resource_client.resource_groups.list():
    print(rg.name)
