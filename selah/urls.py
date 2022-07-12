
from django.contrib import admin
from django.urls import path,include
from shop import views as shopapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shopapp_views.index, name='index'),
]
