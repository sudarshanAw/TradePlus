from rest_framework import routers

from django.urls import path,include
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path("", home, name = 'api.home'),
    path("brand/", include('api.brand.urls')),
    path("category/", include('api.category.urls')),
    path("product/", include('api.product.urls')),
]
