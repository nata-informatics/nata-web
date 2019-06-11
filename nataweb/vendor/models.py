from django.db import models

# Create your models here.
class Vendor(models.Model):
	nama = models.TextField()
	deskripsi = models.TextField()