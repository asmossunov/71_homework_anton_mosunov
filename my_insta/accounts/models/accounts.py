from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import TextChoices

from accounts.managers import UserManager


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        blank=False)

    avatar = models.ImageField(
        null=False,
        blank=False,
        upload_to='avatars',
        verbose_name='Аватар',
        default='uploads/default_avatar/default-user.png'
    )
    birthday = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    liked_posts = models.ManyToManyField(verbose_name='Понравившиеся публикации', to='posts.Post',
                                         related_name='user_likes')
    subscriptions = models.ManyToManyField(verbose_name='Подписки', to='accounts.Account', related_name='subscribers')
    commented_posts = models.ManyToManyField(verbose_name='Прокомментированные публикации', to='posts.Post',
                                             related_name='user_comments')
    about_user = models.TextField(
        verbose_name='Информация о пользователе',
        max_length=5000,
        null=True,
        blank=True
    )
    phone = PhoneNumberField(
        unique=True,
        null=True,
        blank=True
    )
    gender = models.ForeignKey(
        to='accounts.Gender',
        verbose_name='Пол',
        related_name='accounts',
        null=True,
        blank=True,
        on_delete=models.CASCADE
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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
