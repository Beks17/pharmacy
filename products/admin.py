from django.contrib import admin
from .models import Product, ActiveIngredient, MedClass
# Register your models here.
admin.site.register(Product)
admin.site.register(ActiveIngredient)
admin.site.register(MedClass)