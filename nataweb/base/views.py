from django.shortcuts import render

# Create your views here.
def test_base(request):
    return render(request, 'base.html')