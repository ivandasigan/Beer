
from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from beers.models import Beer
from .views import BeerView, BrandView, BeerAPIView, BrandAPIView
router = DefaultRouter()
router.register('beers', BeerView, basename='beers')
router.register('brand', BrandView, basename='brand')

urlpatterns = [
    path('', include(router.urls)),
    path('beers/', BeerAPIView.as_view()),
    path('brand/', BrandAPIView.as_view())

]