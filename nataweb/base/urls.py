from django.urls import path
from . import views


urlpatterns = [
    path('', views.test_base, name='test_base') 
]
