# Django-Rest-Framework 

It shows the use of REST API's with Django &amp; The Django Rest Framework

I have defined various apps within the projects to clarify what all the methods I am using, different apps contribute to different tasks, I have written many comments in the code explaining all the important parts of the code, Here on github I will just be giving a brief on what different apps contains and what all methods and ways are used in those apps to have a general understanding as to what is written in the code.

  App Name: - api

This app basically contains the information of how can we access the api endpoints using the requests library and how we can pass in the parameters and query arguments and how we can echo this data back and access it according to our requirements. We convert the json data sent to us in the form of a dictionery and accessing the data we get the query paramters that we have send in the data. I have commented all the necessary information and in the py_client folder I have all the information there to access the basic api view.

  App Name: - products

I have defined a single model with three components as follwos: - Price,Content and title and with 2 functions which are sale prices and discount, these don't have any significant means they are just for me to use them and understand the context, This app in intermingled with the auth's app and some things that will be mentioned here will also be mentioned there as well.

1. Serializers: - Serializers in Django REST Framework provide a way to convert complex data types, such as Django models, into a format that can be easily rendered into JSON, XML, or other content types. They also handle deserialization, which means they can take incoming data and convert it into a Python object that can be used to create or update a model instance. They can also be used to handle single incomming fields, for example making a field unique only by letting the user know that content already exist in that field.

Like forms, serializers can also perform validation on the data they receive, ensuring that it meets certain criteria before it is processed further. This can include checking that required fields are present, that data is of the correct type, or that it meets other custom validation rules you define.
They are basically similar to what forms do in the normal Django platform, They have an inbuild object validated_data through which we can access almost all of the products that we require, which we are doing in the project sometimes.

In the serialzers we have to use self.context.get('request') method to get the request object whereas in views we can simply use self.request.

2. Viewsets: - They are simply the already created classes that we can use to represent our data and they are provided by the rest_framework, which we can use in order to perform CRUD operations and they are very powerful, in order to control these views we may use mixins, and allowing for only specific operations through them. product_list_view=ProductGenericViewSet.as_view({'get':'list'}), this will give you only the list of all the products, product_detail_view =ProductGenericViewSet.as_view({'get':'retrieve'}), will fetch individual products that we need to pass the names as in the routers or urls.py to acceess the API's through this method.

3. Routers: - They are very similar to urls.py path function, but theya re provided by the rest_framework app and we can use them exactly as we use normal urls and they get appended in the urls, themselves. They are defined like this: - where router is an object of the function DefaultRouter(), from the rest_framework. router.register('product-router-with-mixin',ProductGenericViewSet,basename='productsmixin'), urlpatterns = router.urls. The SimpleRouter(), method will automatically generates Url, usually for all the operations that we can do.

4. Validators: - It is preffered to define most of the validators for the input in the models file but we may need custom validtors that we require, like email for some specific organizations in our appp therefore we can define them in our serializers or we can simply define them in their own file and then import them in serialziers.

5. Mixins: - A class that can be added into another classes so tha we can avoid making use of reducndant code, I have defined mixins in my auth app and we have two mixins defined there STAFFEDITORMIXIN AND USERQUERYSETMIXIN, to define staff permissions and to sort data based of users. 

We are also making use of the decorsator like api_view whcih control the access type like whether the model request in put,get,delete etc. so as to only give the access to those requests in function based views.

Class based views are very powerfull and we only need to write very few lines of code to create them, And we are using mixinx from rest_framework.generics that we can inherit in our class and then we can use them for performing CRUD operations, we have full control over how they should react by manipulating their default functions, this just save us time while coding, where as function based views are more flexible and explainable in themsleves.

In update and destroy view we have to use request.put and requests.delete methods while calling these views, whereas the patch method allows us to partially update a database as it is used in the project where there are a lot of fileds that needs to be updated.

For more information regarding all the methods I have used, you have to look in the views.py file in the products app. And in py_cleint I have commented out all the ways I am using to retrieve the data, and performin all functionalities that I have presented so far,

  App Name: - Auths

This app contains the authentication nechanism that I have been using like tokenauthentication, Staff mixin that I have created, authentication based of your group that we can configure in the admin.py file.

I am using various ways to authenticate the user basic one is to use the tokenauthentication as of now, so as to get the users authenticated so as to get access to the api calls that are made to the server, but the authentication that I am using is not much validated as I was not able to set the permissions that are needed for differnt users, through code, but Through the django backend portal I was able to set it up.









