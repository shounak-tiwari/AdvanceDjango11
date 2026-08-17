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
from .models import Info


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

# get apis 
@api_view(['GET'])
def get_index(request):
       data = Info.objects.all()
       serializer = InfoSerializers(data,many=True)

       return Response({
              "status":True,
              "message":"Data Fetched Successfully",
              "data":serializer.data,
              "code":HTTP_200_OK
       })
# update information :perform changes in existing data 
@api_view(['PUT'])
def update_information(request,id):
       try:
              data = Info.objects.get(id=id)
       except Info.DoesNotExist:
              return Response({
                     "status":False,
                     "message":"data not found",
                     "code":HTTP_404_NOT_FOUND
              })
       serializer = InfoSerializers(data,data = request.data)
       if serializer.is_valid():
              serializer.save()
              return Response({
                     "status":True,
                     "message" : "data updated successfully",
                     "code":HTTP_200_OK
              })
       else:
            return Response({
                   "status":False,
                   "message":"Invalid data",
                   "error":serializer.error,
                   "code":HTTP_400_BAD_REQUEST
            })
       
#delete : delete existing info in db 
@api_view(['DELETE'])
def delete_information(request,id):
       try:
              data = Info.objects.get(id=id)
       except Info.DoesNotExist:
              return Response({
                     "status":False,
                     "Message":"data not found",
                     "code":HTTP_404_NOT_FOUND
              })
       data.delete()
       return Response({
              "status":True,
              "message":"data deleted successfully",
              "code":HTTP_200_OK
       })