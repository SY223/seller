from django.http import HttpResponseRedirect
from django.shortcuts import render
from shop.models import Employee, Location, Category, Product, Order, Payment
from shop.forms import EmployeeForm, LocationForm, CategoryForm, ProductForm, OrderForm, PaymentForm

def index(request):
    location = Location.objects.get(name='JAMDOOR AYOBO')
    context = {
        'location':location,
    }
    return render(request, 'shop/index.html', context)

def add_store(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = LocationForm()
    context = {'form':form}
    return render(request, 'shop/add_location.html', context)
            

def add_employee(request):
    if request.method =="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = EmployeeForm()
    context = {'form':form}
    return render(request, 'shop/add_employee.html', context)

