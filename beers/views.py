from os import stat
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.http import response
from django.shortcuts import render
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from beers.models import Beer, Brand
from .serializer import BeerSerializer, BrandSerializer, UserSeriailizer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken import views
# Create your views here.


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSeriailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            token_obj, _ = Token.objects.get_or_create(user=user)
            return Response({'status' : 200, 'payload' : serializer.data, 'token': str(token_obj), 'message': 'your data is saved'})
        return Response({'status' : 403, 'errors': serializer.errors, 'message':'something went wrong'})


class LoginUser(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.get(username=username, password=password)
        user_token = user.auth_token.key
        return Response({"status":200,"token": user_token, "message":"Successfully login"})




class BeerAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            #Get beer object using url param
            name = request.query_params["name"]
            if name != None:
                beer = Beer.objects.get(name=name)
                serializer = BeerSerializer(beer)
        except:
            #return all beer objects
            beers = Beer.objects.all()
            serializer = BeerSerializer(beers, many=True)
  
        return Response(serializer.data)
    #Add new beer object
    def post(self,request):
        serializer = BeerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class BeerPUTAPIView(APIView):

    def put(self, request):
        name = request.query_params["name"]
        beer = Beer.objects.get(name=name)
        serializer = BeerSerializer(beer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 201, "payload": serializer.data, "message":"Successfully Updated"})
        return Response({"status": 401, "payload": serializer.errors, "message":"Something went wroing"})


class BrandAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                brand = Brand.objects.get(id=id)
                serializer = BrandSerializer(brand)
        except:
            brands = Brand.objects.all()
            serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)







class BeerView(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
   
  
        


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
