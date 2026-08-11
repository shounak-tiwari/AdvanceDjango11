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

def index(request):
    return HttpResponse("Hello wellcome to  Django ! it is virtaul world")