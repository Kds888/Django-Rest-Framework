# Ususally we define viewsets in the vuews.py file but as to keep this learning less complex I am defining it seprately.
from rest_framework import viewsets

from . import models

from .serializers import ProductSerialzer
# This is similar to teh APICREATE VIEW
class ProductViewSet(viewsets.ModelViewSet): # This is giving powerful access to us like we can do almost like anything with the given data 
    # here using this 
    # get-> get the list of items and get individual items 
    # and we also have something to post teh item 
    # we have put access to update and we also have patch which is to partial update 
    # and we can destroy the item entry 
    queryset = models.Product.objects.all()
    serializer_class=ProductSerialzer
    lookup_field='pk' # default 
# As they alow for almost all of the operations therefore we prefer to use different type of viewsets 
# this viewset is very similar to what we have in mixins in views.

from rest_framework import mixins

class ProductGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.RetrieveModelMixin):# iT allow us to use mixins therefore limiting the use of the viewsets and 
    # there fore we can control the CRUD operations
    # This will give us some control over the things that we want to do using CRUD
    queryset = models.Product.objects.all()
    serializer_class=ProductSerialzer
    lookup_field='pk'
    # Here we are not able to see the supported urls that are within this viewset therefore we need to define the urls as below

# product_list_view=ProductGenericViewSet.as_view({'get':'list'})# this will give you only the list of all the products 

# product_detail_view =ProductGenericViewSet.as_view({'get':'retrieve'}) 
# the above ways are the ways to get the views based of the methods in the routers and then we only pass these variables in teh routers for 
# different access levels 



