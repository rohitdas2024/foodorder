from django.shortcuts import render
from rest_framework import generics
from .models import Outlet,Item
from .serializers import OutletSerializer,ItemSerializer
from rest_framework import permissions

class ListOutlet(generics.ListCreateAPIView):
  permission_classes=(permissions.IsAuthenticated)
  queryset=Outlet.objects.all()
  serializer_class=OutletSerializer

class DetailOutlet(generics.RetrieveUpdateDestroyAPIView):
  permission_classes=(permissions.IsAuthenticated)
  queryset=Outlet.objects.all()
  serializer_class=OutletSerializer

class ListItem(generics.ListCreateAPIView):
  permission_classes=(permissions.IsAuthenticated)
  queryset=Item.objects.all()
  serializer_class=ItemSerializer

class DetailItem(generics.RetrieveUpdateDestroyAPIView):
  permission_classes=(permissions.IsAuthenticated)
  queryset=Item.objects.all()
  serializer_class=ItemSerializer
