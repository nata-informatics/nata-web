from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk

# Create your views here.
def home(request):
	context = {}
	context["produks"] = Produk.objects.all()
	return render(request, 'home-farras.html', context)

def error_404_view(request, exception):
	data = {"name" : "ThePythonDjango.com"}
	return render(request, "error_404.html", data)

def addItem(request):
	if (request.user.is_superuser):
		if request.method == "POST":
			print(request.POST)
			namaItem = request.POST["namaProduk"]
			namaVendor = request.POST["namaVendor"]
			hargaProduk = request.POST["hargaProduk"]
			lokasiVendor = request.POST["lokasiVendor"]
			linkImg = request.POST["linkImg"]
			stockAvailabitlity = request.POST.get("stockAvailabitlity")
			if stockAvailabitlity == None : 
				stockAvailabitlity = False 
			else: 
				stockAvailabitlity = True
			print(stockAvailabitlity)
			Produk.objects.create(nama=namaItem, vendor=namaVendor, harga=hargaProduk, stok=stockAvailabitlity, lokasi=lokasiVendor, urlimg=linkImg)
			return redirect("/")
		return render(request, 'add-item.html')
	else:
		return redirect("/landing/")

def detailItem(request, id=None):
	produk_instance = get_object_or_404(Produk, id=id)
	context = {
		'produk' : produk_instance,
		'availability' : "Available" if produk_instance.stok == True else "Not Available",
	}
	return render(request, "produk-detail.html", context)

def displayItems(request):
	context = {}
	context["produks"] = Produk.objects.all()
	return render(request, "display-items.html", context)

def logout(request):
	request.session.flush()
	return redirect("/landing/")
