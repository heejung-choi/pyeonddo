from django.shortcuts import render
from .models import Product

# Create your views here.
def promotion(request, brand):
    product = Product.objects.get(brand=brand)
    context = {
        'product': product,
    }
    return render(request, 'promotions/promotion.html', context)