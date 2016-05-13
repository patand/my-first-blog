# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Calendar'
        db.create_table('notes_calendar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('notes', ['Calendar'])

        # Adding model 'Event'
        db.create_table('notes_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_cancelled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('calendar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notes.Calendar'])),
        ))
        db.send_create_signal('notes', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Calendar'
        db.delete_table('notes_calendar')

        # Deleting model 'Event'
        db.delete_table('notes_event')


    models = {
        'notes.calendar': {
            'Meta': {'ordering': "['name']", 'object_name': 'Calendar'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'notes.event': {
            'Meta': {'ordering': "['start', 'end']", 'object_name': 'Event'},
            'calendar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['notes.Calendar']"}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_cancelled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['notes']