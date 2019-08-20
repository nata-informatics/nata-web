from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-item/', views.addItem, name='addItem'),
    path('logout/', views.logout),
    path('detail-item/<id>/', views.detailItem),
]
