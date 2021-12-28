
from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from beers.models import Beer
from .views import BeerView, BrandView, BeerAPIView, BrandAPIView, RegisterUser, BeerPUTAPIView, LoginUser

from rest_framework.authtoken import views

router = DefaultRouter()
router.register('beers', BeerView, basename='beers')
router.register('brand', BrandView, basename='brand')

urlpatterns = [
    #path('', include(router.urls)),
    path('beers/', BeerAPIView.as_view()),
    path('brand/', BrandAPIView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('register/', RegisterUser.as_view()),
    path('putbeer/', BeerPUTAPIView.as_view()),
    path('login/', LoginUser.as_view())
]