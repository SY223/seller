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
    class Meta:
        model = Category
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
       
