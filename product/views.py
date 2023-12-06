from rest_framework import generics
from .models import ProductList, PlaceOrder, Transaction
from .serializers import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import status


class ProductListAPIView(generics.ListAPIView):
    queryset = ProductList.objects.all()
    serializer_class = ProductSerializer



class OrderCreateAPIView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        product_data = request.data.get('products', [])
        print(product_data)
        total_amount = sum(product['price'] for product in product_data)
        order_data = {'products': product_data, 'total_amount': total_amount}
        
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

        serializer = PlaceOrder_DataSerializer(data=serialized_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serialized_data)



class ProductSearchAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        queryset = ProductList.objects.filter(name__icontains=search_query)

        return queryset



class ProductFilterAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category__id = self.request.query_params.get('category', None)
        # category_type = self.request.query_params.get('category_type', None)

        queryset = ProductList.objects.all()

        if category:
            queryset = queryset.filter(category__id=category__id)

        # if category_type:
        #     queryset = queryset.filter(category__category_type=category_type)

        return queryset


