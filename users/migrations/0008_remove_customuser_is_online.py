# Generated by Django 3.1.14 on 2022-02-24 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_customuser_is_online'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_online',
        ),
    ]
