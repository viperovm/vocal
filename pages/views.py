from django.shortcuts import render
from .models import *


def about(request):
    about = About.objects.get(name='Страница О нас')
    context = {
        'title': 'О нас',
        'about': about,
    }
    return render(request, 'pages/about.html', context)


def international(request):
    international_page = International.objects.get(name='Международное обучение')
    international_page_items = InternationalElements.objects.all()
    context = {
        'title': 'Международное обучение',
        'international_page': international_page,
        'international_page_items': international_page_items,
    }
    return render(request, 'pages/international.html', context)


def classes(request):
    classes = Study.objects.get(name='Занятия')
    private_classes_elements = StudyPrivateElements.objects.all()
    group_classes_elements = StudyGroupElements.objects.all()
    context = {
        'title': 'Занятия',
        'classes': classes,
        'private_classes_elements': private_classes_elements,
        'group_classes_elements': group_classes_elements,
    }
    return render(request, 'pages/classes.html', context)


def contact(request):
    context = {}
    return render(request, 'pages/contact.html', context)
