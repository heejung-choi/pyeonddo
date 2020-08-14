from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request,'tothers/index.html')

def signup(request):
    return render(request,'tothers/signup.html')

def signup2(request):
    return render(request,'tothers/signup2.html')

def update(request):
    return render(request,'tothers/update.html')