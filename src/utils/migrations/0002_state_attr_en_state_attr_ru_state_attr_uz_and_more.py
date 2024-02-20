# Generated by Django 5.0.2 on 2024-02-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("utils", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="state",
            name="attr_en",
            field=models.CharField(
                max_length=200, null=True, verbose_name="Qisqa nomi [attr]"
            ),
        ),
        migrations.AddField(
            model_name="state",
            name="attr_ru",
            field=models.CharField(
                max_length=200, null=True, verbose_name="Qisqa nomi [attr]"
            ),
        ),
        migrations.AddField(
            model_name="state",
            name="attr_uz",
            field=models.CharField(
                max_length=200, null=True, verbose_name="Qisqa nomi [attr]"
            ),
        ),
        migrations.AddField(
            model_name="state",
            name="title_en",
            field=models.CharField(
                max_length=200, null=True, verbose_name="To'liq nomi [title]"
            ),
        ),
        migrations.AddField(
            model_name="state",
            name="title_ru",
            field=models.CharField(
                max_length=200, null=True, verbose_name="To'liq nomi [title]"
            ),
        ),
        migrations.AddField(
            model_name="state",
            name="title_uz",
            field=models.CharField(
                max_length=200, null=True, verbose_name="To'liq nomi [title]"
            ),
        ),
    ]
