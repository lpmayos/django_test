from django.contrib import admin
from adventure_time.models import World, Location


class LocationInline(admin.TabularInline):
    model = Location
    extra = 3


class WorldAdmin(admin.ModelAdmin):
    # fields = ['name', 'surface', 'world_type']
    fieldsets = [
        (None, {'fields': ['name', 'world_type', 'creation_date', 'owner']}),
        ('Other information', {'fields': ['surface'], 'classes': ['collapse']}),
    ]
    inlines = [LocationInline]
    list_display = ('name', 'world_type', 'surface', 'was_created_recently', 'creation_date', 'owner')
    list_filter = ['world_type']
    search_fields = ['name']

admin.site.register(World, WorldAdmin)
