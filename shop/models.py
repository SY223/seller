from django.db import models
from django.utils import timezone

#tryig to draft a model for a simple retail app that operates from backend
#the app will enter customer orders item by item, total it, determine if payment was successful
#Upon successful payment, total items price is deducted from total payment, 
# to determine if there are owings or repayments

class Location(models.Model):
    name = models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    zipcode = models.IntegerField(max_length=6)

    def __str__(self):
        return self.name

class Employee(models.Model):
    E_id = models.CharField(max_length=20, unique=True, blank=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.lastname    

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

#these customers are random person that make purchase at the store
#the unique thing about cutomers are their transaction id and date.
class Customer(models.Model):
    customer_name = models.CharField(max_length=50, blank=False)
    store = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name


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

class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=150)
    payment_method = models.CharField(max_length=150)
    amount_paid = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.payment_id}'





