from rest_framework import routers
from .views import ProductViewsets
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'', ProductViewsets)

urlpatterns = [
    path('',include(router.urls))
]