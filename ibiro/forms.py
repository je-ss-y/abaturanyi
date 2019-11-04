from .models import Profile
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