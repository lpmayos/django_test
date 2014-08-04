from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from adventure_time.models import World


def index(request):
    latest_world_list = World.objects.all().order_by('name')[:5]
    context = {'latest_world_list': latest_world_list}
    return render(request, 'worlds/index.html', context)


def detail(request, world_id):
    world = get_object_or_404(World, pk=world_id)
    return render(request, 'worlds/detail.html', {'world': world})


def ranking(request, world_id):
    return HttpResponse("You're looking at the location likes ranking of world %s." % world_id)


def like(request, world_id):
    return HttpResponse("You're liking locations on world %s." % world_id)
