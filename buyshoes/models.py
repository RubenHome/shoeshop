from django.db import models
from django.utils import timezone


class Shoe(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	image = models.CharField(max_length=200, default='')

	def __str__(self):
		return self.name

class Purchase(models.Model):
	client_name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	email = models.EmailField(max_length=100)

class CartManager(models.Manager):
	def create_cart(self,shoe,amount):
		cart = self.create(shoe=shoe,amount=amount)
		return cart

class Cart(models.Model):
	shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
	amount = models.IntegerField(default=0)

	objects = CartManager()


