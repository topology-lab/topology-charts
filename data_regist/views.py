from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the data_regist index.")
