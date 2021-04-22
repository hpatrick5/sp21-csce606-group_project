# Generated by Django 3.2 on 2021-04-22 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_auto_20210422_0236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='user_profile',
            options={'ordering': ['last_name']},
        ),
        migrations.AddField(
            model_name='savedfile',
            name='save_file',
            field=models.FileField(default=None, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
