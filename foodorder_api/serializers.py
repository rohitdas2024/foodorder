from rest_framework import serializers
from .models import Outlet,Item,Cart
from django.contrib.auth.models import User

class OutletSerializer(serializers.ModelSerializer):
  class Meta:
    fields=('id','name')
    model=Outlet

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    fields=('id','name','category','price','stock')
    model=Item

class UserSerializer(serializers.ModelSerializer):
    items=serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())
    class Meta:
        model = User
        fields = ('id','username','email','items')

class CartUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')

class CartSerializer(serializers.ModelSerializer):
  cart_id=CartUserSerializer(read_only=True,many=False)
  items=ItemSerializer(read_only=True,many=True)
  class Meta:
    fields=('cart_id','items')
    model=Cart


