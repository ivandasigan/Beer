# Generated by Django 4.0 on 2021-12-23 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0003_remove_brand_beers_beer_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beers', to='beers.brand'),
        ),
    ]
