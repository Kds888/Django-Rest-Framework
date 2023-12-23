# setting up a endpoint
# here the rest api request will send you the JSON object whereas the normal http reqiuest will send you html code

import requests

endpoint1 = "http://localhost:8000/api/"


#get_Response= requests.get(endpoint1)
#
# print("Simple JSON request to get the data")
#print(get_Response.text )
# It is just a simple way of getting the json response from the server side.

# Echoing the data means that, if I send something in the endpoint like mention below it should give me the data that I send it to in the 
# first place.


#get_Response= requests.get(endpoint1, params={'abc':123},json={'query':"Hello KDS"})# As we are sending data we need it to echo to us

# PArams here are query parameters we see them in the websites url as http://localhost:8000/api/?this_arg=this_value, so in our case it is
# http://localhost:8000/api/?abc=123 to acees these parameters we have the request.Get method aligned up
#print(get_Response.text)
######################################################################################################################################################

# Now we will be working on the django model instance as the API response.
# get_model_response_get = requests.get("http://localhost:8000/products/")
# print(get_model_response_get.text)

get_model_response_post = requests.post("http://localhost:8000/products/post/",json={'title':'Hello World'}) 
print(get_model_response_post.text)


