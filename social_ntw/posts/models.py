from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Posts(models.Model):
    slug = models.SlugField(
        'Заголовок транслитом',
        help_text='Заголовок транслитом',
        unique=True
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    title = models.CharField(
        'Заголовок',
        help_text='Заголовок',
        max_length=200,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
        help_text='Автор'
    )
    brief = models.CharField(
        'Краткое содержание',
        help_text='Краткое содержание',
        max_length=250,
    )
    contents = models.TextField(
        'Содержание',
        help_text='Содержание'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.slug


class IsLiked(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='liked_posts',
        verbose_name='Пользователь',
        help_text='Пользователь'
    )
    post = models.ForeignKey(
        Posts,
        on_delete=models.CASCADE,
        related_name='is_liked',
        verbose_name='Избранная новость',
        help_text='Избранная новость'
    )

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
