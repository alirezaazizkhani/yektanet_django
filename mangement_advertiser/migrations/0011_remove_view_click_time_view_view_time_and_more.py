# Generated by Django 5.0.2 on 2024-02-27 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangement_advertiser', '0010_alter_click_click_time_alter_view_click_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='view',
            name='click_time',
        ),
        migrations.AddField(
            model_name='view',
            name='view_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='click',
            name='click_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
