from django.db import models
from django.utils import timezone
import datetime


class World(models.Model):
    name = models.CharField(max_length=200)
    world_types = (
        ('continent', 'Continent'),
        ('home', 'Home'),
        ('kingdom', 'Kingdom'),
        ('world', 'World'),
        ('demon_world', 'Demon World'),
        ('imagination_realm', 'Imagination realm'),
    )
    world_type = models.CharField(max_length=200,
                                  choices=world_types,
                                  default='kingdom')
    surface = models.IntegerField(null=True)
    creation_date = models.DateTimeField('creation date')
    owner = models.ForeignKey('auth.User',
                              related_name='worlds',
                              null=True,
                              blank=True)

    def __unicode__(self):
            return self.name

    def was_created_recently(self):
            now = timezone.now()
            return now - datetime.timedelta(days=1) <= self.creation_date <= now

    was_created_recently.admin_order_field = 'creation_date'
    was_created_recently.boolean = True
    was_created_recently.short_description = 'Created recently?'


class Location(models.Model):
    world = models.ForeignKey(World,
                              related_name='locations')
    name = models.CharField(max_length=200)
    coordinates = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User',
                              related_name='locations',
                              null=True,
                              blank=True)

    def __unicode__(self):
            return self.name
