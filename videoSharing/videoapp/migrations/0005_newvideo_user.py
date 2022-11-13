# Generated by Django 4.1.2 on 2022-11-08 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videoapp', '0004_remove_newvideo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='newvideo',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
