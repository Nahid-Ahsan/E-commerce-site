from rest_framework import generics
from .models import ProductList, PlaceOrder, Transaction
from .serializers import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q

class ProductListAPIView(generics.ListAPIView):
    queryset = ProductList.objects.all()
    serializer_class = ProductSerializer



class OrderCreateAPIView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        product_data = request.data.get('products', [])
        print(product_data)
        total_amount = sum(product['price'] for product in product_data)
        order_data = {'products': product_data, 'total_price': total_amount}
        
        return Response(order_data) 


class PlaceOrderAPIView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        placeOrder_data = request.data.get('place_orders', [])

        serialized_data = {}
        for item_data in placeOrder_data:
            for key, value in item_data.items():
                if key == "products":
                    serialized_data[key] = str(value)
                else:
                    serialized_data[key] = value 

        seialized_customer_data = {}
        for item_data in placeOrder_data:
            for key, value in item_data.items():
                if key in ["name", "phone", "email", "address"]:
                    seialized_customer_data[key] = value


        serializer = PlaceOrder_DataSerializer(data=serialized_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        customer_serializer = CustomerSerializer(data=seialized_customer_data)
        customer_serializer.is_valid(raise_exception=True)
        customer_serializer.save()


        return Response(serialized_data)



class ProductSearchAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        print(search_query)
        queryset = ProductList.objects.filter(
            Q(name__icontains=search_query) |
            Q(name__icontains=search_query.lower()) |
            Q(name__icontains=search_query.upper())
        )

        return queryset



class ProductFilterAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category__id = self.request.query_params.get('category', None)
        # category_type = self.request.query_params.get('category_type', None)
        print(category__id)

        queryset = ProductList.objects.all()
        print(queryset)

        if category__id:
            queryset = queryset.filter(category__id=category__id)

        # if category_type:
        #     queryset = queryset.filter(category__category_type=category_type)

        return queryset


