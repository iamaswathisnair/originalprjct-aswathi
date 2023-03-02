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