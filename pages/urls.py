#!/usr/bin/env python
__author__ = "Ryan Manella"

from django.urls import path
from .views import homePageView

urlpatterns = [
    path("", homePageView, name="home"),
]

