# Generated by Django 2.1.7 on 2019-03-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ThermalConductivity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thermalconductivity',
            name='p1',
            field=models.CharField(max_length=100, verbose_name='二次方程'),
        ),
        migrations.AlterField(
            model_name='thermalconductivity',
            name='p2',
            field=models.CharField(max_length=100, verbose_name='导函数'),
        ),
    ]
