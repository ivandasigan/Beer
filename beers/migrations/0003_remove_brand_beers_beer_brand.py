# Generated by Django 4.0 on 2021-12-23 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0002_remove_brand_beers_brand_beers_alter_brand_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='beers',
        ),
        migrations.AddField(
            model_name='beer',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beers.brand'),
        ),
    ]
