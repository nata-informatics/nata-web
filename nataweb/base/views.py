from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from base.forms import NataUser

# Create your views here.
def test_base(request):
    return render(request, 'base.html')

def sign_up(request):
    if request.method == 'POST':
        form = NataUser(request.POST)
        if form.is_valid():
            f_fname = form.cleaned_data['first_name']
            f_lname = form.cleaned_data['last_name']
            f_email = form.cleaned_data['email']
            f_password = form.cleaned_data['password']
            f_password2 = form.cleaned_data['password2']
            f_birth = form.cleaned_data['date_of_birth']
            f_phone = form.cleaned_data['phone_number']

            # manual validation
            print(str(type(f_fname)) + ": " + f_fname)
            print(str(type(f_lname)) + ": " + f_lname)
            print(str(type(f_email)) + ": " + f_email)
            print(str(type(f_password)) + ": " + f_password)
            print(str(type(f_password2)) + ": " + f_password2)
            print(str(type(f_birth)) + ": " + str(f_birth))
            print(str(type(f_phone)) + ": " + str(f_phone))
            
            return HttpResponseRedirect('/landing/')
    else:
        form = NataUser()

    context = {
        'form' : form
    }
    return render(request, 'sign_up.html', context)

def test_sign_up(request):
    return render(request, 'test-sign-up.html')