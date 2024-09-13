from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def student(request):
    return render(request,'pro.html')


def profile(request):
    return render(request,'profile.html')

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')