from django import forms
from shop.models import Employee, Location, Category, Customer, Product, Order, Payment
from django.forms.models import ModelChoiceField


class LocationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter store name',
        'class': 'form-control',
    }))
    street = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter street address',
        'class': 'form-control',
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter store city',
        'class': 'form-control',
    }))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter store zipcode',
        'class': 'form-control',
    }))
    class Meta:
        model = Location
        fields = ['name', 'street', 'city', 'zipcode',]


class EmployeeForm(forms.ModelForm):
    store_location = forms.ModelChoiceField(queryset=Location.objects.all(),initial=0)

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter firstname',
        'class': 'form-control',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter lastname',
        'class': 'form-control',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter username',
        'class': 'form-control',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Enter email',
        'class': 'form-control',
    }))
    employee_nu = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder':'Enter employee telephone',
        'class': 'form-control',
    }))
    class Meta:
        model = Employee
        fields = ['store_location','first_name','last_name', 'username', 'email', 'employee_nu',]



class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter category name',
        'class': 'form-control',
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'Enter category description',
        'class': 'form-control',
    })) 
    class Meta:
        model = Category
        fields = ['category_name', 'description', 'cart_image',]


class ProductForm(forms.ModelForm):
    item = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter product name',
        'class': 'form-control',
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'Enter product description',
        'class': 'form-control',
    })) 
    stock = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder':'Enter available stock',
        'class': 'form-control',
    }))
    class Meta:
        model = Product
        fields = ['item','description','price','image','stock']


class CustomerForm(forms.ModelForm):
    customer_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter customer full name',
        'class': 'form-control',
    }))
    customer_email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Enter customer email address',
        'class': 'form-control',
    }))
    customer_nu = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder':'Enter customer telephone',
        'class': 'form-control',
    }))
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_email', 'customer_nu',] 


       
