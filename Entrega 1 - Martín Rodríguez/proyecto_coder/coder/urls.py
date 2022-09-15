from django.urls import path
from coder.views import *

urlpatterns = [
    path("", index),
]