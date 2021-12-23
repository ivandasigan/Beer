from django.shortcuts import render
from rest_framework import viewsets

from beers.models import Beer, Brand
from .serializer import BeerSerializer, BrandSerializer


# Create your views here.

class BeerView(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
