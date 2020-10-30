from django.urls import path
from . import views

app_name = 'buyshoes'

urlpatterns = [
	path('', views.shoes_list, name='shoes_list'),
	path('purchase', views.purchase, name='purchase'),
	path('finish_purchase', views.finish_purchase, name='finish_purchase'),
	path('add_cart', views.add_cart, name='add_cart'),
]