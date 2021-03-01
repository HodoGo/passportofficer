from django.urls import path
from .views import index

app_name = 'HouseApp'
urlpatterns = [
    path('',index,name='index'),
]
