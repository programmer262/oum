# Generated by Django 3.1.1 on 2020-10-18 18:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('download', '0012_auto_20201018_1901'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Class',
            new_name='Classe',
        ),
    ]
