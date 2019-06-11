from django.shortcuts import render

# Create your views here.

def view_dummy(request):
	return render(request, 'Vendor.html')
