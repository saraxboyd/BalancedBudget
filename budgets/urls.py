from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from django import core as core_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url('logout', auth_views.LogoutView.as_view(next_page='index'), name='logout'), # logout redirects to home page
    url('dashboard', views.dashboard, name = 'dashboard'), # create url path to results page
    url(r'^signup/$', views.signup.as_view(), name='signup'),
]