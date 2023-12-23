from django.urls import path
from . import views


urlpatterns=[
    path('',views.django_products_api_get,name='products'),
    path('post/',views.django_products_api_post, name ='post_products'),
    path('genericretrieveview/<int:pk>/',views.ProductDetailAPIView.as_view(),name='product-detail'),
    path('genericcreateview/',views.ProductCreateAPIView.as_view()),
    path('genericlistview/',views.ProductListCreateAPIView.as_view(),name='product-list'),
    path('function/<int:pk>/',views.product_alt_view),
    path('function/',views.product_alt_view),
    path('genericdestroyview/<int:pk>/',views.ProductDestroyAPIView.as_view()),
    path('genericupdateview/<int:pk>/',views.ProductUpdateAPIView.as_view(),name='product-update'),
    path('mixinview/',views.ProductMixinView.as_view()),
    path('mixinview/<int:pk>/',views.ProductMixinView.as_view()),
    


]