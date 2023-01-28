from django.shortcuts import render
from rest_framework import generics
from .models import Outlet,Item
from .serializers import OutletSerializer,ItemSerializer

class ListOutlet(generics.ListCreateAPIView):
  queryset=Outlet.objects.all()
  serializer_class=OutletSerializer

class DetailOutlet(generics.RetrieveUpdateDestroyAPIView):
  queryset=Outlet.objects.all()
  serializer_class=OutletSerializer

class ListItem(generics.ListCreateAPIView):
  queryset=Item.objects.all()
  serializer_class=ItemSerializer

class DetailItem(generics.RetrieveUpdateDestroyAPIView):
  queryset=Item.objects.all()
  serializer_class=ItemSerializer
