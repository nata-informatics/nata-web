from django.urls import path
from . import views


urlpatterns = [
    path('', views.test_base, name='test_base'),
    path('sign_up/', views.sign_up, name='sign_up')
]
