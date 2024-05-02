from django.urls import path
from . import views

urlpatterns= [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('collections',views.collections,name="collections"),
    path('service/<int:id>',views.service,name="service"),
    path('collections/<str:cname>/<str:pname>',views.service_details,name="service_details"),
    path('shopname/<int:id>',views.shop_name,name="shopname"),
    path('support',views.support,name="support"),
    path('termsofuse',views.termsofuse,name="termsofuse")

]