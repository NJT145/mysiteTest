from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
#from .models import

def overview(request=None):
    return render(request, "contents.html")

