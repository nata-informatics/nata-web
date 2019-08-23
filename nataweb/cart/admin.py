from django.contrib import admin
from .models import *

class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "total"]
    list_filter = ["user"]
    search_fields = ["user"]

    class Meta:
        model = Cart

# Register your models here.
admin.site.register(Cart, CartAdmin)
# Register your models here.
