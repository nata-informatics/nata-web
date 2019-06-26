from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

def landing(request):
    if request.method == "POST":
	    user = authenticate(email=request.POST['email'], password=request.POST['password'])
	    login(request, user)
	    return HttpResponseRedirect('/')

    return render(request, 'landing.html')
