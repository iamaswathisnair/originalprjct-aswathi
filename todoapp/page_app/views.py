from django.shortcuts import render,redirect
from .forms import userform
from .models import Profile
from .models import Category
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

def is_user(user):  
    try:       
        return user.is_authenticated and (user.profile.type == 'USER')    
    except Profile.DoesNotExist:        
        return False      

def home(request):
    return render(request,'home.html')
def task(request):
    return render(request,'task.html')
def calender(request):
    return render(request,'calender.html')
 
def theme(request):
    return render(request,'theme.html')
def today(request):
    return render(request,'today.html')
def yesterday(request):
    return render(request,'yesterday.html')
def lastmonth(request):
    return render(request,'lastmonth.html')


def category(request):
    allCategory = Category.objects.all()
    return render(request,'category.html',{"category":allCategory})

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
    if request.method =='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                if(user.profile.type =='USER'):
                    return redirect("userhome")
                
    else:
        form = AuthenticationForm()
    return render(request,'login.html', {'form':form})

@user_passes_test(is_user,login_url='/user/login/')   
def user_home(request):
    return render(request,'user_home.html')

def logout_user(request):
    logout(request)
    return redirect('userlogin')