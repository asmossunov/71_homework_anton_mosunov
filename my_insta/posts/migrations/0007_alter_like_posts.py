# Generated by Django 4.1.1 on 2022-11-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='posts',
            field=models.ManyToManyField(related_name='posts_likes', to='posts.post', verbose_name='Публикации с лайком'),
        ),
    ]