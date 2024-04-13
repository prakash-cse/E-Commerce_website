from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('Chome',views.Chome,name="Chome"),
    path('Cregister',views.Cregister,name="Cregister"),
    path('Clogin',views.Clogin,name="Clogin")
]