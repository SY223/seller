from django import forms
from shop.models import *
import random


CHARSET = 'abcdefghjkmnpqrstvwxyzABCDEFGHJKMNPQRSTVWXYZ'



class LocationForm(forms.Form):
    name = forms.CharField()
    street = forms.CharField()
    city = forms.CharField()
    zipcode = forms.CharField()

    def clean_name(self):
        name = self.cleaned_data['name']
        special_characters = '$@#&'
        for char in special_characters:
            if char in name:
                raise forms.ValidationError("Name cannot contain special characters.")
        return name
    def clean_street(self):
        street = self.cleaned_data['street']
        special_characters = '$@#&'
        for char in special_characters:
            if char in street:
                raise forms.ValidationError("Street cannot contain special characters.")
        return street
    def clean_city(self):
        city = self.cleaned_data['city']
        special_characters = '$@#&'
        for char in special_characters:
            if char in city:
                raise forms.ValidationError("City cannot contain special characters.")
        return city
    def clean_zipcode(self):
        zipcode = self.cleaned_data['zipcode']
        for letas in CHARSET:
            if letas in zipcode:
                raise forms.ValidationError("Zip must not contain alphabets.")
        return zipcode

        



class EmployeeForm(forms.Form):
    first_name = forms.CharField(required=True, help_text='Enter your given name')
    last_name = forms.CharField(required=True,help_text='Enter your surname name')
    email = forms.EmailField(required=True,help_text='Enter email')
    username = forms.CharField(required=True,help_text='Enter your username')
    employee_phone = forms.CharField(required=True, widget=forms.NumberInput)
    position = forms.ModelChoiceField(required=True,widget=forms.Select,queryset=Role.objects.all())
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
    


       
