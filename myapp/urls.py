from django.urls import path, register_converter
from . import views

from django_filters.views import FilterView
from .filters import ShopFilter as uu


app_name = 'myapp'

urlpatterns = [
    path('list', views.shop_list, name='shop_list'),
    path('list/<str:pk>/', views.shop_detail, name='shop_detail'),
    path('new/', views.shop_new, name='shop_new'),
    path('list/<str:pk>/edit', views.shop_edit, name='shop_edit'),
    path('list/<str:pk>/delete', views.shop_delete, name='shop_delete'),
    path('list2', FilterView.as_view(
                filterset_class = uu,
                template_name = 'myapp/shop_list_filter.html'),
         name = 'index')
]
