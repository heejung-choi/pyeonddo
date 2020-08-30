from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request,'maps/index.html')

def test(request):
    return render(request,'maps/test.html')