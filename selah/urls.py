
from django.contrib import admin
from django.urls import path,include
from shop import views as shopapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shopapp_views.index, name='index'),
    path('add/store', shopapp_views.add_store, name='add-store'),
    path('add/employee', shopapp_views.add_employee, name='add-employee'),
    path('add/category', shopapp_views.add_category, name='add-category'),
    path('add/new/product', shopapp_views.add_product, name='add-product'),
    path('add/customer', shopapp_views.add_customer, name='add-customer'),
]
