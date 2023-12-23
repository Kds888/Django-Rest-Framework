from django.urls import path 
from products.views import ProductListCreateAPIView,ProductDetailAPIView
from rest_framework.authtoken.views import obtain_auth_token # it is a pregiven library that we are using to get the things done like getting and 
# generating the token given that we are using this to get the 

urlpatterns =[
    path('product_list_create/',ProductListCreateAPIView.as_view()),
    path('product_detail/<int:pk>/',ProductDetailAPIView.as_view()),
    path('',obtain_auth_token),
]