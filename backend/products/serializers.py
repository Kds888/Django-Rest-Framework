from rest_framework import serializers # just help us view the data that we need to view.
from . models import Product
from . validators import  validate_title,validate_no_hello_in_title,unique_value_validator

from rest_framework.reverse import reverse
from auths.serializers import UserPublicSerializer

class ProductSerialzer(serializers.ModelSerializer):
   # user=serializers.CharField(read_only=True) # We are able to directly get the user here as we have deined in the models the user varuiable as well so serialzer is autmatically 
    # mapping it to our defined field.
    # this user object thatw e hvae created automatically captures the username for us and give us back the details.
    owner=UserPublicSerializer(source='user')# we can supply read_only arguments here also but we have already defined it in the serializers.
    # just defining that the my_discount field is read only
    my_discount=serializers.SerializerMethodField(read_only=True)
    # adding the urls for each product in its detail field
    detail_url = serializers.SerializerMethodField(read_only=True) # this is the bad way of doing this in total
    # the below method only works for model serializers only and takes care of all the function definations for us  
    update_url = serializers.HyperlinkedIdentityField(view_name='product-update',lookup_field='pk')# this is alos one of the way of achieving the same thing above
    # If we want to send an email to a person when we are creating a product 
    # email = serializers.EmailField(write_only=True), we can accept this from the user in the same form but while saving the form we will pop this 
    # out from the list, because there will be no filed in the model that can realte to it
    title=serializers.CharField(validators=[validate_no_hello_in_title,unique_value_validator]) # there is another way which we have showed below
    # Here charfiled can be changed with email field and similar so that we can have other fileds to validate those as well
    # name = serializer.Charfiled(source='title',read_only=True), making a copy of the given Title.

    class Meta:
        model=Product
        fields=['owner','detail_url','pk','sale_price','title','content','price','my_discount','update_url'] # I ahve removed the email as of now
    
    # Custom validation of the data 
    # def validate_<fieldname>:
    # any validation that we need to perform, like the one we are performing belwo basically tells us that we need to have unique values for titles.

    # def validate_title(self,value):
    #     qs=Product.objects.filter(title__exact=value)# if we do iexact instead of exact, then we will make it case insensitive
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} already exists in our data ")
    #     return value
    # We will do this in seprate file named validator.py.

    
    
    # this is the way of accessing the functions in the models that w e created 

    # def get_url(self,obj):
    #     return f"/auths/product_detail/{obj.pk}/"
    # this is not the good way of doing 
    # def create(self,validated_data):
    #     email = validated_data.pop('email') # This will get us the email of that person whom we have to send the information about what we 
    #     # added in the dataset 
    #     return super().create(validated_data)
    # # we can do this in perform_create method in the productcreate api view class also 

    # def update(self,instance,validated_data):
    #     instance.title=validated_data.get('title')
    #     return instance
    # This is all just an example to add an arbitray filed that we want but don't want to include in our database.
    # this will update the data based of the given title 
    

    def get_detail_url(self,obj):
        request=self.context.get('request')
        # we need to access the request this way as sometimes the Serializers don't have access to the self.request method
        if request is None:
            return None
        else:
            return reverse('product-detail',kwargs ={'pk':obj.pk},request=request)
        
    # def get_update_url(self,obj):
    #     request=self.context.get('request')
    #     if request is None:
    #         return None
    #     else:
    #         return reverse('product-update',kwargs ={'pk':obj.pk},request=request)
    # there is another way of achieving the same result

    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        return obj.get_discount()