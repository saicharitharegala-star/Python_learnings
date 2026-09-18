from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def blogposts(request):
    return HttpResponse("All blog posts!")
