from django.urls import path
from .views import ListOutlet,DetailOutlet,ListItem,DetailItem,ListUser,DetailUser,ListCart,DetailCart

urlpatterns=[
  path('outlet/',ListOutlet.as_view(),name='outlet'),
  path('outlet/<int:pk>/',DetailOutlet.as_view(),name='singleoutlet'),
  
  path('item/',ListItem.as_view(),name='item'),
  path('item/<int:pk>/',DetailItem.as_view(),name='singleitem'),

  path('users/',ListUser.as_view(), name='users'),
  path('users/<int:pk>/',DetailUser.as_view(),name='singleuser'),

  path('carts/',ListCart.as_view(),name='allcarts'),
  path('carts/<int:pk>',DetailCart.as_view(),name='cartdetail'),

]