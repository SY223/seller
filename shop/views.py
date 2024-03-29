from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from shop.models import Employee, Location, Category, Product
from shop.forms import CustomerForm, EmployeeForm, LocationForm, CategoryForm, ProductForm



def index(request):
    return render(request, 'shop/index.html',)

def add_store(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            street = form.cleaned_data['street']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            new_loc = Location.objects.create(name=name, street=street,city=city,zipcode=zipcode)
            new_loc.save()
            return redirect('location')
    else:
        form = LocationForm()
    context = {'form':form}
    return render(request, 'shop/location.html', context)
            

def new_employee(request):
    if request.method =="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            employee_phone = form.cleaned_data['employee_phone']
            position = form.cleaned_data['position']
            store_location = form.cleaned_data['store_location']
            new_staff = Employee.objects.create(first_name=first_name, last_name=last_name, email=email, username=username, employee_phone=employee_phone,\
                position=position, store_location=store_location)
            new_staff.save()
            return redirect('staff')  
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


def location(request):
    store_list = Location.objects.all()
    context = {'store_list': store_list}
    return render(request, 'shop/location_list.html', context)

def location_detail(request, pk):
    store = Location.objects.get(id=pk)
    context = {'store': store}
    return render(request, 'shop/location_detail.html', context)


def staff(request):
    employee_list = Employee.objects.all()
    context = {'employee_list': employee_list}
    return render(request,'shop/employee_list.html', context)

def staff_detail(request, pk):
    employee = Employee.objects.get(id=pk)
    context = {'employee': employee}
    return render(request, 'shop/employee_detail.html', context)