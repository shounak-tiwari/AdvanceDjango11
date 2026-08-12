from django.http import HttpResponse
'''
views.py is reposible for showing ouptut or what you want to send or anyoperations of clint and server 

views is divide into two cato 
a. function based views 
b. class based views 
basic syntax of functions
def functionname(request):
    return response("anything or any statements  ")
'''
from rest_framework.decorators import api_view
from .serializer import InfoSerializers
from rest_framework.response import Response
from rest_framework.status import * 


@api_view(['POST'])
def index(request):
    data1 = InfoSerializers(data = request.data) 
    if data1.is_valid():
            data1.save()
            return Response({
                "status":True,
                "message":"data is saved into db",
                "code": HTTP_201_CREATED
            })
    else:
            return Response({
                "status":False,
                "message":"invalid data",
                "code" : HTTP_406_NOT_ACCEPTABLE
            })
        