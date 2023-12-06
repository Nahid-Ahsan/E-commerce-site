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
#     {"id": 1, "name": "Napa", "price": 10},
#     {"id": 2, "name": "Lipstick", "price": 20}
#   ]
# }


# http://127.0.0.1:8000/place_order/  [POST]
# {
#   "place_orders": [
#     {"name": "test1"},
#     {"phone":"3424234234"},
#     {"email": "test@gmail.com"},
#     {"address": "testaddress"},
#     {"products": [
#         {
#             "id": 1,
#             "name": "Napa",
#             "price": 10
#         },
#         {
#             "id": 2,
#             "name": "Lipstick",
#             "price": 20
#         }
#     ]},
#     {"total_price": 30},
#     {"payment_type": "bkash"},
#     {"transactions_id": "1234frggrerg"}
  
#   ]
# }


# http://127.0.0.1:8000/search/  [GET]

"napa"
