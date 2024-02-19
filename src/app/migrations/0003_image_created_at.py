# Generated by Django 5.0.2 on 2024-02-19 10:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_remove_image_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Yaratilgan vaqti",
            ),
            preserve_default=False,
        ),
    ]
