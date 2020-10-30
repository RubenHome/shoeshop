from django.urls import path
from .views import ShoesListView, ShoesDetailView


urlpatterns = [
	path('shoes/', ShoesListView.as_view(), name='shoes_list'),
	path('shoes/<int:pk>/', ShoesDetailView.as_view(), name='shoe_detail'),
]