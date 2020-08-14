from django.urls import path
from . import views

app_name = 'tothers'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),  
    path('signup2/', views.signup2, name='signup2'),  
    path('update/', views.update, name='update'),        
]

