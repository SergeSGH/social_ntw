from django.contrib import admin

from .models import IsLiked, Posts, User


class UserAdmin(admin.ModelAdmin):

    def posts_count(self, obj):
        return obj.posts.all().count()

    posts_count.short_description = 'Количество постов'

    list_display = (
        'id',
        'first_name',
        'last_name',
        'username',
        'email',
        'location',
        'company',
        'posts_count'
    )
    ordering = ('id',)
    empty_value_display = '--empty--'


class IsLikedInline(admin.StackedInline):
    model = IsLiked
    extra = 0


class PostsAdmin(admin.ModelAdmin):

    def like_count(self, obj):
        return obj.favorited.all().count()

    like_count.short_description = 'Число лайков'

    inlines = (IsLikedInline, )
    list_display = (
        'id',
        'slug',
        'title',
        'author',
        'brief',
        'contents',
    )
    search_fields = (
        'slug',
        'title',
        'author__username',
        'author__email'
    )
    list_filter = ('author__username',)
    empty_value_display = '--empty--'


class IsLikedAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'post'
    )
    search_fields = (
        'user__username',
        'post__brief'
    )
    list_filter = ('user__username',)
    empty_value_display = '--empty--'


admin.site.register(User, UserAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(IsLiked, IsLikedAdmin)
