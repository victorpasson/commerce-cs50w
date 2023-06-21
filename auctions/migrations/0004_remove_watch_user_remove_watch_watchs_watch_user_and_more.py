# Generated by Django 4.2.2 on 2023-06-13 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0003_alter_watch_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="watch",
            name="user",
        ),
        migrations.RemoveField(
            model_name="watch",
            name="watchs",
        ),
        migrations.AddField(
            model_name="watch",
            name="user",
            field=models.ManyToManyField(
                related_name="mywatchs", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="watch",
            name="watchs",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="watchs",
                to="auctions.action",
            ),
        ),
    ]