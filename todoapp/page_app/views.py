from django.shortcuts import render

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