# Generated by Django 5.0.2 on 2024-02-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangement_advertiser', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='Advertiser',
            new_name='advertiser_id',
        ),
        migrations.RenameField(
            model_name='ad',
            old_name='Clicks',
            new_name='clicks',
        ),
        migrations.RenameField(
            model_name='ad',
            old_name='ID',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='ad',
            old_name='Link',
            new_name='img_url',
        ),
        migrations.RenameField(
            model_name='ad',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='ad',
            old_name='Views',
            new_name='views',
        ),
        migrations.RenameField(
            model_name='advertiser',
            old_name='Clicks',
            new_name='clicks',
        ),
        migrations.RenameField(
            model_name='advertiser',
            old_name='ID',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='advertiser',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='advertiser',
            old_name='Views',
            new_name='views',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='imgUrl',
        ),
        migrations.AddField(
            model_name='ad',
            name='link',
            field=models.URLField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]