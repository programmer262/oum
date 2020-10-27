# Generated by Django 3.1.1 on 2020-10-13 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corrigé',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('document', models.FileField(upload_to='')),
                ('Corrigé', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('document', models.FileField(upload_to='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('cour', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Exercice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('document', models.FileField(upload_to='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('exercice', models.CharField(max_length=200)),
            ],
        ),
    ]
