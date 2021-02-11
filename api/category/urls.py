from rest_framework import routers
from .views import CategoryViewset
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'', CategoryViewset)

urlpatterns = [
    path('',include(router.urls))
]