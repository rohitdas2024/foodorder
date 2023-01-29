from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('foodorder_api.urls')),
    path('auth/auth-token',obtain_auth_token,name='obtain_auth_token')
]
