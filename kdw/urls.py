from django.contrib import admin
from django.urls import path, include
from blog import urls
from rest_framework import urls
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
