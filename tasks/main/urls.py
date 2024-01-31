from django.urls import path
from . import views

app_name="tasks"
urlpatterns = [
    path('MainForm/', views.mainForm, name="mainForm"),
    path('', views.mainList, name="mainList"),
]