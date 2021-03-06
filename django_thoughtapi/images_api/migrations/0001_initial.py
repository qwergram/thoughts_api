# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 00:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import images_api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('published', models.CharField(choices=[('UNLISTED', 'Unlisted'), ('PUBLIC', 'Public')], max_length=255)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1024)),
                ('published', models.CharField(choices=[('UNLISTED', 'Unlisted'), ('PUBLIC', 'Public')], default='PUBLIC', max_length=255)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to=images_api.models.image_path)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='images_api.Photo'),
        ),
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(related_name='starred_in', to='images_api.Photo'),
        ),
    ]
