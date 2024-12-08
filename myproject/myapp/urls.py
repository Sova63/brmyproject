from django.urls import path
from .views import index,newsfirst

urlpatterns = [
    path('', index, name='index'),
    path('newsfirst', newsfirst,name='newsfirst')
]