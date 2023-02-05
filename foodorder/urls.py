from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('foodorder_api.urls')),
    path('auth/auth-token',obtain_auth_token,name='obtain_auth_token'),
    path('auth/login/',TokenObtainPairView.as_view(),name='login'),
    path('auth/refresh-token',TokenRefreshView.as_view(),name='refreshtoken'),
]
