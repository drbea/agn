# Generated by Django 5.1.6 on 2025-03-09 14:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, default='img/default_article.png', null=True, upload_to='')),
                ('introduction', models.TextField(blank=True, null=True)),
                ('subtitle_1', models.CharField(blank=True, max_length=250, null=True)),
                ('contenu_1', models.TextField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('subtitle_2', models.CharField(blank=True, max_length=250, null=True)),
                ('contenu_2', models.TextField(blank=True, null=True)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('subtitle_3', models.CharField(blank=True, max_length=250, null=True)),
                ('contenu_3', models.TextField(blank=True, null=True)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('subtitle_4', models.CharField(blank=True, max_length=250, null=True)),
                ('contenu_4', models.TextField(blank=True, null=True)),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('topics', models.ManyToManyField(blank=True, to='blog.topic')),
            ],
        ),
    ]
