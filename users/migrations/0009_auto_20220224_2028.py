# Generated by Django 3.1.14 on 2022-02-24 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_customuser_is_online'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='userimage/userimage.jpg', null=True, upload_to='userimage/'),
        ),
    ]
