from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<slug:cat>/', categories, name='cats'),
    path('about/', about, name='about'),
]