import http
import json

def auth_token(req_url, payload, header, auth_token_url):
    '''
       To get the Bearer token to call rest apis.
    '''
    try:
        conn = http.client.HTTPSConnection("%s" %req_url)
        conn.request("POST", auth_token_url, payload, header)
        res = conn.getresponse()
        if res.status == 200 or res.status == 201:
            token = json.loads(res.read().decode("utf-8"))
            # print("under if cond") 
            return token['access_token']
        else:
            token = json.loads(res.read().decode("utf-8"))
            return "Error: ",  token
    except Exception as err:
        return "Error: (%s)" % str(err)

def create_vnet(req_url, payload, header, vnet_url):
    '''
    To create the Vnet in given subcription and resource group
    '''
    try:
        conn = http.client.HTTPSConnection("%s" %req_url)
        conn.request("PUT", vnet_url, payload, header)
        res = conn.getresponse()
        if res.status == 200 or res.status == 201 or res.status == 202:
                #            data = json.loads(res.read().decode("utf-8"))
                #            print("under if cond")
                #            print(data)
            return res.status
        else:
            data = json.loads(res.read().decode("utf-8"))
            return "Error: %s" % str(data)
    except Exception as err:
        return "Error: (%s)" % str(err)  

def create_subnet(req_url, payload, headers, subnet_url):
    '''
    To create the subnets in given subcription and resource group
    '''
    try:
        conn = http.client.HTTPSConnection("%s" %req_url)
        conn.request("PUT", subnet_url, payload, headers)   
        res = conn.getresponse()
        
        if res.status == 200 or res.status == 201 or res.status == 202:
            # data = json.loads(res.read().decode("utf-8"))
            # print(data)
            return res.status
        else:
            data = json.loads(res.read().decode("utf-8"))
            return "Error: %s "  %str(data)
    except Exception as err:
        return "Error: (%s)" % str(err)  
    
def create_nsg(req_url, payload, headers, nsg_url):
    '''
    To create nsg under the given Vnet
    '''
    try:
        conn = http.client.HTTPSConnection("%s" %req_url)
        conn.request("PUT", nsg_url, payload, headers)   
        res = conn.getresponse()
        if res.status == 200 or res.status == 201 or res.status == 202:
            return res.status
        else:
            data = json.loads(res.read().decode("utf-8"))
            return "Error: (%s)" % str(data)
    except Exception as err:
        return "Error: (%s)" % str(err) 

def create_vpn_gateway():
    '''
    To create the vpn gateway in given subnet
    '''
    pass


def create_local_gateway(req_url, payload, headers, local_gw_url):
    '''
    To create local gateway in given subnet
    '''
    try:
        conn = http.client.HTTPSConnection("%s" %req_url)
        conn.request("PUT", local_gw_url, payload, headers)   
        res = conn.getresponse()
        if res.status == 200 or res.status == 201 or res.status == 202:
            return res.status
        else:
            data = json.loads(res.read().decode("utf-8"))
            # print(data)
            return "Error: (%s)" % str(data)
    except Exception as err:
        return "Error: (%s)" % str(err) 


def create_datafactory(req_url, payload, headers, dfactory_url):
    '''
    To create data factory under the given subscription and resource group
    '''
    try:
        conn = http.client.HTTPSConnection("%s" %req_url)    
        conn.request("PUT", dfactory_url, payload, headers)
        res = conn.getresponse()
        if res.status == 200 or res.status == 201 or res.status == 202:
            return res.status
        else:
            data = json.loads(res.read().decode("utf-8"))
            return "Error: (%s)" %str(data)
    except Exception as err:
        return "Error: (%s)" % str(err)         


def create_databricks_workspace(req_url, payload, headers, dbricks_ws_url):
    '''
    To create databricks workspace in given subscription and resource group
    '''

    try:
        conn = http.client.HTTPSConnection("%s" % req_url)  
        conn.request("PUT", dbricks_ws_url, payload, headers)
        res = conn.getresponse()
        if res.status == 200 or res.status == 201 or res.status == 202:
            return res.status
        else:
            data = json.loads(res.read().decode("utf-8"))        
            return "Error: (%s)" % str(data)
    except Exception as err:
        return "Error: (%s)" % str(err) 


def create_databricks_cluster(req_url, payload, header, dbricks_clu_url):
    '''
    To create the databricks cluster under the given workspace
    '''
    try:
        conn = http.client.HTTPSConnection("%s" %req_url)
        conn.request("POST", "%s" %dbricks_clu_url, payload, header)
        res = conn.getresponse()
        if res.status == 200 or res.status == 201 or res.status == 202:
            return res.status
        else:
            # print("under db else condition")
            data = json.loads(res.read().decode("utf-8"))
            return "Error: (%s)" % str(data)
    except Exception as err:
        return "Exception: (%s)" % str(err)


def create_storage_ac(req_url, payload, headers, storage_url):
    '''
    To delegate the Vnet with other Vnet.
    '''
    try:
        conn = http.client.HTTPSConnection("%s" %req_url)    
        conn.request("PUT", storage_url, payload, headers)
        res = conn.getresponse()
        if res.status == 200 or res.status == 201 or res.status == 202:
            # data = json.loads(res.read().decode("utf-8"))
            # print(data)
            return res.status
        else:
            data = json.loads(res.read().decode("utf-8"))
            return "Error: (%s)" % str(data)
    except Exception as err:
        return "Error: (%s)" % str(err) 


def create_vms():
    '''
    To create the VM
    '''
    pass


def stop_vms():
    '''
    To stop the one VM and VMs
    '''
    pass


def delegate_vnet(req_url, payload, headers, subnet_url):
    '''
    To delegate the Vnet with other Vnet.
    '''
    pass