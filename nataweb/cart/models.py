from django.db import models
from users.models import CustomUser
from home.models import Produks

class Cart(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	products = models.ManyToManyField(Produks, blank=True)
	total = models.IntegerField(default=0)
	updated = models.DateTimeField(auto_now=True)
	added = models.DateTimeField(auto_now_add=True)
