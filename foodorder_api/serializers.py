from rest_framework import serializers
from .models import Outlet,Item,Cart

class OutletSerializer(serializers.ModelSerializer):
  class Meta:
    fields=('id','name')
    model=Outlet

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    fields=('id','name','category','price','stock')
    model=Item

class CartSerializer(serializers.ModelSerializer):
  items=ItemSerializer(read_only=True,Many=True)
  class Meta:
    fields=('cart_id','items')
    model=Cart


