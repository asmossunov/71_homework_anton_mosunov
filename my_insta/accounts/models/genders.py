from django.db import models


class Gender(models.Model):
    gender_name = models.CharField(
        verbose_name='Пол',
        max_length=100,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    def __str__(self):
        return f'{self.gender_name}'
