from django.urls import path, register_converter
from . import views



app_name = 'myapp'

urlpatterns = [
    path('', views.shop_list, name='shop_list'),
    path('<str:pk>/', views.shop_detail, name='shop_detail'),
]
