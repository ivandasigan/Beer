# Generated by Django 3.2.5 on 2021-12-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0009_alter_beer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
