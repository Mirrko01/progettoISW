from django.shortcuts import render
from django.http import HttpResponse


def firstView(request):
    return HttpResponse("First view")
