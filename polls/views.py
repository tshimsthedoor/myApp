from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You are a the polls index")