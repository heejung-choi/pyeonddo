from django.urls import path
from . import views

app_name = 'promotions'

urlpatterns = [
    path('', views.promotion, name='promotion'),
]
