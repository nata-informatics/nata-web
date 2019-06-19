from django.shortcuts import render

def catalog_page(request) :
    return render(request, 'catalog.html')
