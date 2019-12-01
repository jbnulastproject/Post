from rest_framework.routers import DefaultRouter
from django.urls import include, path
from blog import views


router = DefaultRouter()
router.register('essay', views.PostViewSet)
#일단 essay
urlpatterns = [
    path('', include(router.urls))
]