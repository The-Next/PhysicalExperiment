# Generated by Django 2.1.7 on 2019-04-18 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ThermalConductivity', '0003_auto_20190307_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThermalConductivity_PDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, default='李华', max_length=20, null=True, verbose_name='学生姓名')),
                ('user_num', models.CharField(blank=True, default='1', max_length=20, null=True, verbose_name='学生学号')),
                ('uu_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='用来关联pdf文档的id')),
                ('pdf_file', models.FileField(upload_to='pdf/ThermalConductivity', verbose_name='PDF文件')),
            ],
        ),
        migrations.AddField(
            model_name='thermalconductivity',
            name='uu_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='用来关联pdf文档的id'),
        ),
        migrations.AlterField(
            model_name='thermalconductivity',
            name='img10',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='升温曲线'),
        ),
        migrations.AlterField(
            model_name='thermalconductivity',
            name='img20',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='降温曲线'),
        ),
    ]
