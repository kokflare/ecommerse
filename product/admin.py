from django.contrib import admin
from .models import Product, Card

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','desc']
    ordering = ('name',)

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['product','quantity']

