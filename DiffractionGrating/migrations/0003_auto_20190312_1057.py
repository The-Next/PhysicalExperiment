# Generated by Django 2.1.7 on 2019-03-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiffractionGrating', '0002_auto_20190312_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diffractiongrating',
            name='d',
            field=models.DecimalField(decimal_places=7, max_digits=15, verbose_name='光栅常数'),
        ),
    ]
