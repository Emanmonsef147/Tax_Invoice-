from django.contrib import admin
from .models import Setting, Product, Invoice
# Register your models here.

admin.site.register(Setting)
admin.site.register(Product)
admin.site.register(Invoice)
