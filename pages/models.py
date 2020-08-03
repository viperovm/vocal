from django.db import models


class About(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    heading = models.CharField(max_length=200, verbose_name='Заголовок')
    heading2 = models.CharField(max_length=200, verbose_name='Заголовок2')
    heading3 = models.CharField(max_length=200, verbose_name='Заголовок3')
    heading_teachers = models.CharField(max_length=200, verbose_name='Заголовок учителя')
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
        verbose_name = 'Страница О нас'
        verbose_name_plural = 'Страница О нас'
        ordering = ['pk']


class International(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
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
        verbose_name = 'Страница Международное обучение'
        verbose_name_plural = 'Страница Международное обучение'
        ordering = ['pk']


class InternationalElements(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    heading = models.CharField(max_length=200, null=True, blank=True, verbose_name='Заголовок')
    text = models.TextField(null=True, blank=True, verbose_name='Текст')
    img = models.FileField(blank=True, verbose_name='Изображение')

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
        verbose_name = 'Элементы страницы Международное обучение'
        verbose_name_plural = 'Элементы страницы Международное обучение'
        ordering = ['pk']


class Study(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    heading_private = models.CharField(max_length=200, null=True, blank=True, verbose_name='Заголовок Частные занятия')
    text_private = models.TextField(null=True, blank=True, verbose_name='Текст Частные занятия')
    heading_group = models.CharField(max_length=200, null=True, blank=True, verbose_name='Заголовок Групповые занятия')
    text_group = models.TextField(null=True, blank=True, verbose_name='Текст Групповые занятия')
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
        verbose_name = 'Страница Занятий'
        verbose_name_plural = 'Страница Занятий'
        ordering = ['pk']


class StudyPrivateElements(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    heading = models.CharField(max_length=200, null=True, blank=True, verbose_name='Заголовок')
    text = models.TextField(null=True, blank=True, verbose_name='Текст')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Элементы частные Занятия'
        verbose_name_plural = 'Элементы частные Занятия'
        ordering = ['pk']


class StudyGroupElements(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    heading = models.CharField(max_length=200, null=True, blank=True, verbose_name='Заголовок')
    text = models.TextField(null=True, blank=True, verbose_name='Текст')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Элементы групповые Занятия'
        verbose_name_plural = 'Элементы групповые Занятия'
        ordering = ['pk']
