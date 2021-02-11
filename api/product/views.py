from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializers

# Create your views here.
class ProductViewsets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

