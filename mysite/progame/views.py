from django.http import HttpResponse


def index(request):
    return HttpResponse("SALOM! .")


def hello(requsest):
    return HttpResponse('SALOM GURUH')
