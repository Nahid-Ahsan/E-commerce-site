from django.contrib import admin
from .models import *

admin.site.register(CategoryType)
admin.site.register(Category)
admin.site.register(ProductList)
admin.site.register(PlaceOrder)
admin.site.register(Transaction)
admin.site.register(PlaceOrder_Data)

class ProductListAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image', 'description')


class OrderListAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address', 'products', 'total_price', 'payment_type', 'transactions_id', 'transaction_date')

class TransactionListAdmin(admin.ModelAdmin):
    list_display = ('order','transaction_date' )