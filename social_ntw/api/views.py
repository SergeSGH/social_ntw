from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostsFilter

from posts.models import IsLiked, Posts
from .pagination import PostsPagination
from .permissions import IsAuthor, ReadOnly
from .serializers import PostsSerializer
User = get_user_model()


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
        print(self.kwargs)
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
