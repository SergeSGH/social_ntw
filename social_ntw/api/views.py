import os

import clearbit
import requests
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from dotenv import load_dotenv
from rest_framework import filters, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from posts.models import IsLiked, Posts
from .filters import PostsFilter
from .pagination import PostsPagination, UsersPagination
from .permissions import AllowUserChange, AllowUserCreate, IsAuthor, ReadOnly
from .serializers import PostsSerializer, UserSerializer

User = get_user_model()


def check_email(email, api_key):
    url = ('https://api.hunter.io/v2/email-verifier?'
           f'email={email}&api_key={api_key}')
    requests.get(url, timeout=0.5)
    domain = email.split('@')[1]
    if not domain == 'gmail.com':
        return False
    return True


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        AllowUserCreate | AllowUserChange | ReadOnly,
    )
    pagination_class = UsersPagination
    lookup_field = 'username'
    filter_backends = (
        filters.SearchFilter,
    )
    search_fields = ('username',)

    def perform_create(self, serializer):
        load_dotenv()
        clearbit.key = os.getenv('CLEARBIT_KEY')
        data = serializer.validated_data
        email = data['email']
        try:
            response = clearbit.Enrichment.find(email=email, stream=True)
        finally:
            pass
        if response:
            if 'location' not in data:
                if response['person'] is not None:
                    if response['person']['location'] is not None:
                        location = response['person']['location']
                        data['location'] = location
            if 'company' not in data:
                if response['company'] is not None:
                    if response['company']['name'] is not None:
                        company = response['company']['name']
                        data['company'] = company
        api_key = os.getenv('API_KEY')
        if check_email(email, api_key):
            serializer.save(**data)
        else:
            raise serializers.ValidationError(
                'e-mail некорректный!'
            )


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostsSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        ReadOnly | IsAuthor,
    )
    queryset = Posts.objects.all()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = PostsFilter
    ordering_fields = ('pub_date', )
    pagination_class = PostsPagination

    @action(
        detail=True,
        methods=('post', ),
        url_path='like',
        permission_classes=(IsAuthenticated,),
    )
    def like(self, request, **kwargs):
        post = get_object_or_404(Posts, id=self.kwargs.get('pk'))
        if IsLiked.objects.filter(
            post=post, user=self.request.user
        ).exists():
            return Response(
                'Лайк уже есть!',
                status=status.HTTP_400_BAD_REQUEST
            )
        IsLiked.objects.create(
            post=post, user=self.request.user
        )
        return Response(
            'Поставили лайк!',
            status=status.HTTP_201_CREATED
        )

    @action(
        detail=True,
        methods=('post', ),
        url_path='unlike',
        permission_classes=(IsAuthenticated,),
    )
    def unlike(self, request, **kwargs):
        post = get_object_or_404(Posts, id=self.kwargs.get('pk'))
        if not IsLiked.objects.filter(
            post=post, user=self.request.user
        ).exists():
            return Response(
                'Лайка нет!',
                status=status.HTTP_400_BAD_REQUEST
            )
        like = IsLiked.objects.filter(
            post=post, user=self.request.user
        )
        like.delete()
        # статус 200 вместо 204 чтобы вывести сообщение
        return Response(
            'Убрали лайк!',
            status=status.HTTP_200_OK
        )
