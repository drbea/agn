# Generated by Django 5.1.6 on 2025-03-09 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='category',
        ),
        migrations.AddField(
            model_name='topic',
            name='category',
            field=models.ManyToManyField(to='blog.category'),
        ),
    ]
