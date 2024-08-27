# Generated by Django 5.0.4 on 2024-08-21 12:05

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_сountry_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
            managers=[
                ('city', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='country',
            managers=[
                ('country', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='country',
            name='city',
        ),
        migrations.AddField(
            model_name='country',
            name='city',
            field=models.ManyToManyField(related_name='countries', to='products.city', verbose_name='Город'),
        ),
    ]
