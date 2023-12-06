from rest_framework import serializers
from .models import ProductList, PlaceOrder, Transaction, PlaceOrder_Data

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductList
        fields = '__all__'



class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class OrderedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductList
        fields = ['id', 'name', 'price']



# class PlaceOrderSerializer(serializers.ModelSerializer):
#     products = OrderedProductSerializer(many=True)

#     class Meta:
#         model = PlaceOrder
#         fields = ['name', 'phone', 'email', 'address', 'products', 'total_price', 'payment_type', 'transactions_id']

#     def create(self, validated_data):
#         products_data = validated_data.pop('products', [])  # Extract products data

#         # Create and add related ProductList instances
#         place_order_instance = PlaceOrder.objects.create(**validated_data)
#         for product_data in products_data:
#             product_instance = ProductList.objects.create(**product_data)
#             place_order_instance.products.add(product_instance)

#         return place_order_instance

class PlaceOrder_DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceOrder_Data
        fields = ['name', 'phone', 'email', 'address', 'products', 'total_price', 'payment_type', 'transactions_id']