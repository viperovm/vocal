# Generated by Django 3.0.8 on 2020-08-01 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200801_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='international',
            name='heading',
        ),
    ]
