from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from rest_framework import generics
from adventure_time.serializers import WorldSerializer
from adventure_time.models import World, Location


class IndexView(generic.ListView):
    template_name = 'adventure_time/index.html'
    context_object_name = 'latest_world_list'

    def get_queryset(self):
        """ Return the last five created worlds (not including those set to be created in the future).
        """
        return World.objects.filter(creation_date__lte=timezone.now()).order_by('name')[:5]


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
        selected_location = world.location_set.get(pk=request.POST['location'])
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

class WorldList(generics.ListCreateAPIView):
    """ List all worlds, or create a new world.
    """

    queryset = World.objects.all()
    serializer_class = WorldSerializer


class WorldDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete a world instance.
    """

    queryset = World.objects.all()
    serializer_class = WorldSerializer
