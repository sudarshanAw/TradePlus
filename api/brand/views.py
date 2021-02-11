from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BrandSerializer
from .models import Brand

# Create your views here.

class BrandViewset(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
