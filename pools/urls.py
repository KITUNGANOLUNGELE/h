from django.urls import path
from .views import *

urlpatterns = [
    path('', sayhello, name="Hello")
]