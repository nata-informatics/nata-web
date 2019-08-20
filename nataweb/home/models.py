from django.db import models

# Create your models here.
class Produks(models.Model):
	nama = models.CharField(max_length=255)
	vendor = models.CharField(max_length=255)
	urlimg = models.TextField(default="https://dummyimage.com/vga")
	harga = models.IntegerField()
	satuan = models.CharField(max_length=255, default="Box")
	stok = models.BooleanField()
	lokasi = models.CharField(max_length=255)
