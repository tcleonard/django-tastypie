# Generated by Django 2.2.1 on 2019-05-28 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tastypie.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SlugBasedNote',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('content', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=tastypie.utils.timezone.now)),
                ('updated', models.DateTimeField(default=tastypie.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnnotatedNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annotations', models.TextField()),
                ('note', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='annotated', to='basic.Note')),
            ],
        ),
    ]
