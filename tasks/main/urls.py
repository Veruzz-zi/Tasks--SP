from django.urls import path
from . import views

urlpatterns = [
    path('MainForm/', views.mainForm, name="mainForm"),
    path('MainList/', views.mainList, name="mainList")
]