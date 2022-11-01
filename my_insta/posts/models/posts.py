from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    description = models.CharField(verbose_name='Описание', null=True, blank=True, max_length=200)
    image = models.ImageField(verbose_name='Фото', null=False, blank=False, upload_to='uploads')
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='posts', null=False, blank=False,
                               on_delete=models.CASCADE)
    comment_count = models.IntegerField(
        verbose_name='Количество комментариев',
        default=0,
    )
    like_count = models.IntegerField(
        verbose_name='Количество лайков',
        default=0,
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False, null=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )
