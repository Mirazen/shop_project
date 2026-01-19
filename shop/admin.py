from django.contrib import admin
from .models import User, Category, Manufacturer, Supplier, Product

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Supplier)
admin.site.register(Product)