# Generated by Django 3.0.8 on 2020-08-01 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_counter_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='counter_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Идентификатор'),
        ),
    ]
