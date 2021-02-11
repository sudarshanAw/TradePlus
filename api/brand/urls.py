from rest_framework import routers
from .views import BrandViewset
from django.urls import path,include

router = routers.DefaultRouterRouter()
router.register(r'', BrandViewset)

urlpatterns = [
    path('',include(router.urls))
]