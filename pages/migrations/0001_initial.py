# Generated by Django 3.0.8 on 2020-08-01 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('heading', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('heading2', models.CharField(max_length=200, verbose_name='Заголовок2')),
                ('heading3', models.CharField(max_length=200, verbose_name='Заголовок3')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст')),
                ('button_text', models.CharField(max_length=50, verbose_name='Текст кнопки')),
                ('img', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Страница О нас',
                'verbose_name_plural': 'Страница О нас',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='International',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('heading', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('img', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Страница Международное обучение',
                'verbose_name_plural': 'Страница Международное обучение',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='InternationalElements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('heading', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст')),
                ('img', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Элементы страницы Международное обучение',
                'verbose_name_plural': 'Элементы страницы Международное обучение',
                'ordering': ['pk'],
            },
        ),
    ]
