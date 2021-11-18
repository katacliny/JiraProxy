from django.shortcuts import render
from django.http import HttpResponse


def proxy_view(request):
    return HttpResponse("OK")

