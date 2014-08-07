from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from adventure_time import views


urlpatterns = patterns('',
                       url(r'^no_api/$', views.IndexView.as_view(), name='index'),
                       url(r'^no_api/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       url(r'^no_api/(?P<pk>\d+)/ranking/$', views.RankingView.as_view(), name='ranking'),
                       url(r'^no_api/(?P<world_id>\d+)/like/$', views.like, name='like'),
                       )

# django rest framewrok url

urlpatterns += patterns('adventure_time.views',
                        url(r'^$', 'world_list'),
                        url(r'^(?P<pk>[0-9]+)/$', 'world_detail'),
                        )

urlpatterns = format_suffix_patterns(urlpatterns)
