from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^profileform', views.profile_form, name='profile'),
    url(r'^profiledisplay', views. user_profile, name='profiledisplay'),
    url(r'^new/post$', views.new_post, name='new_post'),
]