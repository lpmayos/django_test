from rest_framework import serializers
from adventure_time.models import World, Location
from django.contrib.auth.models import User


class WorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = ('id', 'name', 'world_type', 'surface', 'creation_date', 'owner')

    owner = serializers.Field(source='owner.username')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'coordinates', 'likes', 'world')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    worlds = serializers.HyperlinkedRelatedField(many=True, view_name='world-detail')

    class Meta:
        model = User
        fields = ('id', 'username', 'worlds')
