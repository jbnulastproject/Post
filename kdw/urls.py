
from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home,name="home"),
    path('blog/<int:blog_id>/',blog.views.detail,name="detail"),
    path('blog/post/',blog.views.post,name='post'),
    path('blog/create/', blog.views.create, name='create'),
]
