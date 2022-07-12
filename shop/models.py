from django.db import models
from django.utils import timezone

#tryig to draft a model for a simple retail app that operates from backend
#the app will enter customer orders item by item, total it, determine if payment was successful
#Upon successful payment, total items price is deducted from total payment, 
# to determine if there are owings or repayments



class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=200)
    cart_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=250)
    price = models.FloatField()
    image = models.ImageField(upload_to='photos/product')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.customer_name


class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=150)
    payment_method = models.CharField(max_length=150)
    amount_paid = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.payment_id}'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=10, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    total = models.FloatField() 
    owings = models.FloatField() #Amount to pay as change to customer
    repayments = models.FloatField() #Amount customer owe us
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer



