from django.conf.urls import patterns, url
from adventure_time import views


urlpatterns = patterns('',
                       # ex: /worlds/
                       url(r'^$', views.index, name='index'),
                       # ex: /worlds/5/
                       url(r'^(?P<world_id>\d+)/$', views.detail, name='detail'),
                       # ex: /worlds/5/ranking/
                       url(r'^(?P<world_id>\d+)/ranking/$', views.ranking, name='ranking'),
                       # ex: /worlds/5/like/
                       url(r'^(?P<world_id>\d+)/like/$', views.like, name='like'),
                       )
