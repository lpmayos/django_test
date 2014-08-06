from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from adventure_time.models import World, Location
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
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

class JSONResponse(HttpResponse):
    """ An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def world_list(request):
    """ List all worlds, or create a new world.
    """
    if request.method == 'GET':
        worlds = World.objects.all()
        serializer = WorldSerializer(worlds, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WorldSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def world_detail(request, pk):
    """ Retrieve, update or delete a world.
    """
    try:
        world = World.objects.get(pk=pk)
    except World.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = WorldSerializer(world)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = WorldSerializer(world, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        world.delete()
        return HttpResponse(status=204)
