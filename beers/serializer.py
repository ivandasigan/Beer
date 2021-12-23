
from rest_framework import fields, serializers
from .models import Beer, Brand

class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = ['id', 'name','size','srp']
    
class BrandSerializer(serializers.ModelSerializer):
    beers = BeerSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = ['name', 'beers']

    def create(self, validated_data):
        beers_data = validated_data.pop('beers')
        brand = Brand.objects.create(**validated_data)
        for beer_data in beers_data:
            Beer.objects.create(brand=brand, **beer_data)
        return brand