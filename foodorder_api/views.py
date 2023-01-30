from django.shortcuts import render
from rest_framework import generics
from .models import Outlet,Item,Cart
from .serializers import OutletSerializer,ItemSerializer,CartSerializer,UserSerializer,RegistrationSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

class RegistrationAPIView(generics.GenericAPIView):
  serializer_class = RegistrationSerializer
  def post(self, request):
    serializer = self.get_serializer(data = request.data)
    # serializer.is_valid(raise_exception = True)
    # serializer.save()
    if(serializer.is_valid()):
      serializer.save()
      return Response({
        "Message": "User created successfully",
        "User": serializer.data}, status=status.HTTP_201_CREATED
    ) 
    return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)

class ListOutlet(generics.ListCreateAPIView):
  permission_classes=(permissions.IsAuthenticated,)
  queryset=Outlet.objects.all()
  serializer_class=OutletSerializer

class DetailOutlet(generics.RetrieveUpdateDestroyAPIView):
  permission_classes=(permissions.IsAuthenticated,)
  queryset=Outlet.objects.all()
  serializer_class=OutletSerializer

class ListItem(generics.ListCreateAPIView):
  permission_classes=(permissions.IsAuthenticated,)
  queryset=Item.objects.all()
  serializer_class=ItemSerializer

class DetailItem(generics.RetrieveUpdateDestroyAPIView):
  permission_classes=(permissions.IsAuthenticated,)
  queryset=Item.objects.all()
  serializer_class=ItemSerializer

class ListUser(generics.ListCreateAPIView):
  permission_classes=(permissions.IsAuthenticated,)
  queryset=User.objects.all()
  serializer_class=UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
  permission_classes=(permissions.IsAuthenticated,)
  queryset=User.objects.all()
  serializer_class=UserSerializer

class ListCart(generics.ListCreateAPIView):
  permission_classes=(permissions.IsAuthenticated,)
  queryset=Cart.objects.all()
  serializer_class=CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
  permission_classes=(permissions.IsAuthenticated,)
  queryset=Cart.objects.all()
  serializer_class=CartSerializer
