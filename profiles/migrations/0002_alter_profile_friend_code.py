# Generated by Django 3.2.25 on 2024-12-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friend_code',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
