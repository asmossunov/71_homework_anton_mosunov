# Generated by Django 4.1.1 on 2022-11-01 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_gender_account_about_user_account_changed_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default='default_avatar/default-user.png', upload_to='avatars', verbose_name='Аватар'),
        ),
    ]
