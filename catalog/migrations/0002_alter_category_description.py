# Generated by Django 4.2.4 on 2023-08-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Описание'),
        ),
    ]
