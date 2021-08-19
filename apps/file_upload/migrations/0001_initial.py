# Generated by Django 2.2.14 on 2021-08-19 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FileInfo',
            fields=[
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('file_name', models.TextField()),
                ('file_path', models.TextField()),
                ('grade', models.CharField(max_length=2)),
                ('subject', models.CharField(max_length=25)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
