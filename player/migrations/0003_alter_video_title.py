# Generated by Django 5.0.9 on 2025-01-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_folder_video_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
