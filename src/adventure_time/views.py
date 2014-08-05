from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from adventure_time.models import World, Location


class IndexView(generic.ListView):
    template_name = 'worlds/index.html'
    context_object_name = 'latest_world_list'

    def get_queryset(self):
        """ Return the last five published polls.
        """
        return World.objects.order_by('name')[:5]


class DetailView(generic.DetailView):
    model = World
    template_name = 'worlds/detail.html'


class RankingView(generic.DetailView):
    model = World
    template_name = 'worlds/ranking.html'


def like(request, world_id):
    world = get_object_or_404(World, pk=world_id)
    try:
        selected_location = world.location_set.get(pk=request.POST['location'])
    except (KeyError, Location.DoesNotExist):
        # Redisplay the world voting form.
        return render(request, 'worlds/detail.html', {
            'world': world,
            'error_message': "You didn't select a location.",
        })
    else:
        selected_location.likes += 1
        selected_location.save()
        return HttpResponseRedirect(reverse('adventure_time:ranking', args=(world.id,)))
