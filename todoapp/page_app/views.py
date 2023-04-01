from django.shortcuts import render,redirect
from .forms import userform,TaskForm, TaskFormEdit
from .models import Profile,Task
from .models import Category
from .models import Quotes
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import user_passes_test
from datetime import datetime, timedelta
import random
# Create your views here.

def is_user(user):  
    try:       
        return user.is_authenticated and (user.profile.type == 'USER')    
    except Profile.DoesNotExist:        
        return False 

def home(request):
    quotes = Quotes.objects.all()
    qt = random.choice(quotes)
    if request.user and hasattr(request.user,'profile'):
        theme = request.user.profile.theme
    else:
        theme = "orange"
    if request.user:
        print("working")
    data ={
        "qt":qt,
        "user":is_user(request.user),
        "username":request.user.username,
        "theme":theme
    }
    print(request.user)
    return render(request,'home.html',data)

@user_passes_test(is_user,login_url='/user/login/') 
def task(request):

    catID = request.GET.get('categoryID')
    if catID:
        tasks = Task.objects.filter(added_by=request.user).filter(category=catID)
    else:
        tasks = Task.objects.filter(added_by=request.user)

    data ={
        "tasks":tasks,
        "user":is_user(request.user),
        "theme":request.user.profile.theme

    }
    return render(request,'task.html',data)

@user_passes_test(is_user,login_url='/user/login/') 
def single_task(request,id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task_form = TaskFormEdit(request.POST,request.FILES)
        if task_form.is_valid():
            task.completionstatus = task_form.cleaned_data['completionstatus']
            task.save()
            redirect(f'/tasks/{id}')
    else:
        task_form = TaskFormEdit()
    data ={
        "task":task,
        "user":is_user(request.user),
        "theme":request.user.profile.theme,
        "form":task_form
    }
    return render(request,'single-task.html',data)


@user_passes_test(is_user,login_url='/user/login/')    
def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST,request.FILES)
        if task_form.is_valid():
            task= Task()
            task.title = task_form.cleaned_data['title']
            task.start_date = task_form.cleaned_data['start_date']
            task.end_date = task_form.cleaned_data['end_date']
            task.deadline =task_form.cleaned_data['deadline']
            task.completionstatus  = task_form.cleaned_data['completionstatus']
            task.description  = task_form.cleaned_data['description']
            task.category  = task_form.cleaned_data['category']
            task.added_by = request.user
            task.save()
            return redirect('task')
    else:
        task_form = TaskForm()
    data ={
        "task_form":task_form,
        "user":request.user,
        "theme":request.user.profile.theme

    }
    return render(request,'add-task.html',data)

@user_passes_test(is_user,login_url='/user/login/')   
def delete_task(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('task')

@user_passes_test(is_user,login_url='/user/login/')   
def calender(request):
    data={
        "theme":request.user.profile.theme

    }
    return render(request,'calender.html',data)
 
def theme(request):
    theme = request.GET.get('theme')

    if theme:
        profile = Profile.objects.filter(user=request.user)[0]
        profile.theme = theme
        profile.save()
    data={
        "theme":request.user.profile.theme

    }
    return render(request,'theme.html',data)

@user_passes_test(is_user,login_url='/user/login/')   
def today(request):
    today = datetime.now().date()
    tasks = Task.objects.filter(start_date=today)
    data ={
        "tasks":tasks,
        "user":is_user(request.user),
        "theme":request.user.profile.theme
    }
    return render(request,'today.html',data)
    
@user_passes_test(is_user,login_url='/user/login/')       
def yesterday(request):
    yesterday =datetime.now() - timedelta(1)
    tasks = Task.objects.filter(start_date=yesterday.date())
    data ={
        "tasks":tasks,
        "user":is_user(request.user),
        "theme":request.user.profile.theme

    }
    return render(request,'yesterday.html',data)


def quote(request):
    return render(request,'home.html')

@user_passes_test(is_user,login_url='/user/login/')
def category(request):
    allCategory = Category.objects.all()
    return render(request,'category.html',{"category":allCategory,"user":request.user,"theme":request.user.profile.theme})

def user_registration(request):
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile()
            profile.type = 'USER'
            profile.user = user
            profile.save()
            return redirect('userlogin')
    else:
        form = userform()
    return render(request,'register.html' ,{'form':form})
   
def user_login(request):
    if request.method =='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                if(user.profile.type =='USER'):
                    return redirect("home")
                
    else:
        form = AuthenticationForm()
    return render(request,'login.html', {'form':form})

@user_passes_test(is_user,login_url='/user/login/')   
def user_home(request):
    return render(request,'user_home.html')

def logout_user(request):
    logout(request)
    return redirect('userlogin')

def newtask(request):
    return redirect(request,'task.html')