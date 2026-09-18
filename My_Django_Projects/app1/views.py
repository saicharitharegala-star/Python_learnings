from django.http import HttpResponse


def blog(request):
    return HttpResponse("Welcome to my blog")
