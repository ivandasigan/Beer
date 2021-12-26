
from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import BeerView, BrandView
router = DefaultRouter()
router.register('beers', BeerView)
router.register('brand', BrandView)

urlpatterns = [
    path('', include(router.urls))
]