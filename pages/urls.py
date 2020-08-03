from django.urls import path
from .views import *

urlpatterns = [
    path('about/', about, name='about'),
    path('international/', international, name='international'),
    path('classes/', classes, name='classes'),
    path('contact/', contact, name='contact'),
]