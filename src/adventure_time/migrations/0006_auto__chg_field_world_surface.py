# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'World.surface'
        db.alter_column(u'adventure_time_world', 'surface', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'World.surface'
        db.alter_column(u'adventure_time_world', 'surface', self.gf('django.db.models.fields.IntegerField')(default=0))

    models = {
        u'adventure_time.location': {
            'Meta': {'object_name': 'Location'},
            'coordinates': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'world': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['adventure_time.World']"})
        },
        u'adventure_time.world': {
            'Meta': {'object_name': 'World'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'surface': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'world_type': ('django.db.models.fields.CharField', [], {'default': "'kingdom'", 'max_length': '200'})
        }
    }

    complete_apps = ['adventure_time']