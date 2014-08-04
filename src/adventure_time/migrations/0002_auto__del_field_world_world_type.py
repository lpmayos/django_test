# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'World.world_type'
        db.delete_column(u'adventure_time_world', 'world_type')


    def backwards(self, orm):
        # Adding field 'World.world_type'
        db.add_column(u'adventure_time_world', 'world_type',
                      self.gf('django.db.models.fields.CharField')(default='kingdom', max_length=2),
                      keep_default=False)


    models = {
        u'adventure_time.location': {
            'Meta': {'object_name': 'Location'},
            'coordinates': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'world': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['adventure_time.World']"})
        },
        u'adventure_time.world': {
            'Meta': {'object_name': 'World'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'surface': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['adventure_time']