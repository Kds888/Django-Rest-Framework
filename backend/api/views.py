from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.


def api_home(request,*args,**kwargs):
    # the request that we get here will contain teh data that we are going to echoed
    data={}# empty dictionery that, will conatin all the info
    try:
        data = json.loads(request.body)# takes in json data and trun it into python dictionery
        print(data)# This Data will only contain the query set that the use is passing, not anything else.
    except:
        print("Empty")# Nothing is passed it the URL and we just prinet the empty URL.
        pass
    data['header']=dict(request.headers)
    data['params']=request.GET# get method here returns the parameters that we have sent it in the URL
    data['content_type']=request.content_type
    return JsonResponse(data)
# this demonstrates the way of getting back the data that you sent, specifically echoing back the data.
# we are gtting teh output as b'{"query": "Hello KDS"}', to geth the raw output we need the json library
############################################################################################################################
