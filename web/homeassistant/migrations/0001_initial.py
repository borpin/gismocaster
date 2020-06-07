# Generated by Django 3.0.6 on 2020-06-07 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ComponentValue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("abbreviation", models.CharField(max_length=32)),
                (
                    "type_value",
                    models.CharField(
                        choices=[
                            ("string", "String"),
                            ("int", "Integer"),
                            ("bool", "Boolean"),
                            ("float", "Float"),
                        ],
                        default="string",
                        max_length=16,
                    ),
                ),
                (
                    "default_value",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Template",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("abbreviation", models.CharField(max_length=32)),
                (
                    "default_value",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("abbreviation", models.CharField(max_length=32)),
                (
                    "specialized_for",
                    models.CharField(blank=True, max_length=64, null=True),
                ),
                (
                    "default_value",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TopicValue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("abbreviation", models.CharField(max_length=32)),
                (
                    "type_value",
                    models.CharField(
                        choices=[
                            ("string", "String"),
                            ("int", "Integer"),
                            ("bool", "Boolean"),
                            ("float", "Float"),
                        ],
                        default="string",
                        max_length=16,
                    ),
                ),
                (
                    "default_value",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "tuya_type_value",
                    models.CharField(
                        choices=[
                            ("string", "String"),
                            ("int", "Integer"),
                            ("bool", "Boolean"),
                            ("float", "Float"),
                        ],
                        default="string",
                        max_length=16,
                    ),
                ),
                ("tuya_value", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "topic",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="homeassistant.Topic",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Component",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                ("technical_name", models.CharField(max_length=32)),
                ("templates", models.ManyToManyField(to="homeassistant.Template")),
                ("topics", models.ManyToManyField(to="homeassistant.Topic")),
                ("values", models.ManyToManyField(to="homeassistant.ComponentValue")),
            ],
        ),
    ]
