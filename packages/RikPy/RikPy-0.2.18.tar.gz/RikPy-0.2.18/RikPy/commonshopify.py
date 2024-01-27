import requests

def Shopify_get_metaobject_gid(shop, access_token, metaobject_type, handle):

    print(f"Access token: {access_token}")

    url = f"https://{shop}.myshopify.com/admin/api/2024-01/graphql.json"
    headers = {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': access_token
    }

    print(f"headers: {headers}")

    query = """
    query GetMetaobjectByHandle($type: String!, $handle: String!) {
      metaobjectByHandle(handle: {
            type: $type,
            handle: $handle
        }) {
            id
            type
            handle
        }
    }
    """
    
    variables = {
        "type": metaobject_type,
        "handle": handle
    }
    
    payload = {
        'query': query,
        'variables': variables
    }

    print(f"payload: {payload}")
    
    response = requests.post(url, json=payload, headers=headers)
    # response = requests.post(url, json={'query': query}, headers=headers)
    
    if response.status_code == 200:
        response_json = response.json()
        result_id = response_json['data']['metaobjectByHandle']['id']
        return result_id
    else:
        print(f"Error: {response.status_code}")
        return None

def Shopify_update_metaobject(shop, access_token, metaobject_gid, banner_url, mobile_banner_url, product_url, metaobject_banner_number):
    # Push to shopify banner object for vinzo
    # shop = '9d9853'  
    # access_token = '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'  
    metaobject_type = "product_banner"
    metaobject_handle = "aiir-banner"
    # metaobject_gid="gid://shopify/Metaobject/32967917879"

    url = f"https://{shop}.myshopify.com/admin/api/2024-01/graphql.json"
    headers = {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': access_token
    }

    # Generate field names based on metaobject_banner_number
    field_names = [f"product_link_{metaobject_banner_number}",
                   f"banner_url_{metaobject_banner_number}",
                   f"mobile_banner_url_{metaobject_banner_number}"]

    mutation = """
    mutation UpdateMetaobject($id: ID!, $metaobject: MetaobjectUpdateInput!) {
    metaobjectUpdate(id: $id, metaobject: $metaobject) {
        metaobject {
        handle
        """
    
    # Add dynamic field names to the mutation
    for field_name in field_names:
        mutation += f"{field_name}: field(key: \"{field_name}\") {{ value }}\n"

    mutation += """
        }
        userErrors {
        field
        message
        code
        }
    }
    }
    """

    variables = { 
        "id": metaobject_gid,
        "metaobject": {
            "fields": [
                {"key": field_name, "value": value}
                for field_name, value in zip(field_names, [product_url, banner_url, mobile_banner_url])
            ]
        } 
    }

    response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error loading to shopify: {response.status_code}")
        return (f"Error loading to shopify: {response.status_code}")

def Shopify_get_products(shop, access_token):

    '''Uses Admin API'''

    url = f"https://{shop}.myshopify.com/admin/api/2024-01/products.json"
    headers = {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': access_token
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve products: {response.status_code}")
        return None