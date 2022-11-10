from django import forms
from shop.models import Employee, Location, Category, Customer, Product, Order, Payment
import random


class LocationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter store name',\
        'class': 'form-control',}))
    street = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter street address',\
        'class': 'form-control',}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter store city',\
        'class': 'form-control',}))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter store zipcode',\
        'class': 'form-control',}))
    class Meta:
        model = Location
        fields = ['name', 'street', 'city', 'zipcode',]
    
    def __str__(self):
        return self.name


class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter firstname',\
        'class': 'form-control',}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter lastname',\
        'class': 'form-control',}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter email',\
        'class': 'form-control',}))

    employee_phone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder':\
        'Enter employee telephone','class': 'form-control',}))
    store_location = forms.ModelChoiceField(widget=forms.Select,queryset=Location.objects.all())
    class Meta:
        model = Employee
        fields = ['first_name','last_name', 'email','username','employee_phone','store_location']
    

    def clean_email(self):
        email = self.cleaned_data['email']
        
        with open("shop/disposable_email_list.txt", 'r') as f:
            blacklist = f.read().splitlines()

        for disposable_email in blacklist:
            if disposable_email in email:
                raise forms.ValidationError("You cannot signup with a disposable email.")
            elif Employee.objects.filter(email=email).exists():
                raise forms.ValidationError("Email already exists, login via staff portal.")
        return email

  

    # def clean_username(self):
    #     username = self.cleaned_data["username"]    
    #     confam_username = Employee.objects.get(username=username).username
    #     if confam_username.exists():
    #         try:
    #             username +=  str(random.randrange(0,9,1))
    #             username.save()
    #         except username is None:
    #             raise forms.ValidationError("Email address cannot be blank")
    #     return username
 




            
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
    customer_phone = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder':'Enter customer telephone',
        'class': 'form-control',
    }))
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_email', 'customer_phone',] 


       
