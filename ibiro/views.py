from django.shortcuts import render
from django.http  import HttpResponse
from .models import Location


# Create your views here.



def welcome(request):
    location = Location.objects.all()
    return render(request, 'all-posts/welcome.html',{"location":location})