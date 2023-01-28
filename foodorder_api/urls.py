from django.urls import path
from .views import ListOutlet,DetailOutlet,ListItem,DetailItem

urlpatterns=[
  path('outlet/',ListOutlet.as_view(),name='outlet'),
  path('outlet/<int:pk>/',DetailOutlet.as_view(),name='singleoutlet'),
  path('item/',ListItem.as_view(),name='item'),
  path('item/<int:pk>/',DetailItem.as_view(),name='singleitem'),
]