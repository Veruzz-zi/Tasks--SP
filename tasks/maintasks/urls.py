from django.urls import path
from . import views
from views import index

url patterns = [
    path('', views.index, name=index)
]