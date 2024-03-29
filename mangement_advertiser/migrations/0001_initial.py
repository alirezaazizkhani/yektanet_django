# Generated by Django 5.0.2 on 2024-02-24 19:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=25)),
                ('Clicks', models.IntegerField(default=0)),
                ('Views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('imgUrl', models.CharField(max_length=255)),
                ('Link', models.CharField(max_length=255)),
                ('Clicks', models.IntegerField(default=0)),
                ('Views', models.IntegerField(default=0)),
                ('Advertiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangement_advertiser.advertiser')),
            ],
        ),
    ]
