from django.urls import path, re_path
from RussianTravels.Views.Person.Person import PersonMainPage
urlpatterns = [
    re_path('^$', PersonMainPage)
]