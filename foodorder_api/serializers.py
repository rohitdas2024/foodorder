from rest_framework import serializers
from .models import Outlet,Item

class OutletSerializer(serializers.ModelSerializer):
  class Meta:
    fields=('id','name')
    model=Outlet

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    fields=('id','name','category','price','stock')
    model=Item


