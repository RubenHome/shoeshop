from django.shortcuts import render
from django.views import View
from buyshoes.models import *
from django.http import JsonResponse
from django.forms import model_to_dict


class ShoesListView(View):
	def get(self,request):
		shoes = Shoe.objects.all()
		return JsonResponse(list(shoes.values()), safe=False)


class ShoesDetailView(View):
	def get(self,request, pk):
		shoe = Shoe.objects.get(pk=pk)
		return JsonResponse(model_to_dict(shoe))
