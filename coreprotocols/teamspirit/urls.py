from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.landing_page,  name='landing_page'),
    url(r'team/create/$', views.team_create,  name='team_create'),
    url(r'team/signup/$', views.sign_up,  name='sign_up'),
    url(r'dashboard/$', views.dashboard, name='dashboard'),
    url(r'team/member/add/(?P<pk>.+)$', views.member_add, name='member_add'),
    url(r'team/session/close/', views.session_close, name='session_close'),
    url(r'team/session/add/(?P<pk>.+)$', views.session_add, name='session_add'),
    url(r'team/session/emotion/record', views.session_emotion_record, name='session_emotion_record'),
    url(r'team/session/stats/(?P<pk>.+)$', views.session_stats, name='session_stats'),

]