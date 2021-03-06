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
			username = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect('/')
	else:
		form = CustomNataUserForm()
	context = {
        'form' : form
    }
	return render(request, 'sign-up.html', context)

def sign_in(request):
	if request.session.get("_auth_user_id") == None:
		if request.method == "POST":
			user = authenticate(email=request.POST['email'], password=request.POST['password'])
			if (user != None):
				login(request, user)
			else :
				request.session["message"] = "Email or Password is invalid."
				return HttpResponseRedirect('/users/sign-in/')

			if request.session.get("message") != None:
				del request.session["message"]
			return HttpResponseRedirect('/')

		return render(request, 'sign-in.html')
	else:
		return HttpResponseRedirect("/")