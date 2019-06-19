from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_page, name='catalog_page')
]
