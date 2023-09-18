from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'feed'

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]