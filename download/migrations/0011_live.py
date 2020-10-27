# Generated by Django 3.1.1 on 2020-10-18 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('download', '0010_auto_20201018_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Live',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lien', models.TextField()),
                ('matiére', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=200)),
                ('heure', models.CharField(max_length=200)),
                ('professeur', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
