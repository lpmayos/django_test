from django.conf.urls import patterns, url
from adventure_time import views


urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       url(r'^(?P<pk>\d+)/ranking/$', views.RankingView.as_view(), name='ranking'),
                       url(r'^(?P<world_id>\d+)/like/$', views.like, name='like'),
                       )
