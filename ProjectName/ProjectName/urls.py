from django.urls import path
from app.views import index

urlpatterns = [
    path('',index),
]

# path is an function of urls which take views as an arguments 