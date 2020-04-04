# Introduction:
  This project is to create services in Azure cloud using REST APIs.

# Install required packages
  clone the repository using below command:

  git clone <projectrepo>
  
  cd <cloned repo>
  
  pip install -r requirements.txt

# Run the script with required parameters
  python main.py 

# Required input details in input.json
  ## Below are the required inputs values to create the services.
  
  SUBSCRIPTION_ID : Subscription id of Azure account under which resources will be created.

  RS_GROUP_NAME:  Resource group name under which resources will be created.

  TENANT_ID: Tenant_id of the azure account.

  CLIENT_ID: Client ID of the azure account.

  SECRET:  App reisgration secret key.

  LOCATION: location under which all the resources/services will be created. Default value is "west europe".

# Service name and required parameters:
## Input parameters to Create Vnet

VNET_ADD_PREFIX          : Address prefix for Vnet

VNET_SUBNET_ADD_PREFIX   : Address prefix for subnet including names of subnets.

VNET_NAME                : Vnet name

## Input parameters to Create Subnet. it has three options:

1. Subnet with prefix

2. Subnet with vnet Delegation : 

3. Subnet With Vnet Delegation and NSG  : It will create/update the Network Security group(NSG) then will create/update the subnet and update with NSG & delegate to given VNET.

Required parameters for all 3 options :

   SUBNET_ADD_PREFIX : Address prefix for subnet.
   
   SUBNET_NAME       : Subnet name
   
   VNET_NAME         : Vnet name under which subnet should be created.
   
additional parameters for option 2:

   DELEGATION_NAME   : Delegate name
   
   DELEGATE_SER_NAME : Vnet or service name to delegate.
   
Addition parameters for option 3 with option 2: 

   NSG_NAME          : NSG name
   
## Input parameters to create NSG(Network Security Group):
NSG_NAME    :    NSG name

## Input parameters to create DataFactory:
DATAFACTORY_NAME : Data factory name.

## Input parameters to create Storage Account:
STORAGE_NAME : stoarge name(it only accepts characters and numbers) should be unique.

## Input parameters to create Databricks workspace. it has two Options:

1. Create DataBricks Workspace without VNET option: Databricks will automatically create the vnets(public and private).

2. Create Databricks Workspace in own vnet: Need to provide the private and public subnets with CIDR(26 or less than that). Also Vnets must be delegated to the Microsoft.Databricks/workspaces service.

For both option below parameters are required:

   DATABRICKS_MGMT_RG : Unique name of resource.
   
   DATABRICKS_SKU : Type of SKU(standard/premium).
   
   DATABRICKS_WS_NAME: name of Workspace.

For Option 2 below are the additional parameters.

   DATABRICKS_PVT_SUB : private subnet name
   
   DATABRICKS_PUB_SUB: Public subnet name
   
   DATABRICKS_ENABLENOPUBLICIP :  Public ip address
   
   DATABRICKS_VNET_PRE: first 2 octets of the Vnet.
   

# Input parameters to create DataBricks Cluster

   DATABRICKS_CLU_NAME          :   Cluster name 
   
   DATABRICKS_SPARK_VERSION     :   Multiple spark versions are avilable. Default is "6.3.x-scala2.11"
   
   DATABRICKS_NODE_TYPE         :   Worker and driver node types. Default is "Standard_DS3_v2"
   
   DATABRICKS_NUM_NODES         :   Number of worker nodes default value 2
   
   DATABRICKS_AUTO_TER_MINS     :   Auto termination time of cluster in mins, default value 30 mins
   
   SPARK_ENV_VARS               :   Spark env variables  

# Note:
To create or Update service use create_service.json file. Update the values to integer number for single and multiple services.
Defalut value for all the services is 0 which is not to create or update service.
