from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokenAuthentication(BaseTokenAuth):
    keyword ="Bearer"
# If we delete the tokens then we can have to create them again and once the token is created you can use that token for 
# autehntication without any problem 