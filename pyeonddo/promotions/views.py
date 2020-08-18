from django.shortcuts import render

# Create your views here.
def promotion(request):
    return render(request,'promotions/promotion.html')