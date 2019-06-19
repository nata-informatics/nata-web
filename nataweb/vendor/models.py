from django.db import models

# Create your models here.

class Vendor(models.Model):
	nama = models.CharField(max_length=50)
	lokasi = models.TextField(max_length=100, null=True)
	deskripsi = models.TextField(max_length=300, null=True)

class Jenis_Barang(models.Model):
	nama = models.CharField(max_length=50)

class Kontak(models.Model):
	vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
	website = models.CharField(max_length=50, null=True)
	email = models.CharField(max_length=50)
	no_hp = models.CharField(max_length=50)
	facebook = models.CharField(max_length=50)
	twitter = models.CharField(max_length=50)
	instagram = models.CharField(max_length=50)
	line = models.CharField(max_length=50)

class Jenis_Barang_Vendor(models.Model):
	vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
	jenis_barang = models.ForeignKey('Jenis_Barang', on_delete=models.CASCADE)

class Testimoni(models.Model):
	vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
	deskripsi = models.TextField(max_length=300, null=True)

class Barang(models.Model):
	vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
	jenis_barang = models.ForeignKey('Jenis_Barang', on_delete=models.CASCADE)
	nama = models.TextField(max_length=50)
	harga = models.PositiveIntegerField()
	deskripsi = models.TextField(max_length=300, null=True)

class Gambar_Barang(models.Model):
	barang = models.ForeignKey('Barang', on_delete=models.CASCADE)
	link = models.TextField(max_length=100)
