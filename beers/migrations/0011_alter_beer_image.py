# Generated by Django 3.2.5 on 2021-12-29 13:44

import beers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0010_alter_beer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='image',
            field=models.ImageField(null=True, upload_to=beers.models.filePath),
        ),
    ]