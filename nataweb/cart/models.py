from django.db import models
from users.models import CustomUser
from home.models import Produk

class Transaction(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	products = models.ManyToManyField(Produk, blank=True)
	total = models.IntegerField(default=0)
	updated = models.DateTimeField(auto_now=True)
	added = models.DateTimeField(auto_now_add=True)

class OrderedProduct(models.Model):
	transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
	produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	jumlah = models.IntegerField(default=0)
