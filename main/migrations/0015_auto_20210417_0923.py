# Generated by Django 2.2.17 on 2021-04-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210417_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='barcode',
            field=models.CharField(blank=True, max_length=120, verbose_name='Barcode'),
        ),
    ]
