from rest_framework import serializers
from adventure_time.models import World, Location
from django.contrib.auth.models import User


class WorldSerializer(serializers.ModelSerializer):
    locations = serializers.HyperlinkedRelatedField(many=True, view_name='location-detail')
    owner = serializers.Field(source='owner.username')

    class Meta:
        model = World
        fields = ('id', 'name', 'world_type', 'surface', 'creation_date', 'owner', 'locations')


class LocationSerializer(serializers.ModelSerializer):
    world = serializers.HyperlinkedRelatedField(many=False, view_name='world-detail')
    owner = serializers.Field(source='owner.username')

    class Meta:
        model = Location
        fields = ('id', 'name', 'coordinates', 'likes', 'world', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    worlds = serializers.HyperlinkedRelatedField(many=True, view_name='world-detail')
    locations = serializers.HyperlinkedRelatedField(many=True, view_name='location-detail')

    class Meta:
        model = User
        fields = ('id', 'username', 'worlds', 'locations')
