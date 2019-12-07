
from django.contrib import admin
from .models import Shop, Product

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['거래처코드', '거래처명', '내용']
    list_display_links = ['거래처코드']
    ordering = ('거래처코드',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['품목코드', '품목명', '거래처코드']
    list_display_links = ['품목코드']
    ordering = ('품목코드',)