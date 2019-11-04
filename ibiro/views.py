from django.shortcuts import render
from django.http  import HttpResponse
from .models import Location
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileForm

# Create your views here.




@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def profile_form(request):
    current_user = request.user
    if request.method == 'POST':
        form =  ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        form = ProfileForm()
    return render(request, 'all-posts/profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    # snap = Snap.objects.filter(user=current_user)
    profilepicture=Profile.objects.get(user=current_user)
   
 
    return render(request, 'all-posts/profiledisplay.html', {"profilepicture": profilepicture})
