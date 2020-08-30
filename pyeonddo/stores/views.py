from django.shortcuts import render, redirect
from . models import Store

# Create your views here.
def kind(request):
    stores = Store.objects.all()
    for store in stores:
        print(store)
    context = {
        'stores' : stores,
        
    }
    return render(request,'stores/kind.html', context)
