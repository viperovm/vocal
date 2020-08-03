from django.shortcuts import render
from .models import *


def index(request):
    slider_item_1 = Slider.objects.get(name='Слайдер 1')
    slider_item_2 = Slider.objects.get(name='Слайдер 2')
    slider_item_3 = Slider.objects.get(name='Слайдер 3')
    about = About.objects.get(name='Раздел О нас')
    classes = Studies.objects.get(name='Раздел Классы')
    class_items = Studies.objects.exclude(name='Раздел Классы')
    reasons = Reasons.objects.get(name='Раздел Причины')
    reasons_items_1 = Reasons.objects.all()[1:4]
    reasons_img = Reasons.objects.get(name='4 элемент')
    reasons_items_2 = Reasons.objects.all()[5:8]
    counter = Counter.objects.get(name='Раздел Счетчик')
    counter_items = Counter.objects.exclude(name='Раздел Счетчик')
    testimonials = Testimonials.objects.get(name='Раздел отзывы')
    testimonials_items = Testimonials.objects.exclude(name='Раздел отзывы')

    context = {
        'title': 'Главная страница',
        'slider_item_1': slider_item_1,
        'slider_item_2': slider_item_2,
        'slider_item_3': slider_item_3,
        'about': about,
        'classes': classes,
        'class_items': class_items,
        'reasons': reasons,
        'reasons_items_1': reasons_items_1,
        'reasons_img': reasons_img,
        'reasons_items_2': reasons_items_2,
        'counter': counter,
        'counter_items': counter_items,
        'testimonials': testimonials,
        'testimonials_items': testimonials_items,
    }
    return render(request, 'home/index.html', context)
