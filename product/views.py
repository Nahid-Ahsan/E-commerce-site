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


# class TransactionReportCreateAPIView(generics.CreateAPIView):
#     queryset = TransactionReport.objects.all()
#     serializer_class = TransactionReportSerializer

#     def create(self, request, *args, **kwargs):
#         # Retrieve order and transaction data from the request
#         order_id = request.data.get('order_id')
#         transaction_details = request.data.get('transaction_details', 'No transaction details provided.')

        # Create the transaction report
        # transaction_report_data = {'order': order_id, 'transaction_details': transaction_details}
        # transaction_report_serializer = TransactionReportSerializer(data=transaction_report_data)
        # if transaction_report_serializer.is_valid():
        #     transaction_report = transaction_report_serializer.save()
        # else:
        #     return Response(transaction_report_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         return Response(TransactionReportSerializer(transaction_report).data, status=status.HTTP_201_CREATED)
