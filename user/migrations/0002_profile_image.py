# Generated by Django 5.0.1 on 2024-12-27 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar.jpg', upload_to='ProfileImage/'),
        ),
    ]
