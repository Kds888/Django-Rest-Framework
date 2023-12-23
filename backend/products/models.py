from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet  # auth.user
from django.db.models import Q 
import random
# Create your models here.
# we are going to create a method on the model below to filter the queryset whether it is public or not 

TAGS_MODEL_VALUE =['electronics','camera','cars','boats']

class ProductQueryset(models.QuerySet):
    def is_public(self):
        return self.filter(public=True) 
    def search(self,query,user=None):
        # the below statement checks for query to be in either title or content
        lookup= Q(title__icontains=query) | Q(content__icontains=query) # becuase of Q we can write queries like that we have seen this in django
        # where we can write queries like this or using filter twice
        qs=self.is_public().filter(lookup)
        if user is not None:
            # qs=qs.filter(user=user)# this would only show us teh data with the guiven user and with only public data
            # but if we want the user data whether its public or non public for that user only.
            qs2=self.filter(user=user).filter(lookup)
            qs=(qs|qs2).distinct() # to get like only unique data , and now e will have a ll the data for the given user, where it doesn't matter 
            # whether it is public or not.
        return qs # this will performa case insesitive searchbased of the query in the set 
        
class ProductManager(models.Manager):

    def get_queryset(self,*args,**kwargs):
        return ProductQueryset(self.model,using=self._db)# sending the data of the model from the database and in turn getting back the data when it is filtered.
    
    def search(self,query,user=None):
        return self.get_queryset().search(query,user=user)
    # using the get_queryset we will have an object of the Product queryset class, on wqhich we can call the is_public function which then filters the dataset based of the 
    # title 

# we are updating our user model so that a user gets attached to it.


class Product(models.Model):
    user=models.ForeignKey(User,default=1,on_delete=models.SET_NULL,null=True) # We are setting the default ID of the user to be one.
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=15,decimal_places=2,default=99.99)
    public=models.BooleanField(default=True) # search only public records that we have

    objects=ProductManager() # in get queryset the search function will be passed here

    def is_public(self):
        return self.public
    
    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUE)]

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)# basically giving an 80% discount 
    # this functionality exist in the django framework but not in the normal djnago jsonresponse that's why we can't se this price
    # there fore we will use rest_framework based serializers.
    def get_discount(self): # some confusion is still there in the process
        return "122"