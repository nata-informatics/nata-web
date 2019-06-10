from django.conf.urls import url
from django.urls import path
from .views import *

# app_name = "cscareapp"
urlpatterns = [
	path('dummy/', view_dummy, name='dummy')
]
