import requests

# get_model_response_post = requests.get("http://localhost:8000/products/genericretrieveview/1/",json={'title':'Hello World'}) 
# # here we are getting the details based of the retrieval view 
# print(get_model_response_post.json())

###############################################################3

# Using function based view 

# get_function_response = requests.get("http://localhost:8000/products/function/1/")

# print(get_function_response.json())  

get_response_mixin=requests.get("http://localhost:8000/products/mixinview/1/")
print(get_response_mixin.json()) 