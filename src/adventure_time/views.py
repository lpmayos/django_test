from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from adventure_time.serializers import WorldSerializer, LocationSerializer, UserSerializer
from adventure_time.models import World, Location
from adventure_time.permissions import IsOwnerOrReadOnly


class IndexView(generic.ListView):
    template_name = 'adventure_time/index.html'
    context_object_name = 'latest_world_list'

    def get_queryset(self):
        """ Return the list of worlds (not including those set to be created in the future).
        """
        return World.objects.filter(creation_date__lte=timezone.now()).order_by('name')


class DetailView(generic.DetailView):
    model = World
    template_name = 'adventure_time/detail.html'

    def get_queryset(self):
            """ Excludes any worlds that aren't created yet.
            """
            return World.objects.filter(creation_date__lte=timezone.now())


class RankingView(generic.DetailView):
    model = World
    template_name = 'adventure_time/ranking.html'


def like(request, world_id):
    world = get_object_or_404(World, pk=world_id)
    try:
        selected_location = world.locations.get(pk=request.POST['location'])
    except (KeyError, Location.DoesNotExist):
        # Redisplay the world voting form.
        return render(request, 'adventure_time/detail.html', {
            'world': world,
            'error_message': "You didn't select a location.",
        })
    else:
        selected_location.likes += 1
        selected_location.save()
        return HttpResponseRedirect(reverse('adventure_time:ranking', args=(world.id,)))


# Django REST framework views

class WorldViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = World.objects.all()
    serializer_class = WorldSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class LocationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
