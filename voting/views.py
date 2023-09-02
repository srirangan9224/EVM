from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


def dummy(request):
    """
    returns the index view with an argument of hello
    """
    return HttpResponseRedirect(reverse("index", args=("hello",)))


def index(request, msg=""):
    """
    returns the main page the user is taken to
    """
    return render(
        request,
        "voting/index.html",
        {
            "msg": msg,
            "notNull": msg != "",
        },
    )


def LOC(request):
    """
    returns the page with the list of candidates.
    """
    candidates = Candidate.objects.all()
    return render(
        request,
        "voting/LOC.html",
        {
            "candidates": candidates,
        },
    )


def vote(request):
    """
    returns a page where the user should vote
    """
    if request.method == "POST":
        try:
            girl_candidate = request.POST["girls"]
            boy_candidate = request.POST["boys"]
        except:
            return HttpResponse("error: select a candidate")
        if girl_candidate == "none" or boy_candidate == "none":
            return HttpResponse("candidates not yet registered")
        girl_candidate = Candidate.objects.get(pk=girl_candidate)
        boy_candidate = Candidate.objects.get(pk=boy_candidate)
        girl_candidate.votes += 1
        girl_candidate.save()
        boy_candidate.votes += 1
        boy_candidate.save()

        return HttpResponseRedirect(reverse("index", args=("you have voted",)))

    girls = Candidate.objects.filter(gender="Female").order_by("name").all()
    boys = Candidate.objects.filter(gender="Male").order_by("name").all()
    return render(
        request,
        "voting/vote.html",
        {
            "boys": boys,
            "girls": girls,
        },
    )


def results(request):
    """
    returns the results
    """ 
    girls = Candidate.objects.filter(gender="Female")
    girls = girls.order_by("-votes").all()
    boys = Candidate.objects.filter(gender="Male")
    boys = boys.order_by("-votes").all()
    return render(request, "voting/results.html", {"girls": girls, "boys": boys})
