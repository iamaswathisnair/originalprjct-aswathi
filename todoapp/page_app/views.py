from django.shortcuts import render,redirect
from .forms import userform
from .models import Profile

# Create your views here.

def home(request):
    return render(request,'home.html')
def task(request):
    return render(request,'task.html')
def calender(request):
    return render(request,'calender.html')
def category(request):
    return render(request,'category.html')
def login(request):
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username= request.POST.get('username')
        firstname= request.POST.get('firstname')
        lastname= request.POST.get('lastname')
        email= request.POST.get('email')
        password= request.POST.get('password')
        repassword= request.POST.get('repassword')
        print(username)
        print(firstname)
        print(lastname)
        print(email)
        print(password)
        print(repassword)

    return render(request,'register.html')

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
    return render(request,'login.html')
def user_home(request):
    return render(request,'user_home.html')

