from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('task/', views.task,name='task'),
    path('calender/', views.calender,name='calender'),
    path('category/', views.category,name='category'),
    path('user/register/', views.user_registration, name='userregistration'),
    path('user/login/', views.user_login, name='userlogin'),
    path('user/home/', views.user_home, name='userhome')
    
]


 