import requests

data={
    'title':'Luxury watch',
    'price':129.99,
    'content':'TMBV'
}

# get_function_response = requests.put("http://localhost:8000/products/genericupdateview/1/",json=data)
# # put is used here not post
# print(get_function_response.json()) 
# 
get_mixin_update=requests.put("http://localhost:8000/products/mixinview/15/",json=data)

print(get_mixin_update.json())


