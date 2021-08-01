from django.contrib import admin
from .models import Product,Contact
# Register your models here.
@admin.register(Product)
class Product(admin.ModelAdmin):
    pass

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    pass