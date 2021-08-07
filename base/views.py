from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request,'base/home.html')


def about(request):
    return render(request,'base/about.html')

def studio(request):
    return render(request,'base/studio.html')


def blog(request):
    return render(request,'base/blog.html')

def contact(request):
    return render(request,'base/contact.html')