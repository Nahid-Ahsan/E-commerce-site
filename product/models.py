from django.db import models

class CategoryType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    category_type = models.ForeignKey(CategoryType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProductList(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='food_images/',  blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

class PlaceOrder(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.TextField()
    products = models.TextField()
    # products = models.ManyToManyField(ProductList)
    # products = JSONField()
    # products = models.ListField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=50)
    transactions_id = models.CharField(max_length=255)
    transaction_date = models.DateTimeField(auto_now_add=True)

class PlaceOrder_Data(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.TextField()
    products = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=50)
    transactions_id = models.CharField(max_length=255)
    transaction_date = models.DateTimeField(auto_now_add=True)

# class OrderedProducts(models.Model):
#     data = models.JSONField()
    
class Transaction(models.Model):
    order = models.OneToOneField(PlaceOrder, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order

