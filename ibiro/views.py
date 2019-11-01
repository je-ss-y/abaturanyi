from django.shortcuts import render
from django.http  import HttpResponse
from .models import Location


# Create your views here.



def welcome(request):
    location = Location.objects.all()
    return render(request, 'all-posts/welcome.html',{"location":location})

def search_results(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users= Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-posts/search.html',{"searched_users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-posts/search.html',{"message":message})