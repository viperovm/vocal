# Generated by Django 3.0.8 on 2020-08-01 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
