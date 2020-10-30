from django import forms
from .models import Purchase


class PurchaseForm(forms.ModelForm):

	class Meta:
		model = Purchase
		fields = ('client_name', 'address', "email")

	def __init__(self, *args, **kwargs):
		super(PurchaseForm, self).__init__(*args, **kwargs)
		self.fields['client_name'].label = "Name"