# Generated by Django 5.0.2 on 2024-03-02 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangement_advertiser', '0011_remove_view_click_time_view_view_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
            ],
        ),
    ]
