from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    # path('about/', about, name='about'),
    # path('international/', international, name='international'),
    # path('classes/', classes, name='classes'),
    # path('teachers/', teachers, name='teachers'),
    # path('contact/', contact, name='contact'),
]