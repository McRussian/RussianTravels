from django.http import HttpResponse

def PersonMainPage(request):
    return HttpResponse("Main Page Person's")