from django.urls import path
from .views import json_handler, html_handler

urlpatterns = [
    path('json/', json_handler),
    path('html', html_handler)
]