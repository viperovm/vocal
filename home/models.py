from django.db import models
from faicon.fields import FAIconField


# Dynamic content for home page

class Slider(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    heading = models.CharField(max_length=200, verbose_name='Заголовок')
    text1 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Текст 1')
    text2 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Текст 2')
    button_text = models.CharField(max_length=50, verbose_name='Текст кнопки')
    img = models.ImageField(upload_to='slider/', verbose_name='Изображение')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'
        ordering = ['name']


class About(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    heading1 = models.CharField(max_length=200, verbose_name='Заголовок1')
    heading2 = models.CharField(max_length=200, verbose_name='Заголовок2')
    text = models.TextField(verbose_name='Текст')
    button_text = models.CharField(max_length=50, verbose_name='Текст кнопки')
    img = models.ImageField(verbose_name='Изображение')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Studies(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    heading = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    button_text = models.CharField(max_length=50, null=True, blank=True, verbose_name='Текст кнопки')
    img = models.ImageField(blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = 'Классы'
        verbose_name_plural = 'Классы'
        ordering = ['pk']


class Reasons(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    heading = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.CharField(max_length=255, blank=True, verbose_name='Текст')
    icon = FAIconField(blank=True, verbose_name='Иконка')
    img = models.ImageField(blank=True, verbose_name='Изображение')

    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Причины'
        verbose_name_plural = 'Причины'
        ordering = ['pk']


class Counter(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Наименование')
    heading = models.CharField(max_length=200, blank=True, verbose_name='Заголовок')
    icon = FAIconField(blank=True, verbose_name='Иконка')
    counter_id = models.CharField(max_length=20, blank=True, verbose_name='Идентификатор')
    number = models.IntegerField(null=True, blank=True, verbose_name='Число')
    text = models.CharField(max_length=50, blank=True, verbose_name='Текст')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Счетчик'
        verbose_name_plural = 'Счетчик'
        ordering = ['pk']


class Testimonials(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    heading = models.CharField(max_length=200, verbose_name='Заголовок')
    heading2 = models.CharField(max_length=200, blank=True, verbose_name='Заголовок2')
    text = models.TextField(blank=True, verbose_name='Текст')
    img = models.ImageField(blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.heading

    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'
        ordering = ['pk']