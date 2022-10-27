from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True)

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars',
        verbose_name='Аватар'
    )
    birthday = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
