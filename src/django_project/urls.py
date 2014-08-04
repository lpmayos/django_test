from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^worlds/', include('adventure_time.urls', namespace="adventure_time")),
                       url(r'^admin/', include(admin.site.urls)),
                       )
