import requests

# get_model_response_post = requests.get("http://localhost:8000/products/genericlistview/") 
# # we have to b ecraefull in this view because if we send the post request then we are creating the data and if we send the get request
# # we are getting the list of the data 
# # Here we can list the data and can also create the data as this the list and create view in django 
# print(get_model_response_post.json())

##############################################################33

# Function based calls 
# get_function_response=requests.get("http://localhost:8000/products/function/")

# print(get_function_response.json())

# Using MIXIN's

# get_response_mixin=requests.get("http://localhost:8000/auths/product_list_create/")
# print(get_response_mixin.json()) 

from getpass import getpass
username = input("What is your Username?\n")

password= getpass("What is your Password?\n") # using this we are jsut hashing out our password, which simply means we will get same output for same content entered 


auth_endpoint = "http://localhost:8000/auths/" # to get the token for our authentication.

auth_response = requests.post(auth_endpoint,json ={'username':username,'password':password})
# Auth response give us back the token that is authorized to access the page 
# the above code is used for autheticating the user, whether the user is valid and whether his credentials are valid or not 
if auth_response.status_code == 200:# if user gets authenticated 
    token = auth_response.json()['token']
    headers={
        'Authorization':f"Bearer {token}" # we can change the name of the authentication like bearer to anything by overwriting it 
        # in the authtokenclass, as I have done in authentication.py file in auths app
    }
    get_response_after_auth = requests.get("http://localhost:8000/auths/product_list_create/",headers=headers)
    # we are passing the authenticated token that is the user's password in the url to get access to the page view.
    print(get_response_after_auth.json())

    # due to introduction of pagination we may have to change our pyclient information.
    # we can create a recursive loop call to the function which will keep on getting the new data for us 
    
    # using pagination we can get this data for us while using the method below.

while True:
    next_url=get_response_after_auth.json()['next']
    if next_url is not None:
        get_response_after_auth = requests.get(next_url,headers=headers)
        print(get_response_after_auth.json())
    else:
        break


