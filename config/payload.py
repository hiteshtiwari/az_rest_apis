auth_token_payload_str = "grant_type=client_credentials&client_id={client_id}&client_secret={secret}&resource=https%3A%2F%2F{url}"

vnet_payload_str = """{
     "properties": 
           {"addressSpace": 
		         {"addressPrefixes": ["%s"]},
		    "subnets": 
		          %s,
	  },"location": "%s"
	  }"""
# vnet_payload_str = "  "            
subnet_payload_str = """{
    "properties": {"addressPrefix": "%s"}
	}"""

nsg_payload_str = """{
    "location": "%s"
    }"""

subnet_delegate_payload_str = """{
    "properties": {
    "addressPrefix": "%s", 
    "delegations": [{"name": "%s",
	                 "id": "/subscriptions/%s/resourceGroups/%s/providers/Microsoft.Network/virtualNetworks/%s/subnets/%s/delegations/%s",
					 "properties": 
					     {"serviceName": "%s","actions": []}
						  }    
						]  
	    }
	}
"""

subnet_nsg_delegate_payload_str = """{ 
    "properties": { 
    "addressPrefix": "%s",
    "delegations": [{ "name": "%s", 
    "id": "/subscriptions/%s/resourceGroups/%s/providers/Microsoft.Network/virtualNetworks/%s/subnets/%s/delegations/%s",  
    "properties": {"serviceName": "%s","actions": []  }}],
    "NetworkSecurityGroup" : 
        {"id": "/subscriptions/%s/resourceGroups/%s/providers/Microsoft.Network/networkSecurityGroups/%s",
        "name": "%s"}  } }
  """

datafactory_payload_str = """{
    "location": "%s"
	}"""


dbricks_ws_payload_str = """{
    "properties": 
		{"managedResourceGroupId": "/subscriptions/%s/resourceGroups/%s"    
		}, 
		"location": "%s",  
		"sku": {"name": "%s"}
		}"""
        
dbricks_ws_cvnet_payload_str = """{
    "properties": 
		{"managedResourceGroupId": "/subscriptions/%s/resourceGroups/%s",    
		"parameters": { "customPrivateSubnetName": {"value": "%s"  },  
		    "customPublicSubnetName": {"value": "%s" },  
		    "customVirtualNetworkId": {"value": "/subscriptions/%s/resourceGroups/%s/providers/Microsoft.Network/virtualNetworks/%s"},  
		    "enableNoPublicIp": {"value": %s  },  
		    "vnetAddressPrefix": {"value": "%s"}  }  
		}, 
		"location": "%s",  
		"sku": {"name": "%s"}
		}"""
        
# databricks_cluster_payload = "{\r\n  \"cluster_name\": \"my-cluster\",\r\n  \"spark_version\": \"6.3.x-scala2.11\",\r\n  \"node_type_id\": \"Standard_DS3_v2\",\r\n  \"num_workers\": 2,\r\n  \"autotermination_minutes\":10,\r\n  \"spark_env_vars\": {\r\ngc  \"PYSPARK_PYTHON\": \"/databricks/python3/bin/python3\"\r\n    }\r\n}"
databricks_cluster_payload_str = """{
	"cluster_name": "%s",
	"spark_version": "%s",
	"node_type_id": "%s",
	"num_workers": %d,
	"autotermination_minutes":%d,
	"spark_env_vars": %s
	}
	"""

local_gw_payload_str = """{
    "properties": {"localNetworkAddressSpace": 
        {"addressPrefixes": ["%s"]},"gatewayIpAddress": "%s"  },  
        "location": "%s"
        }"""
        
storage_ac_str = """{
    "sku": {
         "name": "Standard_GRS",
         "tier": "Standard"
       },
    "kind": "StorageV2",
    "location": "%s",
    "properties":{
  	   "accessTier": "hot"
       }
   }"""
