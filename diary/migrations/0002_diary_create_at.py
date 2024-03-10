# Generated by Django 5.0.2 on 2024-03-07 07:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("diary", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="diary",
            name="create_at",
            field=models.DateField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="作成日時",
            ),
            preserve_default=False,
        ),
    ]
