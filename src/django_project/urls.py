from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from adventure_time import views


admin.autodiscover()

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'worlds', views.WorldViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^', include('adventure_time.urls', namespace="adventure_time")),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       )
