from django.shortcuts import render
from django.http import JsonResponse,Http404 # jsin response excepts dictionery as an argumnet whereas the httpreposne sends the text reponse back 
from . import models
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from auths.permissions import IsStaffEditorPermission
from auths.authentication import TokenAuthentication
from auths.mixins import StaffEditorPermissionMixin,UserQuerysetMixin # using this we no longer need to write permission_classes code.



# Create your views here.
def products_api(request,*args,**kwargs):
    model_data=models.Product.objects.all().order_by('?').first()# getting any random product that we find.
    data={} 
# This is not perfect we need to searilize the data we need the model dictionery, then we need to convert it to python dict and then return json
# product to client.
    # if model_data:
    #     data['id']=model_data.id
    #     data['title']=model_data.title
    #     data['content']=model_data.content
    #     data['price']=model_data.price  
    # return JsonResponse(data)
    if model_data:
        data=model_to_dict(model_data,fields=['id','title']) # by default we have all the fields getting default
        return JsonResponse(data)
# This above is the simple API view, now we will work on the dkjnago restframework api views ##########################################

from products.serializers import ProductSerialzer
# serializers deal with the presenattion of the data and how the data will be sent to the user and just like forms they can also take 
# in the data and clean the data 

@api_view(['GET'])# In the list we have to define what request we are allowing for..... like get and post
def django_products_api_get(request,*args,**kwargs):
    # It is now an API VIEW
    instance=models.Product.objects.all().order_by('?').first()
    data={}
    if instance:
        data = ProductSerialzer(instance).data
    return Response(data) 

@api_view(['POST'])# In the list we have to define what request we are allowing for..... like get and post
def django_products_api_post(request,*args,**kwargs):
    # It is now an API VIEW
    # use of serialzer for validating the data 
    serializer=ProductSerialzer(data=request.data)
    if serializer.is_valid(raise_exception=True): # It will tell you if you have some error in the posting the data .
    #     serializer.save() # it will save it in the database
    #     data=serializer.data
    # else:
    #     data=None
        print(serializer.data)
    return Response(serializer.data) # Just echoing back the post data 

#####################################################################################################################################

# Now we will be studyuing about the generic api views.
from rest_framework import generics, mixins,permissions,authentication

class ProductDetailAPIView(generics.RetrieveAPIView,StaffEditorPermissionMixin,UserQuerysetMixin):# Here we are getting the data.
    queryset=models.Product.objects.all() # getting all the products in the queryset.
    serializer_class = ProductSerialzer

    # Lookup_filed ='pk' which product to look for in the django, similar to products.object.get(pk=1)
    # It automatically looks up for the given primary key in the datatset

    # Copying the permission classes is a little bit redundant therefore we will use MIXINS for this so that we can access this 
    # Also studying about the throttling class, given one user how many requests can he make and making use of 
    # enginex would be better to control teh access for the entire project


class ProductCreateAPIView(generics.CreateAPIView,StaffEditorPermissionMixin):
    queryset=models.Product.objects.all()
    serializer_class=ProductSerialzer

    def perform_create(self,serializer):# this is a fucntion in generics createapi view which we are overwriting
        #serializer.save(user=self.request.user)
        title=serializer.validated_data.get('title')
        # validated_data is comming from serialzers class
        content=serializer.validated_data.get('content')
        if content is None:
            content=title
        serializer.save(user=self.request.user,content=content) 
        # Send a signal here 


# class ProductListAPIView(generics.ListAPIView):
#     queryset=models.Product.objects.all()
#     serializer_class=ProductSerialzer 
# We will not be using this method as there already exist a view named ListCreateAPIView

class ProductListCreateAPIView(UserQuerysetMixin,generics.ListCreateAPIView,StaffEditorPermissionMixin):
    queryset=models.Product.objects.all()
    serializer_class=ProductSerialzer
    # we no longer need authentication classess as we have added them in the settings module of our project
    #authentication_classes =[authentication.SessionAuthentication,TokenAuthentication] # this allow us to use tokens for authentication
   # permission_classes=[permissions.IsAdminUser, IsStaffEditorPermission]  # 1st we are checking whether the user is registered in the 
    # admin or not and then we define permissions based of the perission that are given to them

    # Just by adding this we are checking for the authentication of our application
    
# Sorting the data based of the users that we have in the system 
    def perform_create(self,serializer):# this is a fucntion in generics createapi view which we are overwriting
        #serializer.save(user=self.request.user)
        title=serializer.validated_data.get('title')
        # validated_data is comming from serialzers class
        content=serializer.validated_data.get('content')
        if content is None:
            content=title
        serializer.save(user=self.request.user,content=content) 

    # def get_queryset(self,*args,**kwargs): # we are commenting this out as we are using the mixinx for this 
    #     qs= super().get_queryset(*args,**kwargs)
    #     request=self.request
    #     user=request.user
    #     print(user)
    #     if not user.is_authenticated:
    #         return None
    #     print(qs.filter(user=1).values())
    #     return qs.filter(user=request.user).values() # filtering the data based of the users, We can also use this as a mixin as well.
    


# Using functions to create the above views for create, list views  and it takes more time but we can use these function based views 
@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args,**kwargs):
    method = request.method
    if pk is None:
        # If we have no arguments in the url we assume the list view otherwise we assume the detail view
        if method =="GET":
        # here we will be getting the args from the url and this will point towards the detail view, and list view
        # this is the list view 
            queryset=models.Product.objects.all()
            data=ProductSerialzer(queryset,many=True).data # many here will grab all the data 
            return Response(data)
    else:
        # queryset=models.Product.objects.filter(pk=pk) # getting the data for the given primary key 
        # if not queryset.exists():
        #     raise Http404
        # else: # This is simialr to get object or 404
        obj=get_object_or_404(models.Product,pk=pk)
        data = ProductSerialzer(obj).data
        return Response(data) 
    # FOr detail view we need to use the pk[details based per view]
    if method =="POST":
        # here we will be creating the items.
        serializer = ProductSerialzer(data=request.data)# this just matches the data with all the fields that we have defined in the 
        # serializer.py
        if serializer.is_valid(raise_exception=True):
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content')
            if content is None:
                content=title
            serializer.save(content = content) # we need to send content here because we are reassigning it with the title name.
            return Response(serializer.data)

################################## UPDATEAPIVIEW and DESTROYAPIVIEW ####################################################################

class ProductUpdateAPIView(generics.UpdateAPIView,StaffEditorPermissionMixin):# Here we are getting the data.
    queryset=models.Product.objects.all() # getting all the products in the queryset.
    serializer_class = ProductSerialzer
    lookup_field='pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content=instance.title

class ProductDestroyAPIView(generics.DestroyAPIView,StaffEditorPermissionMixin):# Here we are getting the data.
    queryset=models.Product.objects.all() # getting all the products in the queryset.
    serializer_class = ProductSerialzer
    lookup_field='pk'

    def perform_destroy(self, instance):
        # we are just repeting the same thing that is written on the main class of destroyapi view, so this is basically useless,
        # but we can perform som functions in between , like sending an email or other things before deleting an object.
        return super().perform_destroy(instance) # even without it it will still delete the data with given id 
    
########################## MIXINS #######################
# Difference between mixins and normal api views, is that use of mixins let us reuse the written code where as using the api views 
# we are reuing most of the code.

class ProductMixinView(generics.GenericAPIView,mixins.UpdateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin):
    queryset = models.Product.objects.all()
    serializer_class = ProductSerialzer
    lookup_field='pk'
# It doesn't matter whether the request is post or get, if we have defined the get and post method it will work accrodingly and return us the list of teh objects

    def get(self,request,*args,**kwargs): 
        # it will send us the entire list of the products that we have 
        print(args,kwargs)
        pk=kwargs.get('pk') # named parameter 
        if pk is not None:
            return self.retrieve(request,*args,**kwargs) 
        # based on the request argument it retrives the data.
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs) 
    
    def perform_create(self,serializer):
        #serializer.save(user=self.request.user)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content')
        if content is None:
            content=title
        serializer.save(content=content)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    # this will be used for updating the fields.



# like this we can use all of the functions, given to us for the previously to perform all teh tasks, we have to be careful for using the 
# put,get, post and delete requests 