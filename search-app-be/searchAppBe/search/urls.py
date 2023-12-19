from django.urls import path
from .views import search, hello

urlpatterns = [
    path('search', search, name='search'),
    path('hello', hello, name='hello'),
]
