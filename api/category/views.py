from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Category
# Create your views here.

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
