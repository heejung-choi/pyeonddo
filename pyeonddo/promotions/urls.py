from django.urls import path
from . import views

app_name = 'promotions'

urlpatterns = [
    path('<str:brand>/', views.promotion, name='promotion'),
]


# 동동규 복습용
# urlpatterns = [
#    path('result/<str:food_ctg>/', views.result, name='result'),
#    path('result/', views.hangover, name='hangover'),
#    path('select/<str:food_name>/', views.select, name='select'),
# ]
# <a href="{% url 'foods:result' foodCategory.food_ctg %}"><img src="{{ foodCategory.food_ctg_image.url }}" class="img-square"></a>
