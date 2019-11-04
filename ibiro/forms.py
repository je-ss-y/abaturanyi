from .models import Profile,Snap
from django.contrib.auth.models import User
from django.db import models
from django import forms




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profilepicture']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }

class PostForm(forms.ModelForm):
    class Meta:
        model = Snap
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
