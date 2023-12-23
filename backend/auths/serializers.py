# This serializer is donated to user managemnet only as of now.

from rest_framework import serializers

from django.core import serializers as sz

class UserInlineSerialziser(serializers.Serializer): # this is from serializers.selrealizer whereas we ususally use serialzer.modelserializer whne we
    # are sending the data outwords.
    detail_url = serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk',read_only=True)
    title=serializers.CharField(read_only=True)
# this basically shows us how we can bring in the nested data, we can also do this in the original serialzers file that we have.
class UserPublicSerializer(serializers.Serializer):
    username=serializers.CharField(read_only=True,default="Ananoumous User")
    id=serializers.IntegerField(read_only=True,default=99999)

   # other_products=serializers.SerializerMethodField(read_only=True) # even if we define this it will not have any effect.

    def get_other_products(self,obj):
        user=obj
        my_products=user.product_set.all() # this is a way of using the user field to get the product data as we have a foriegn key relationship defined here
        # my_products=sz.serialize('json',my_products) # using this we can return all the user related data as well.

        # we are just doing this to get an idea about all the methods that we have available.
        return UserInlineSerialziser(my_products,many=True,context=self.context).data # the my_products is not json seriialzable