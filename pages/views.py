#!/usr/bin/env python
__author__ = "Ryan Manella"

from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Hello World!")
