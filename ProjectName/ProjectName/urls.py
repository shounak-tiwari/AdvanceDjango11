from django.urls import path
from app.views import index,get_index,update_information,delete_information

urlpatterns = [
    path('',index),
    path('get/',get_index),
    path('update/<int:id>',update_information),
    path('delete/<int:id>',delete_information)
]

# path is an function of urls which take views as an arguments 