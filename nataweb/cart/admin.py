from django.contrib import admin
from .models import *

class TransactionAdmin(admin.ModelAdmin):
    list_display = ["user", "total"]
    list_filter = ["user"]
    search_fields = ["user"]

    class Meta:
        model = Transaction

# Register your models here.
admin.site.register(Transaction, TransactionAdmin)
# Register your models here.
