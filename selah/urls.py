
from django.contrib import admin
from django.urls import path,include
from shop import views as shopapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shopapp_views.index, name='index'),
    path('staff', shopapp_views.staff, name='staff'),
    path('staff/<int:pk>/', shopapp_views.staff_detail, name='staff-detail'),
    path('location/', shopapp_views.location, name='location'),
    path('location/<int:pk>', shopapp_views.location_detail, name='location-detail'),
    path('add/store', shopapp_views.add_store, name='add-store'),
    path('new/employee', shopapp_views.new_employee, name='new-employee'),
    path('add/category', shopapp_views.add_category, name='add-category'),
    path('add/new/product', shopapp_views.add_product, name='add-product'),
    path('add/customer', shopapp_views.add_customer, name='add-customer'),
]
