from django.db import models
from django.contrib.auth.models import User

class Outlet(models.Model):
  name=models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Item(models.Model):
  name=models.CharField(max_length=100)
  category=models.ForeignKey(Outlet,related_name='items',on_delete=models.CASCADE)
  price=models.IntegerField()
  stock=models.IntegerField()

  class Meta:
    ordering=['-price']

  def __str__(self):
    return '{}, {}'.format(self.name,self.category)

class Cart(models.Model):
  cart_id=models.OneToOneField(User,on_delete=models.CASCADE)
  items=models.ManyToManyField(Item)

  class Meta:
    ordering=['cart_id']

  def __str__(self):
    return '{}'.format(self.cart_id)

