# Generated by Django 4.1.2 on 2022-11-08 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoapp', '0003_newvideo_user_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newvideo',
            name='user',
        ),
    ]
