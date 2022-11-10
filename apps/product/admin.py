from django.contrib import admin
from .models import Category, Product, ProductImage


class TabularInlineImage(admin.TabularInline):
    model = ProductImage
    extra = 0
    fields = ['image']


class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [TabularInlineImage, ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
