import datetime
from django.db import models
from django.utils import timezone
from decimal import *
from phonenumber_field.modelfields import PhoneNumberField                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
import random
from django.utils.text import slugify

MAX_TRIES = 32
REF_LENGTH = 150 
CHARSET = '0123456789abcdefghjkmnpqrstvwxyz'
UPCHARSET = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
NUMDIGIT = '0123456789'

class Location(models.Model):
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=6)
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    employee_ref = models.CharField(max_length=10, unique=True, null=True)
    store_location = models.ForeignKey(Location, on_delete=models.SET_NULL, related_name='employee_store', null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    employee_nu = PhoneNumberField()
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if not self.id:
            loop_num = 0
            unique = False
            while not unique:
                if loop_num < MAX_TRIES:
                    new_code = ""
                    for i in range(REF_LENGTH):
                        new_code += CHARSET[random.randrange(0,len(CHARSET))]
                    if not Employee.objects.filter(employee_ref=new_code).exists():
                        self.employee_ref = new_code
                        unique = True
                    loop_num+=1
                else:
                    raise ValueError("Staff with reference already exists")
            self.date_created = datetime.datetime.now(tz=timezone.utc)
        self.modified_date = datetime.datetime.now(tz=timezone.utc)
        return super(Employee, self).save(*args, **kwargs)


    

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True, default='')
    description = models.TextField()
    cart_image = models.ImageField(upload_to='photos/categories', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save()

class Product(models.Model):
    item = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=15,decimal_places=2, default=Decimal('0.00'))
    image = models.ImageField(upload_to='photos/product', null=True, blank=True)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    slug = models.SlugField(blank=True, default='')
    is_available = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item

    def save(self, *args, **kwargs):
        self.slug = slugify(self.item)
        super(Product, self).save()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = datetime.datetime.now(tz=timezone.utc)
        self.modified_date = datetime.datetime.now(tz=timezone.utc)
        return super(Product, self).save(*args, **kwargs)
        

class Customer(models.Model):
    customer_name = models.CharField(max_length=50, blank=False)
    customer_email = models.EmailField(unique=True)
    customer_nu = PhoneNumberField()
    store = models.ManyToManyField(Location, related_name='store_location')
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name



class Order(models.Model):
    order_ref = models.CharField(max_length=10, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    items = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    price = models.DecimalField(max_digits=15,decimal_places=2, default=Decimal('0.00'))
    quantity = models.IntegerField()
    total = models.DecimalField (max_digits=15,decimal_places=2, default=Decimal('0.00'))
    total_paid = models.DecimalField(max_digits=15,decimal_places=2, default=Decimal('0.00'))
    balance = models.DecimalField(max_digits=15,decimal_places=2, default=Decimal('0.00')) #Amount to pay as change to customer
    accrual = models.DecimalField(max_digits=15,decimal_places=2, default=Decimal('0.00')) #Amount customer owe us
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_ref
    
    def save(self, *args, **kwargs):
        if not self.id:
            loop_num = 0
            unique = False
            while not unique:
                if loop_num < MAX_TRIES:
                    new_code = ""
                    for i in range(REF_LENGTH):
                        new_code += CHARSET[random.randrange(0,len(CHARSET))]
                    if not Order.objects.filter(order_ref=new_code).exists():
                        self.order_ref = new_code
                        unique = True
                    loop_num+=1
                else:
                    raise ValueError("Can\'t generate a unique code")
            self.date_created =datetime.datetime.now(tz=timezone.utc)
        return super(Order, self).save(*args, **kwargs)



class Payment(models.Model):
    Status = (
        ('Pending','Pending'),
        ('Successful','Successful'),
        ('Declined','Declined'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='order')
    payment_ref = models.CharField(max_length=150, unique=True)
    payment_method = models.CharField(max_length=150)
    amount_paid = models.DecimalField(max_digits=15,decimal_places=2, default=Decimal('0.00'))
    status = models.CharField(max_length=150, choices=Status)
    date_created = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.payment_ref}'         

    def save(self, *args, **kwargs):
        if not self.id:
            loop_num = 0
            unique = False
            while not unique:
                if loop_num < MAX_TRIES:
                    new_code = ""
                    for i in range(REF_LENGTH):
                        new_code += CHARSET[random.randrange(0,len(CHARSET))]
                    if not Payment.objects.filter(payment_ref=new_code).exists():
                        self.payment_ref = new_code
                        unique = True
                    loop_num += 1
                else:
                    raise ValueError("Can\'t generate a unique code")
            self.date_created = datetime.datetime.now(tz=timezone.utc)
        self.modified_date = datetime.datetime.now(tz=timezone.utc)
        return super(Payment, self).save(*args, **kwargs)




