from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from .models import Shoe, Purchase, Cart
from django.core import serializers
from .forms import PurchaseForm
import json, csv, smtplib, datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def shoes_list(request):
	shoes = Shoe.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
	json_data = serializers.serialize("json",shoes)
	context = {
		"json": json_data,
		"shoes": shoes,
	}
	return render(request, 'buyshoes/shoes_list.html', context)


def purchase(request):
	form = PurchaseForm()
	cart = Cart.objects.all()
	total = 0;
	shoes = dict();
	for c in cart:
		shoe = Shoe.objects.filter(pk=c.shoe.id).first()
		shoe_amount = float(shoe.price)*float(c.amount)
		total = total + shoe_amount
		shoes[shoe.name] = c.amount
	return render(request, 'buyshoes/purchase_form.html', {'form': form, 'total': total, 'shoes_list': shoes})


def finish_purchase(request):
	cart = Cart.objects.all()
	total = 0;
	shoes = dict();
	for c in cart:
		shoe = Shoe.objects.filter(pk=c.shoe.id).first()
		shoe_amount = float(shoe.price)*float(c.amount)
		total = total + shoe_amount
		shoes[shoe.name] = c.amount
	name = request.POST['client_name']
	address = request.POST['address']
	email = request.POST['email']
	with open("reports/purchase_report.csv","w") as f:
		writer = csv.writer(f,delimiter=",")
		writer.writerow(['Shoe','Amount','Total'])
		for key, value in shoes.items():
			shoe = Shoe.objects.filter(name=key).first()
			price = float(value) * float(shoe.price)
			writer.writerow([key,value,price])
	send_mail(name,address,email)
	cart = Cart.objects.all().delete()
	shoes = Shoe.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
	json_data = serializers.serialize("json",shoes)
	context = {
		"json": json_data,
		"shoes": shoes,
		"result": "ok",
	}
	return render(request, 'buyshoes/shoes_list.html', context)

def send_mail(name,address,email):
	SERVER = "in-v3.mailjet.com"
	SERVER_PORT = "587"
	SUBJECT = "Purchase Summary"
	FROM = "ruben.tinformatica@gmail.com"
	PASSWD = "0459523f496bf2875f91890bf63b0e31"
	USER = "3205314969a347191b63078606d97b72"
	TO = email
	BODY = getBody(name,address)
	msg = MIMEMultipart()
	msg['Subject'] = SUBJECT
	msg['From'] = FROM
	msg['To'] = TO
	fp = open('reports/purchase_report.csv','rb')
	adj = MIMEBase('multipart', 'encrypted')
	adj.set_payload(fp.read())
	fp.close()
	encoders.encode_quopri(adj)
	adj.add_header('Content-Disposition', 'attachment', filename='purchase_report.csv')
	msg.attach(MIMEText(BODY, 'html'))
	msg.attach(adj)
	TEXT = msg.as_string()
	server = smtplib.SMTP(SERVER,SERVER_PORT)
	server.starttls()
	server.login(USER,PASSWD)
	server.sendmail(FROM,TO,TEXT)
	server.quit()


def getBody(name,address):
	body = "Dear " + name + ", we send you the purchase report in a csv file."
	body += "The shoes, will be sended to address " + address + "."
	body += "Thanks for trust us. King Regards"
	return body

def add_cart(request):
	data = request.GET
	shoe_index = data.get('shoe_index')
	shoe_amount = data.get('shoe_amount')
	shoe = Shoe.objects.filter(pk=shoe_index).first()
	c = Cart.objects.create_cart(shoe,shoe_amount)
	c.save()
	return JsonResponse([200,'OK'], safe=False)