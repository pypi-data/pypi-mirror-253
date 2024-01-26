import requests

def Shopify_update_metaobject(shop, access_token, metaobject_gid, banner_url, mobile_banner_url, product_url):
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
    mutation = """
    mutation UpdateMetaobject($id: ID!, $metaobject: MetaobjectUpdateInput!) {
    metaobjectUpdate(id: $id, metaobject: $metaobject) {
        metaobject {
        handle
        product_link_1: field(key: "product_link_1") { value }
        banner_url_1: field(key: "banner_url_1") { value }
        mobile_banner_url_1: field(key: "banner_url_1") { value }
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
                    {"key": "banner_url_1", "value": banner_url},
                    {"key": "mobile_banner_url_1", "value": mobile_banner_url},
                    {"key": "product_link_1", "value": product_url}
                    ]
            } 
    }
    response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error loading to shopify: {response.status_code}")
        return (f"Error loading to shopify: {response.status_code}")

