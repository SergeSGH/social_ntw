from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Posts, IsLiked

User = get_user_model()


# class UserSerializer(serializers.ModelSerializer):

#    class Meta:
#        model = User
#        fields = ('id', 'first_name', 'last_name', 'username', 'email')


class PostsSerializerShort(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id', 'slug', 'title', 'author',
            'brief', 'contents'
        )
        model = Posts


class PostsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all()
    )
    is_liked = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'id', 'slug', 'pub_date', 'title', 'author',
            'brief', 'contents', 'is_liked'
        )
        model = Posts

    def get_is_liked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return IsLiked.objects.filter(
                user=user, post=obj
            ).exists()
        return False
