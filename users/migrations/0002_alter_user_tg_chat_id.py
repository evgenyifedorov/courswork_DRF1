# Generated by Django 5.0.7 on 2024-07-21 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="tg_chat_id",
            field=models.CharField(
                blank=True, max_length=35, null=True, verbose_name="id чата телеграмма"
            ),
        ),
    ]