# Generated by Django 2.1.7 on 2019-02-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Experimentation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newtown',
            name='r25_5',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='25与5所得的曲率半径'),
        ),
        migrations.AlterField(
            model_name='newtown',
            name='r26_6',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='26与6所得的曲率半径'),
        ),
        migrations.AlterField(
            model_name='newtown',
            name='r27_7',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='27与7所得的曲率半径'),
        ),
        migrations.AlterField(
            model_name='newtown',
            name='r28_8',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='28与8所得的曲率半径'),
        ),
        migrations.AlterField(
            model_name='newtown',
            name='r29_9',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='29与9所得的曲率半径'),
        ),
        migrations.AlterField(
            model_name='newtown',
            name='r30_10',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='30与10所得的曲率半径'),
        ),
    ]
