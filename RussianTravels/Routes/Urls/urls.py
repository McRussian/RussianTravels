from django.urls import re_path
from RussianTravels.Routes.Views.view import RouteMainPage
urlpatterns = [
    re_path('^$', RouteMainPage)
]