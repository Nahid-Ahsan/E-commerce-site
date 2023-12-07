from django.urls import path

from .views import *

urlpatterns = [
   path('products/', ProductListAPIView.as_view(), name='product_list'),
   path('create_order/', OrderCreateAPIView.as_view(), name='create_order'),
   path('place_order/', PlaceOrderAPIView.as_view(), name='place_order'),
   path('search/', ProductSearchAPIView.as_view(), name='product-search'),
   path('filter/', ProductFilterAPIView.as_view(), name='product-filter'),
   # path('transactions/', TransactionListAPIView.as_view(), name='transaction_list'),
]



# http://127.0.0.1:8000/products/  [GET] 


#http://127.0.0.1:8000/create_order/ [GET]

# {
#   "products": [
#     {"id": 1, "name": "Baby Lotion", "price": 500.00},
#     {"id": 2, "name": "Gents Perfume", "price": 999.00},
#     {"id": 4, "name": "Napa", "price": 50.00}

#   ]
# }



# http://127.0.0.1:8000/place_order/  [POST]
# {
#   "place_orders": [
#     {"name": "test1"},
#     {"phone":"3424234234"},
#     {"email": "test@gmail.com"},
#     {"address": "testaddress"},
#     {    "products": [
#         {
#             "id": 1,
#             "name": "Baby Lotion",
#             "price": 500.0
#         },
#         {
#             "id": 2,
#             "name": "Gents Perfume",
#             "price": 999.0
#         },
#         {
#             "id": 4,
#             "name": "Napa",
#             "price": 50.0
#         }
#     ]},
#     {"total_price": 1549.0},
#     {"payment_type": "bkash"},
#     {"transactions_id": "1234frggrerg"}
  
#   ]
# }



# searching
# http://127.0.0.1:8000/search/?search=Napa [GET]

# Params:
# Key: search parameters
# Value: napa


# filtering
# http://127.0.0.1:8000/filter/?category=4 [POST]

# Params:
# Key: category
# Value: 4