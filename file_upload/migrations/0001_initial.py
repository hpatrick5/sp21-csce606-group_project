# Generated by Django 2.2.14 on 2021-04-28 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveIntegerField()),
                ('upload_file', models.FileField(blank=True, default=None, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='file_name')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
