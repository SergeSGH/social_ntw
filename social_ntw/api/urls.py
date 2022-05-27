from django.urls import include, path
from rest_framework import routers

from .views import PostsViewSet, UserViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostsViewSet, basename='posts')
router_v1.register('auth/users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/', include('djoser.urls.jwt')),
]
