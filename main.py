import json
import sys
import os, time
# import logging

from config.payload import auth_token_payload_str, vnet_payload_str, \
     subnet_payload_str, nsg_payload_str, subnet_delegate_payload_str,\
     subnet_nsg_delegate_payload_str,datafactory_payload_str, \
     dbricks_ws_payload_str, dbricks_ws_cvnet_payload_str, \
     databricks_cluster_payload_str, local_gw_payload_str, storage_ac_str

from apis.restapi import auth_token, create_vnet, create_subnet,\
     create_nsg, create_vpn_gateway, create_local_gateway, create_datafactory,\
     create_databricks_workspace, create_databricks_cluster,create_storage_ac 
     
from config.urls import auth_url, auth_token_url, az_mng_url, dbricks_ws_url,\
     vnet_url, subnet_url, nsg_url, dfactory_url, databricks_url, \
     databricks_clu_create_url, local_gw_url, storage_url

vnet = False
subnet = False
subnet_delegate = False
subnet_nsg_delegate = False
nsg = False
datafactory = False
databricks_ws = False
databricks_default = False
# databricks_cvnet = False
# databricks_ws_cvnet = False
databricks_clu = False
vpn_gateway = False
local_gateway = False
storage = False
    
if __name__ == "__main__":
    
    # config_file = '%s\%s\%s' %(os.path.dirname(os.path.abspath(__file__)), "config", "payload.json")
    
    create_service_file = '%s\%s' %(os.path.dirname(os.path.abspath(__file__)), \
                              "create_service.json")
    
    with open(create_service_file) as csf:
        create_services = json.load(csf)
    vnet = create_services.get("vnet", False)
    subnet = create_services.get("subnet",False)
    subnet_delegate = create_services.get("subnet_delegate",False)
    subnet_nsg_delegate = create_services.get("subnet_nsg_delegate",False)
    nsg = create_services.get("nsg",False)
    datafactory = create_services.get("datafactory",False)
    databricks_ws = create_services.get("databricks_ws",False)
    databricks_default = create_services.get("databricks_default",False)
    databricks_clu = create_services.get("databricks_clu",False)
    local_gateway = create_services.get("local_gateway",False)
    storage = create_services.get("storage",False)
    
    if not any([vnet, subnet, subnet_delegate, subnet_nsg_delegate, nsg, datafactory, databricks_ws, databricks_default, databricks_clu, local_gateway, storage]):
        print("Check the create_service.json....")
        print("All the create_services are 0....")
        print("Not creating any service....")
        print("Exiting run....")
        # sys.exit(1)
        
    print("vnet value is :", vnet )
    print("subnet value is :", subnet )
    print("subnet_delegate value is :", subnet_delegate )
    print("subnet_nsg_delegate value is :", subnet_nsg_delegate )
    print("nsg value is :", nsg )
    print("datafactory value is :", datafactory )
    print("databricks_ws value is :", databricks_ws )
    print("databricks_default value is :", databricks_default )
    print("databricks_clu value is :", databricks_clu )
    print("local_gateway value is :", local_gateway )
    
    # sys.exit(0)
    input_file = '%s\%s\%s' %(os.path.dirname(os.path.abspath(__file__)), \
                              "config", "input.json")
    
    # Reading all the input parameters form config/input.json file.
    with open(input_file) as f:
        data = json.load(f)
    
    subscription_id = data["SUBSCRIPTION_ID"]
    rs_group_name = data["RS_GROUP_NAME"]
    location = data["LOCATION"]
    tenant_id = data["TENANT_ID"]
    client_id = data["CLIENT_ID"]
    secret = data["SECRET"]

    # Get the token to create the resource using Rest APIs
    auth_header = {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
            }
    
    auth_payload = auth_token_payload_str.format(client_id=client_id, \
                                                 secret=secret, url=az_mng_url)
    print("Payload for token API is: ", auth_payload)
    print("                ")
    auth_token_url = auth_token_url %(tenant_id)
    token = auth_token(auth_url, auth_payload, auth_header, auth_token_url)
    if 'Error' in token:
        raise Exception("Token creation got failed.", token)
    # print("Token is: ",  token)
    
    # Header for all the Azure resource rest apis     
    az_ser_header = {
    'content-type': "application/json",
    'authorization': "Bearer %s" % token,
    'cache-control': "no-cache"
    }
    # print("Header for Azure services is ", az_ser_header )
    # print("                ")
    # print("Token is main %s" %token)
    
    # Create the Vnet
    if vnet:
        print("Creating Vnet ....")
        print("                ")
        print("Vnet: subscription_id is ", subscription_id)
        print("                ")
        print("Vnet: rs_group_name is ", rs_group_name)
        print("                ")
        print("Vnet: name is ", data["VNET_NAME"])
        print("                ")
        print("Vnet: Address prefix is ", data["VNET_ADD_PREFIX"])
        print("                ")
        print("Vnet: Subnet name and address prefix is ", data["VNET_SUBNET_ADD_PREFIX"])

        vnet_url = vnet_url %(
                subscription_id, rs_group_name, data["VNET_NAME"])
        print("Vnet: url is ", vnet_url)
        print("                ")
        
        vnet_payload = vnet_payload_str %(data["VNET_ADD_PREFIX"], 
                data["VNET_SUBNET_ADD_PREFIX"], data["LOCATION"])
        print("Vnet: payload is ", vnet_payload)
        print("                ")
        print("Vnet: Calling API....")
        vnet_response = create_vnet(az_mng_url, vnet_payload, az_ser_header, vnet_url)
        print("Vnet: response is  ", vnet_response) 
        print("                ")
        if 'error' in str(vnet_response).lower():
            raise Exception("Exception: Vnet creation failed with error ", vnet_response)
        elif vnet_response == 202:
            time.sleep(100)
            vnet_response = create_vnet(az_mng_url, vnet_payload, az_ser_header, vnet_url)
            if 'error' in str(vnet_response).lower():
                raise Exception("Exception: Vnet creation failed with error ", vnet_response)
            elif vnet_response == 201 or vnet_response == 200:
                print("Vnet Created successfully...")
                print("                ")
                time.sleep(60)
        elif vnet_response == 201 or vnet_response == 200:
                print("Vnet Created successfully...")
                print("                ")
                time.sleep(60)
                
    # create NSG
    if nsg:
        print("Creating NSG ....")
        print("                ")
        nsg_payload = nsg_payload_str %(location)
        print("NSG: paylod is %s" %nsg_payload)
        print("                ")
        nsg_url = nsg_url %(subscription_id, rs_group_name, data["NSG_NAME"])
        print("NSG: url is %s" %nsg_url)
        print("                ")
        print("NSG: header is %s" %az_ser_header)
        print("                ")
        nsg_response = create_nsg(az_mng_url, nsg_payload, az_ser_header, nsg_url)
        print("NSG: response is  ", nsg_response) 
        print("                ")
        if 'Error' in str(nsg_response):
            raise Exception("Exception: NSG creation failed with error ", nsg_response)
        elif nsg_response == 202:
            time.sleep(100)
            nsg_response = create_nsg(az_mng_url, nsg_payload, az_ser_header, nsg_url)
            if 'Error' in str(nsg_response):
                raise Exception("Exception: NSG creation failed with error ", nsg_response)
            elif nsg_response == 201 or nsg_response == 200:
                print("NSG Created successfully...")
                print("                ")
                time.sleep(60)
        elif nsg_response == 200 or nsg_response == 201:
            print("NSG Created successfully...")
            print("                ")
            time.sleep(60)
    
    # Create the subnets # Need to check how to create multiple subnets
    if subnet:
        print("Creating Subnet ....")
        print("                ")
        if subnet_delegate:
            subnet_payload = subnet_delegate_payload_str %(
                data["SUBNET_ADD_PREFIX"], data["DELEGATION_NAME"],\
                subscription_id, rs_group_name, data["VNET_NAME"], \
                data["SUBNET_NAME"], data["DELEGATION_NAME"], 
                data["DELEGATE_SER_NAME"])
            
        elif subnet_nsg_delegate:
            print("Creating NSG ....")
            print("                ")
            nsg_payload = nsg_payload_str %(location)
            print("SUBNET_NSG: paylod is %s" %nsg_payload)
            print("                ")
            nsg_url = nsg_url %(subscription_id, rs_group_name, data["NSG_NAME"])
            print("SUBNET_NSG: url is %s" %nsg_url)
            print("                ")
            print("NSG: header is %s" %az_ser_header)
            print("                ")
            nsg_response = create_nsg(az_mng_url, nsg_payload, az_ser_header, nsg_url)
            print("NSG: response is  ", nsg_response) 
            print("                ")
            if 'Error' in str(nsg_response):
                raise Exception("Exception: NSG creation failed with error ", nsg_response)
            elif nsg_response == 202:
                time.sleep(100)
                nsg_response = create_nsg(az_mng_url, nsg_payload, az_ser_header, nsg_url)
                if 'Error' in str(nsg_response):
                    raise Exception("Exception: NSG creation failed with error ", nsg_response)
                elif nsg_response == 201 or nsg_response == 200:
                    print("NSG Created successfully...")
                    print("                ")
                    time.sleep(60)
            elif nsg_response == 200 or nsg_response == 201:
                print("NSG Created successfully...")
                print("                ")
            # time.sleep(60)
            time.sleep(100)
            subnet_payload = subnet_nsg_delegate_payload_str %(
                data["SUBNET_ADD_PREFIX"], data["DELEGATION_NAME"],\
                subscription_id, rs_group_name, data["VNET_NAME"], \
                data["SUBNET_NAME"], data["DELEGATION_NAME"], \
                data["DELEGATE_SER_NAME"], subscription_id, rs_group_name,\
                data["NSG_NAME"], data["NSG_NAME"])
            # print("subnet_payload is ", subnet_payload)
        else:
            subnet_payload = subnet_payload_str %(data["SUBNET_ADD_PREFIX"])
        
        print("SUBNET: paylod is %s" %subnet_payload)
        print("                ")        
        subnet_url = subnet_url %(subscription_id, rs_group_name, data["VNET_NAME"], data["SUBNET_NAME"])
        print("SUBNET: url is %s" %subnet_url)
        print("                ")
        print("SUBNET: header is %s" %az_ser_header)
        print("                ")
        subnets_response = create_subnet(az_mng_url, subnet_payload, az_ser_header, subnet_url)
        if 'Error' in str(subnets_response):
            raise Exception("Exception: Subnet creation failed with error ", subnets_response)
        elif subnets_response == 202:
            time.sleep(100)
            subnets_response = create_subnet(az_mng_url, subnet_payload, az_ser_header, subnet_url)
            if 'Error' in str(subnets_response):
                raise Exception("Exception: Subnet creation failed with error ", subnets_response)
            elif subnets_response == 201 or subnets_response == 200:
                print("Subnet Created successfully...")
                print("                ")
                time.sleep(60)
        elif subnets_response == 200 or subnets_response == 201:
            print("Subnet Created successfully...")
            print("                ")
            time.sleep(60)
        
    
    # Create the Datafactory
    if datafactory:
        print("Creating DataFactory ....")
        print("                ")
        datafactory_payload = datafactory_payload_str %(location)
        print("DataFactory: paylod is %s" %datafactory_payload)
        print("                ")
        # print(datafactory_payload )
        datafactory_url = dfactory_url %(subscription_id, rs_group_name, data["DATAFACTORY_NAME"])
        print("DataFactory: url is %s" %datafactory_url)
        print("                ")
        datafactory_response = create_datafactory(az_mng_url, datafactory_payload, az_ser_header, datafactory_url)
        
        if 'Error' in str(datafactory_response):
            raise Exception("Exception: %s" %datafactory_response)
        elif datafactory_response == 202:
            time.sleep(100)
            datafactory_response = create_datafactory(az_mng_url, datafactory_payload, az_ser_header, datafactory_url)
            if 'Error' in str(datafactory_response):
                raise Exception("Exception: %s" %datafactory_response)
            elif datafactory_response == 200 or datafactory_response == 201:
                print("DataFactory account %s has been created successfully." % data["DATAFACTORY_NAME"])
                print("                ")
                time.sleep(60)
        elif datafactory_response == 200 or datafactory_response == 201:
            print("DataFactory account %s has been created successfully." % data["DATAFACTORY_NAME"])
            print("                ")
            time.sleep(60)
                
    # create Storage account    
    if storage:
        print("Creating Storage Account V2....")
        print("                ")
        storage_payload = storage_ac_str %(location)
        print("Storage Account: paylod is %s" %storage_payload)
        print("                ")
        storage_url = storage_url %(subscription_id, rs_group_name, data["STORAGE_NAME"])
        print("Storage Account: url is %s" %storage_url)
        print("                ")
        storage_response = create_storage_ac(az_mng_url, storage_payload, az_ser_header, storage_url)
        print("storage_response is: ", storage_response)
        if 'Error' in str(storage_response):
            raise Exception("Exception: %s" %storage_response)
        elif storage_response == 202:
            time.sleep(100)
            storage_response = create_storage_ac(az_mng_url, storage_payload, az_ser_header, storage_url)
            print("storage_response is: ", storage_response)
            if 'error' in str(storage_response):
                raise Exception("Exception: %s" %storage_response)
            elif storage_response == 200 or storage_response == 201:
                print("Storage account %s has been created successfully." % data["STORAGE_NAME"])
                time.sleep(60)
        elif storage_response == 200 or storage_response == 201:
                print("Storage account %s has been created successfully." % data["STORAGE_NAME"])
                time.sleep(60)
                
    # create Databricks workspace
    if databricks_ws:
        print("Creating Databricks Workspace ....")
        print("                ")
        if databricks_default:
            dbricks_ws_payload = dbricks_ws_payload_str %(
                subscription_id, data["DATABRICKS_MGMT_RG"],location, \
                data["DATABRICKS_SKU"]
                )
        else:
            dbricks_ws_payload = dbricks_ws_cvnet_payload_str %(
            subscription_id, data["DATABRICKS_MGMT_RG"],data["DATABRICKS_PVT_SUB"],\
            data["DATABRICKS_PUB_SUB"], subscription_id, rs_group_name, data["VNET_NAME"],\
            data["DATABRICKS_ENABLENOPUBLICIP"], data["DATABRICKS_VNET_PRE"], location, \
            data["DATABRICKS_SKU"]
            )
        print("Databricks Workspace: payload is ", dbricks_ws_payload)
        print("                ")     
        dbricks_ws_url = dbricks_ws_url.format(subid=subscription_id, rg=rs_group_name, ws=data["DATABRICKS_WS_NAME"])
        print("Databricks Workspace: url is ", dbricks_ws_url)
        print("                ")     
        databricks_ws_res = create_databricks_workspace(az_mng_url, dbricks_ws_payload, az_ser_header, dbricks_ws_url)
        if 'Error' in str(databricks_ws_res):
            raise Exception("Exception: %s" %databricks_ws_res)
        elif databricks_ws_res == 202:
            time.sleep(100)
            databricks_ws_res = create_databricks_workspace(az_mng_url, dbricks_ws_payload, az_ser_header, dbricks_ws_url)
            if 'Error' in str(databricks_ws_res):
                raise Exception("Exception: %s" %databricks_ws_res)
            elif databricks_ws_res == 200 or databricks_ws_res == 201:
                print("Databricks workspace %s has been created successfully." % data["DATABRICKS_WS_NAME"])
                print("                ")
                time.sleep(60)
        elif datafactory_response == 200 or datafactory_response == 201:
            print("Databricks workspace %s has been created successfully." % data["DATABRICKS_WS_NAME"])
            print("                ")
            time.sleep(100)

    # create databricks cluster
    if databricks_clu:
        print("Creating Databricks Cluster ....")
        print("                ")
        dbricks_clu_payload = databricks_cluster_payload_str %(
            data["DATABRICKS_CLU_NAME"], data["DATABRICKS_SPARK_VERSION"],\
            data["DATABRICKS_NODE_TYPE"], data["DATABRICKS_NUM_NODES"], \
            data["DATABRICKS_AUTO_TER_MINS"], data["SPARK_ENV_VARS"])
        print("Databricks Cluster: payload is ", dbricks_clu_payload)
        print("                ")
        print("Databricks Cluster: url is ", databricks_clu_create_url)
        print("                ")
        dbricks_clu_header = {
            'content-type': "application/json",
            'authorization': "Bearer %s" %(data["DATABRICKS_TOKEN"]),
            'cache-control': "no-cache"
            } 
        print("Databricks Cluster: Header is ", dbricks_clu_header)
        print("                ")
        print("Databricks Cluster: Connection url is ", databricks_url %(location))
        print("                ")
        dbricks_clu_res = create_databricks_cluster(databricks_url %(location),
                   dbricks_clu_payload, dbricks_clu_header, databricks_clu_create_url)
        if 'Error' in str(dbricks_clu_res):
            raise Exception("Exception: %s" %dbricks_clu_res)
        elif databricks_ws_res == 202:
            time.sleep(100)
            dbricks_clu_res = create_databricks_cluster(databricks_url %(location),
                   dbricks_clu_payload, dbricks_clu_header, databricks_clu_create_url)
            if 'Error' in str(dbricks_clu_res):
                raise Exception("Exception: %s" %dbricks_clu_res)
            elif dbricks_clu_res == 200 or dbricks_clu_res == 201:
                print("Databricks Cluster %s has been created successfully." % data["DATABRICKS_CLU_NAME"])
                print("                ")
                time.sleep(60)
        elif dbricks_clu_res == 200 or dbricks_clu_res == 201:
            print("Databricks Cluster %s has been created successfully." % data["DATABRICKS_CLU_NAME"])
            print("                ")
            time.sleep(100)
    
    # create local network gateway
    if local_gateway:
        print("Creating Local gateway Cluster ....")
        print("                ")
        local_gw_payload = local_gw_payload_str %(data["LOCAL_GW_ADD_PRE"], \
                                                        data["LOCAL_GW_IP"], location)
        print("Local Gateway: payload is: ", local_gw_payload)
        print("                ")
        local_gw_url = local_gw_url %(subscription_id, rs_group_name, data["LOCAL_GW_NAME"])
        print("Local Gateway: url is: ", local_gw_url)
        print("                ")
        local_gw_res = create_local_gateway(az_mng_url,local_gw_payload, az_ser_header, local_gw_url)
        if 'Error' in str(local_gw_res):
            raise Exception("Exception: %s" %local_gw_res)
        elif local_gw_res == 202:
            time.sleep(100)
            local_gw_res = create_local_gateway(az_mng_url,local_gw_payload, az_ser_header, local_gw_url)
            if 'Error' in str(local_gw_res):
                raise Exception("Exception: %s" %local_gw_res)
            elif local_gw_res == 200 or local_gw_res == 201:
                print("Local Gateway: %s has been created successfully." % data["LOCAL_GW_NAME"])
                print("                ")
                time.sleep(60)
        elif local_gw_res == 200 or local_gw_res == 201:
            print("Local Gateway: %s has been created successfully." % data["LOCAL_GW_NAME"])
            print("                ")
            time.sleep(100)
    

    


   