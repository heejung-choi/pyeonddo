from django.urls import path
from . import views

app_name = 'stores'

urlpatterns = [
    path('kind', views.kind, name='kind'),
]
