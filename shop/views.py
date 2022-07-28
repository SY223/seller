from django.http import HttpResponseRedirect
from django.shortcuts import render
from shop.models import Employee, Location, Category, Product
from shop.forms import CustomerForm, EmployeeForm, LocationForm, CategoryForm, ProductForm

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
    return render(request, 'shop/employee.html', context)

def add_category(request):
    if request.method =="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CategoryForm()
    context = {'form':form}
    return render(request, 'shop/category.html', context)

def add_product(request):
    if request.method =="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()
    context = {'form':form}
    return render(request, 'shop/product.html', context)

def add_customer(request):
    if request.method =="POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CustomerForm()
    context = {'form':form}
    return render(request, 'shop/customer.html', context)

