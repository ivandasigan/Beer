# Generated by Django 3.2.5 on 2021-12-26 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0004_alter_beer_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
