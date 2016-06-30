from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.landing_page,  name='landing_page'),
    url(r'team/create/$', views.team_create,  name='team_create'),
]