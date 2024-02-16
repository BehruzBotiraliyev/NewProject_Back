# Generated by Django 5.0.2 on 2024-02-16 08:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="About",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=200, verbose_name="To'liq nomi [title]"
                    ),
                ),
                ("content", models.TextField(null=True, verbose_name="Ma'lumot")),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/", verbose_name="Rasm"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Yaratilgan vaqt"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Tahrirlangan vaqt"
                    ),
                ),
            ],
            options={
                "verbose_name": "Sayt haqida",
                "verbose_name_plural": "Sayt haqida",
                "db_table": "about",
            },
        ),
        migrations.CreateModel(
            name="EmployeePosition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("positions", models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name="Employees",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fullname",
                    models.CharField(
                        max_length=200, verbose_name="Ism va familiyangiz [fullname]"
                    ),
                ),
                (
                    "address",
                    models.CharField(max_length=500, verbose_name="Manzilingiz"),
                ),
                (
                    "image",
                    models.ImageField(
                        null=True, upload_to="images/", verbose_name="Rasm"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Telefon raqamingiz"
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=254, verbose_name="Email manzilingiz"),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, unique=True, verbose_name="UUID"
                    ),
                ),
            ],
            options={
                "verbose_name": "Xodim",
                "verbose_name_plural": "Xodimlar",
                "db_table": "employees",
            },
        ),
        migrations.CreateModel(
            name="Footer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "phone",
                    models.CharField(max_length=200, verbose_name="Telefon raqami"),
                ),
                ("address", models.CharField(max_length=200, verbose_name="Manzil")),
                (
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/", verbose_name="Logo"
                    ),
                ),
                (
                    "facebook",
                    models.URLField(
                        blank=True, null=True, verbose_name="Facebook manzili"
                    ),
                ),
                (
                    "instagram",
                    models.URLField(
                        blank=True, null=True, verbose_name="Instagram manzili"
                    ),
                ),
                (
                    "telegram",
                    models.URLField(
                        blank=True, null=True, verbose_name="Telegram manzili"
                    ),
                ),
                (
                    "youtube",
                    models.URLField(
                        blank=True, null=True, verbose_name="Youtube manzili"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Yaratilgan vaqti"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Tahrirlangan vaqti"
                    ),
                ),
            ],
            options={
                "verbose_name": "Footer",
                "verbose_name_plural": "Footer",
                "db_table": "footer",
            },
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/", verbose_name="Rasm"
                    ),
                ),
            ],
            options={
                "verbose_name": "Rasm",
                "verbose_name_plural": "Rasmlar",
                "db_table": "images",
            },
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=200, verbose_name="Sarlavha [title]"),
                ),
                (
                    "content",
                    models.TextField(null=True, verbose_name="Ma'lumot [content]"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Yaratilgan vaqti"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Tahrirlangan vaqti"
                    ),
                ),
                (
                    "published_at",
                    models.DateField(
                        blank=True, null=True, verbose_name="Chop etilgan vaqt"
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, unique=True, verbose_name="UUID"
                    ),
                ),
            ],
            options={
                "verbose_name": "Yangilik",
                "verbose_name_plural": "Yangiliklar",
                "db_table": "news",
            },
        ),
        migrations.CreateModel(
            name="Services",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "service_type",
                    models.CharField(max_length=200, verbose_name="Xizmat turi"),
                ),
            ],
            options={
                "verbose_name": "Xizmat",
                "verbose_name_plural": "Xizmatlar",
                "db_table": "services",
            },
        ),
    ]