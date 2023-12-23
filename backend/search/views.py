from django.shortcuts import render
from products.models import Product
from products.serializers import ProductSerialzer
from rest_framework.response import Response

from . import client

# Create your views here.

# we have created this app to check our search functionality in the app.

from rest_framework import generics

class SearchListOldView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerialzer

    def get_queryset(self,*args,**kwargs):
        qs=super().get_queryset(*args,**kwargs) # this is just getting the queryset 
        q=self.request.GET.get('q')# Getting the parameter q from the url
        results=Product.objects.none()# If there are no products availabe for the given query.
        if q is not None:
            user=None
            if self.request.user.is_authenticated:
                user=self.request.user
            results=qs.search(q,user=user)
        return results
    

class SearchListView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerialzer

    def get(self,request,*args,**kwargs):
        query=request.GET.get('q')
        if not query:
            return Response('',status=400)
        else:
            results =client.perform_search(query)
            return Response(results)
    
