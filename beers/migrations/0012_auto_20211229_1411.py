# Generated by Django 3.2.5 on 2021-12-29 14:11

import beers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0011_alter_beer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to=beers.models.filePath)),
            ],
        ),
        migrations.RemoveField(
            model_name='beer',
            name='image',
        ),
    ]