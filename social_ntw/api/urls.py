from django.urls import include, path
from rest_framework import routers

from .views import PostsViewSet

router_v1 = routers.DefaultRouter()
# router_v1.register('users', UserViewSet, basename='users')
router_v1.register('posts', PostsViewSet, basename='posts')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
