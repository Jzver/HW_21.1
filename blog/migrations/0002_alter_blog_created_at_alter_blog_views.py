# Generated by Django 5.0.4 on 2024-06-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="дата создания"),
        ),
        migrations.AlterField(
            model_name="blog",
            name="views",
            field=models.PositiveIntegerField(default=0, verbose_name="просмотры"),
        ),
    ]
