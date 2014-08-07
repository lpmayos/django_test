from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from adventure_time.models import World, Location
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from adventure_time.serializers import WorldSerializer


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

@api_view(['GET', 'POST'])
def world_list(request, format=None):
    """ List all worlds, or create a new world.
    """
    if request.method == 'GET':
        worlds = World.objects.all()
        serializer = WorldSerializer(worlds, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WorldSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def world_detail(request, pk, format=None):
    """ Retrieve, update or delete a world instance.
    """
    try:
        world = World.objects.get(pk=pk)
    except World.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WorldSerializer(world)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WorldSerializer(world, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        world.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
