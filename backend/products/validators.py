from . models import Product
from rest_framework import serializers
from rest_framework import validators

# The best way to apply the basic unique type of validators is in the models, whereas when we need custom validation like email, or something similar
# to this we make use of validators.

def validate_title(value):
    qs=Product.objects.filter(title__exact=value)# if we do iexact instead of exact, then we will make it case insensitive
    if qs.exists():
        raise serializers.ValidationError(f"{value} already exists in our data ")
    return value

def validate_no_hello_in_title(value): # this is just an example of when we don't want something in our inputs thereafter we can use this for email validations
    if 'hello' in value.lower():
        raise serializers.ValidationError(f"{value} not allowed ")
    return value

unique_value_validator=validators.UniqueValidator(Product.objects.all(),lookup='iexact') # making it case sensitive
