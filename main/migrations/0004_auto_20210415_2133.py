# Generated by Django 2.2.17 on 2021-04-15 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20210415_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersfruits',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Fruit', verbose_name='Friut')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User-Cart',
                'verbose_name_plural': 'User-Carts',
            },
        ),
    ]
