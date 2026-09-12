from django.urls import path
from .views import handler

urlpatterns = [
    path('', handler, name='homepage'),
    ]