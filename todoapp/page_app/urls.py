from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('task/', views.task,name='task'),
    path('task/<int:id>', views.single_task,name='single-task'),
    path('task/delete/<int:id>', views.delete_task,name='delete-task'),
    path('task/add', views.add_task,name='add-task'),
    path('newtask/', views.newtask,name='newtask'),
    path('calender/', views.calender,name='calender'),
    path('category/', views.category,name='category'),
    path('theme/', views.theme,name='theme'),
    path('today/', views.today,name='today'),
    path('yesterday/', views.yesterday,name='yesterday'),
    
    

    path('user/logout/', views.logout_user,name='logout_user'),

    path('user/register/', views.user_registration, name='userregistration'),
    path('user/login/', views.user_login, name='userlogin'),
    path('user/home/', views.user_home, name='userhome')
    
    
]


 