from django.db import models
from api.brand.models import Brand
from api.category.models import Category
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Product(models.Model):

    EXTRA_LARGE = 'XL'
    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'
    EXTRA_SMALL = 'XS'

    SIZES = [
        (EXTRA_LARGE, 'ExtraLarge'),
        (LARGE, 'Large'),
        (MEDIUM, 'Medium'),
        (SMALL, 'Small'),
        (EXTRA_SMALL, 'ExtraSmall'),
    ]

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.IntegerField()
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=3,choices=SIZES,default=None)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self):
        return self.name