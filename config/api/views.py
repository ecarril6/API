from django.http import HttpResponse
from django.shortcuts import render

def mainpage(request):
    return HttpResponse("Hello, world! This is the main page")