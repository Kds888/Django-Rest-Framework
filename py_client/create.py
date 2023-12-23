import requests
# data={
#     'title': "Through generic create view"
# }

# get_model_response_post = requests.post("http://localhost:8000/products/genericcreateview/", json=data) 
# # Here we can create the data

# print(get_model_response_post.json())


data ={
    'title': "IMplemeting authentication based view"
}

# get_function_response_post = requests.post("http://localhost:8000/products/function/",json = data)

# print(get_function_response_post.json()) 

get_mixin_response_create=requests.post("http://localhost:8000/auths/product_list_create/",json=data)
print(get_mixin_response_create.json())

# IN this we receieve the content is None as we ahve not defined the perform_create method here.