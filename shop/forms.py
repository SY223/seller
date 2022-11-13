from django import forms
from shop.models import Employee, Location, Category, Customer, Product, Order, Payment
import random


class LocationForm(forms.Form):
    name = forms.CharField()
    street = forms.CharField()
    city = forms.CharField()
    zipcode = forms.CharField()



class EmployeeForm(forms.Form):
    first_name = forms.CharField(required=True, help_text='Enter your given name')
    last_name = forms.CharField(required=True,help_text='Enter your surname name')
    email = forms.EmailField(required=True,help_text='Enter email')
    username = forms.CharField(required=True,help_text='Enter your username')
    employee_phone = forms.CharField(required=True, widget=forms.NumberInput)
    store_location = forms.ModelChoiceField(required=True,widget=forms.Select,queryset=Location.objects.all())
    
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

    def clean_username(self):
        new_username = self.cleaned_data['username']
        confam_username = Employee.objects.filter(username=new_username)
        if confam_username.exists():
            raise forms.ValidationError("Username already exists")
        return confam_username


  
            
class CategoryForm(forms.Form):
    category_name = forms.CharField(required=True,widget=forms.TextInput)
    description = forms.CharField(required=True,widget=forms.Textarea) 
    cart_image = forms.ImageField(required=False)



class ProductForm(forms.Form):
    item = forms.CharField(required=True,widget=forms.TextInput)
    description = forms.CharField(required=True, widget=forms.Textarea)
    price = forms.CharField(required=True, widget=forms.NumberInput)
    image = forms.ImageField(required=False)
    stock = forms.CharField(widget=forms.NumberInput)



class CustomerForm(forms.Form):
    customer_name = forms.CharField(widget=forms.TextInput)
    customer_email = forms.CharField(widget=forms.EmailInput)
    customer_phone = forms.CharField(widget=forms.NumberInput)
    


       
