from django.http import HttpResponse


def index(request):
    return HttpResponse('Александр, вы ювелир!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
