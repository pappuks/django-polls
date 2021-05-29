from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hellp, world, Yo you are great and at polls index.")

# Create your views here.
