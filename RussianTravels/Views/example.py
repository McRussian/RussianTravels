from django.http import HttpResponse

def HelloWorld(request):
    return  HttpResponse("Hello World")

def MainPage(request):
    return HttpResponse("Main Page")

