from django.urls import path
from . import views 

urlpatterns=[
    path('', views.home ,name="main"),
    path('ingresar/', views.login ,name="login"),
       
]