from django.shortcuts import render  # noqa: F401 (noqa tells the linter to ignore unused import)
from django.http import HttpResponse

# Create your views here.


def home_page_view(request):
    return HttpResponse("Welcome to Harmonia Hall Events!")

# query to fetch all events in db will go here
