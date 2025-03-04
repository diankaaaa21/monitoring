# Generated by Django 5.1.5 on 2025-03-03 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Incident",
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
                ("machine_id", models.CharField(max_length=50)),
                ("parameter", models.CharField(max_length=10)),
                ("value", models.CharField(max_length=10)),
                ("threshold", models.CharField(max_length=10)),
                ("duration", models.IntegerField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "metrics_incident",
            },
        ),
        migrations.CreateModel(
            name="SystemMetrics",
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
                ("machine_id", models.CharField(max_length=50)),
                ("cpu", models.IntegerField()),
                ("mem", models.CharField(max_length=10)),
                ("disk", models.CharField(max_length=10)),
                ("uptime", models.CharField(max_length=50)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "metrics_systemmetrics",
            },
        ),
    ]
