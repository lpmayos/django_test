from rest_framework import serializers
from adventure_time.models import World, Location


class WorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = ('id', 'name', 'world_type', 'surface', 'creation_date')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'coordinates', 'likes', 'world')
