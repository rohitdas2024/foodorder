from rest_framework import serializers
from .models import Outlet,Item,Cart
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):

  email = serializers.EmailField(max_length=50, min_length=6)
  username = serializers.CharField(max_length=50, min_length=6)
  password = serializers.CharField(max_length=50, write_only=True)

  class Meta:
      model = User
      fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')

  def validate(self, args):
      email = args.get('email', None)
      username = args.get('username', None)
      if User.objects.filter(email=email).exists():
        raise serializers.ValidationError({'email': ('email already exists!')})
      if User.objects.filter(username=username).exists():
        raise serializers.ValidationError({'username': ('username already exists!')})
      return super().validate(args)
  

  def create(self, validated_data):
    return User.objects.create_user(**validated_data)

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


