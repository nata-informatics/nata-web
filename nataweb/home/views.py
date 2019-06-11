from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def logout(request):
	request.session.flush()
	return redirect("/")
