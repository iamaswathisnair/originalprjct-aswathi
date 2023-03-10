from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('task/', views.task,name='task'),
    path('calender/', views.calender,name='calender'),
    path('category/', views.category,name='category'),
    path('login/', views.login,name='login'),
    path('register/', views.register,name='register')
    
]


 