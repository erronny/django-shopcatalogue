from django.contrib import admin
from .models import Products, Catagory,Brand

# Register your models here.
admin.site.register(Products)
admin.site.register(Catagory)
admin.site.register(Brand)