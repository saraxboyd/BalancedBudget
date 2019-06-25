from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url('logout', auth_views.LogoutView.as_view(next_page='index'), name='logout'), # logout redirects to home page
    url('dashboard', views.dashboard, name = 'dashboard'), # create url path to results page
]