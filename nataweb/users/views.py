from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import CustomNataUserForm


# Create your views here.

def sign_up(request):
	if request.method == "POST":
		form = CustomNataUserForm(request.POST)
		print(form.is_valid())
		if form.is_valid():
			print("=============================")
			print(form.cleaned_data['first_name'])
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect('/')
	else:
		form = CustomNataUserForm()
	context = {
        'form' : form
    }
	return render(request, 'test-sign-up.html', context)

def sign_in(request):
	if request.method == "POST":
		user = authenticate(email=request.POST['email'], password=request.POST['password'])
		login(request, user)
		return HttpResponseRedirect('/')

	return render(request, 'sign-in.html')
