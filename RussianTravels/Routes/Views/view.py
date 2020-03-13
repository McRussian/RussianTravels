from django.http import HttpResponse

def RouteMainPage(request):
    return HttpResponse("Main Page Route's")