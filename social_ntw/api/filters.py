from django_filters import rest_framework

from posts.models import Posts


class PostsFilter(rest_framework.FilterSet):

    is_liked = rest_framework.filters.BooleanFilter(method='liked')

    def liked(self, queryset, field_name, value):
        if value:
            return queryset.filter(is_liked__user=self.request.user)
        return queryset

    author = rest_framework.filters.CharFilter(
        field_name='author__username',
    )

    class Meta:
        model = Posts
        fields = ('author', 'is_liked')
