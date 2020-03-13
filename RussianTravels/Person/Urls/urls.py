from django.urls import re_path
from RussianTravels.Person.Views.view import PersonMainPage
urlpatterns = [
    re_path('^$', PersonMainPage)
]