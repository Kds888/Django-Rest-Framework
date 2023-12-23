# this will control what all data goes to algolia for search related purposes.

from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Product

@register(Product) # It is similar to admin.site.register 
class ProductIndex(AlgoliaIndex):
    should_index='is_public' # it is the function in the Products and it will only send the data to algolia where the public is true otherwise it won't 
# send the data.
    fields=[
        'title','content','user','price','public',
    ]

    settings={
        'searchableAttributes':['title','content'] # this is just inbuild functionalities in ALgolia where the search will only be done on the attributes mentiones
    }

    tags='get_tags_list'

# to let the algolia know about the fileds, we have the command known as algolia_reindex
# This is one of the way for us to implement the Search 