# Generated by Django 3.1.14 on 2022-02-08 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_following'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Following',
            new_name='FriendModel',
        ),
    ]
