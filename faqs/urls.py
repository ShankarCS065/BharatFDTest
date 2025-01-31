from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet

# Create a router and register our viewset with it
router = DefaultRouter()
router.register(r'faqs', FAQViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include DRF router URLs
]
