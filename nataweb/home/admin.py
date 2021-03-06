from django.contrib import admin

from .models import *

class ProdukAdmin(admin.ModelAdmin):
    list_display = ["nama", "vendor", "harga"]
    list_filter = ["nama", "vendor"]
    search_fields = ["nama", "vendor"]

    class Meta:
        model = Produk

# Register your models here.
admin.site.register(Produk, ProdukAdmin)
