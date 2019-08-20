from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def showCart(request):
	return render(request, "show-cart.html")