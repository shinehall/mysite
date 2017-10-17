from django.conf.urls import url
from . import views

app_name = 'user'
urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'), 
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'), 
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # url(r'^$', views.user_login_get, name='user_login_get'),
    url(r'^profile/$', views.user_profile, name='user_profile'), 
    # url(r'^login/$', views.user_login_post, name='user_login_post'),
    # url(r'^logout/$', views.user_logout, name='user_logout'),
]