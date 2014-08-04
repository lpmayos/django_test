from django.db import models


class World(models.Model):
    name = models.CharField(max_length=200)
    world_types = (
        ('continent', 'Continent'),
        ('home', 'Home'),
        ('kingdom', 'Kingdom'),
        ('world', 'World'),
        ('demon_world', 'Demon World'),
    )
    world_type = models.CharField(max_length=200,
                                  choices=world_types,
                                  default='kingdom')
    surface = models.IntegerField()

    def __unicode__(self):
            return self.name


class Location(models.Model):
    world = models.ForeignKey(World)
    name = models.CharField(max_length=200)
    coordinates = models.CharField(max_length=200)

    def __unicode__(self):
            return self.name
