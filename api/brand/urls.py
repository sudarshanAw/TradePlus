from rest_framework import routers
from .views import BrandViewset
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'', BrandViewset)

urlpatterns = [
    path('',include(router.urls))
]