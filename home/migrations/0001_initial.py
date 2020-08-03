# Generated by Django 3.0.8 on 2020-08-01 14:01

from django.db import migrations, models
import faicon.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', faicon.fields.FAIconField(max_length=50, verbose_name='Иконка')),
                ('number', models.IntegerField(verbose_name='Число')),
                ('text', models.CharField(max_length=50, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Элементы счетчика',
                'verbose_name_plural': 'Элементы счетчика',
            },
        ),
        migrations.CreateModel(
            name='HomeAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('heading1', models.CharField(max_length=200, verbose_name='Заголовок1')),
                ('heading2', models.CharField(max_length=200, verbose_name='Заголовок2')),
                ('text', models.TextField(verbose_name='Текст')),
                ('button_text', models.CharField(max_length=50, verbose_name='Текст кнопки')),
                ('img', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Раздел О нас',
                'verbose_name_plural': 'Раздел О нас',
            },
        ),
        migrations.CreateModel(
            name='HomeClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('heading', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('button_text', models.CharField(max_length=50, verbose_name='Текст кнопки')),
            ],
            options={
                'verbose_name': 'Раздел Классы',
                'verbose_name_plural': 'Раздел Классы',
            },
        ),
        migrations.CreateModel(
            name='HomeCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('heading', models.CharField(max_length=200, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Раздел Счетчик',
                'verbose_name_plural': 'Раздел Счетчик',
            },
        ),
        migrations.CreateModel(
            name='HomePageClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.CharField(max_length=255, verbose_name='Текст')),
                ('img', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Элементы классов',
                'verbose_name_plural': 'Элементы классов',
            },
        ),
        migrations.CreateModel(
            name='HomeReasons1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('heading', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('img', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Раздел 5 причин',
                'verbose_name_plural': 'Раздел 5 причин',
            },
        ),
        migrations.CreateModel(
            name='HomeReasons2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('heading', models.CharField(max_length=200, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Раздел на главной Почему все же мы',
                'verbose_name_plural': 'Раздел на главной Почему все же мы',
            },
        ),
        migrations.CreateModel(
            name='Reasons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('heading', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.CharField(max_length=255, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Элементы раздела 5 причин',
                'verbose_name_plural': 'Элементы раздела 5 причин',
            },
        ),
        migrations.CreateModel(
            name='Reasons2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('heading', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.CharField(max_length=255, verbose_name='Текст')),
                ('img', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Элементы раздела почему все же мы',
                'verbose_name_plural': 'Элементы раздела почему все же мы',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('heading', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст 1')),
                ('text2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст 2')),
                ('button_text', models.CharField(max_length=50, verbose_name='Текст кнопки')),
                ('img', models.ImageField(upload_to='slider/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Элементы слайдера',
                'verbose_name_plural': 'Элементы слайдера',
            },
        ),
    ]