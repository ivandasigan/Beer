
from rest_framework import fields, serializers
from .models import Beer, Brand

class BeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beer
        fields = ('id','name','size','srp')

class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ('id','name','beers')

