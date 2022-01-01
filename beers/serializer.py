
from rest_framework import serializers
from .models import Beer, Brand

from django.contrib.auth.models import User

class UserSeriailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'], password = validated_data['password'])
        user.save()
        return user

class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = ['id','name','image','size','srp', 'stock','ratings']
    
class BrandSerializer(serializers.ModelSerializer):
    beers = BeerSerializer(many=True, read_only=False)

    class Meta:
        model = Brand
        fields = ['id','name', 'beers']

    def create(self, validated_data):
        beers_data = validated_data.pop('beers')
        brand = Brand.objects.create(**validated_data)
        for beer_data in beers_data:
            Beer.objects.create(brand=brand, **beer_data)
        return brand

