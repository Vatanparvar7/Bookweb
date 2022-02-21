# Generated by Django 3.1.14 on 2022-02-08 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_messagefriendmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaqt', models.DateTimeField(auto_now_add=True)),
                ('friend_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Jasur', to=settings.AUTH_USER_MODEL)),
                ('my_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Shexroz', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
