
from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from beers.models import Beer
from .views import BeerView, BrandView, BeerAPIView, BrandAPIView, RegisterUser, BeerPUTAPIView, LoginUser, FilterBeerListView

from rest_framework.authtoken import views

router = DefaultRouter()
router.register('beersss', BeerView, basename='beers')
router.register('brandss', BrandView, basename='brand')



urlpatterns = [
    path('', include(router.urls)),

    #Beer api view
    path('beers/', BeerAPIView.as_view()),
    path('putbeer/', BeerPUTAPIView.as_view()),

    #Brand api view
    path('brand/', BrandAPIView.as_view()),
 
    #Filter Beer
    path('findbeers/', FilterBeerListView.as_view()),

    #User auth
    path('register/', RegisterUser.as_view()),
    path('login/', LoginUser.as_view()),

    path('api-token-auth/', views.obtain_auth_token),

]