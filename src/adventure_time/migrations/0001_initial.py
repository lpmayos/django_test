# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'World'
        db.create_table(u'adventure_time_world', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('world_type', self.gf('django.db.models.fields.CharField')(default='kingdom', max_length=2)),
            ('surface', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'adventure_time', ['World'])

        # Adding model 'Location'
        db.create_table(u'adventure_time_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('world', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adventure_time.World'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('coordinates', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'adventure_time', ['Location'])


    def backwards(self, orm):
        # Deleting model 'World'
        db.delete_table(u'adventure_time_world')

        # Deleting model 'Location'
        db.delete_table(u'adventure_time_location')


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
            'surface': ('django.db.models.fields.IntegerField', [], {}),
            'world_type': ('django.db.models.fields.CharField', [], {'default': "'kingdom'", 'max_length': '2'})
        }
    }

    complete_apps = ['adventure_time']