from django.urls import path
from . import views

# all urls are given below
urlpatterns = [
    path("", views.dummy, name="dummy"),
    path("index/<str:msg>", views.index, name="index"),
    path("LOC", views.LOC, name="LOC"),
    path("vote", views.vote, name="vote"),
    path("results", views.results, name="results"),
]
