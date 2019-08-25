from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Transaction
from users.models import CustomUser
from home.models import Produk

# Create your views here.
def showCart(request):	
	return render(request, "show-cart.html")

def getOrCreateCart(request):
	userId = request.session.get("_auth_user_id", None)
	if userId != None:		
		userObj = CustomUser.objects.get(id=userId)	
		cart = Transaction.objects.filter(user=userObj)	
		if cart.count() != 1:
			cart = Transaction.objects.create(user=userObj)
		else:
			cart = Transaction.objects.get(user=userObj)
		
		if request.method == "POST":			
			produkId = request.POST.get("produkId")
			produkToBeAdded = get_object_or_404(Produk,id=produkId)
			for i in cart.products.all():
				print(i)
			#cart.products.add(produkToBeAdded)
			print(cart.products)
			return HttpResponse(cart.products.all())
	else:
		return redirect("/home/")