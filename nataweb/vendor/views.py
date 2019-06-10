from django.shortcuts import render

# Create your views here.

def view_dummy():
	return render(request, 'Vendor.html')
