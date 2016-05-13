# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.user'
        db.add_column('notes_event', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Event.description'
        db.add_column('notes_event', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Event.frequency'
        db.add_column('notes_event', 'frequency',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=10),
                      keep_default=False)

        # Adding field 'Event.fin'
        db.add_column('notes_event', 'fin',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Event.rep'
        db.add_column('notes_event', 'rep',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Event.activated'
        db.add_column('notes_event', 'activated',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Event.lundi'
        db.add_column('notes_event', 'lundi',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Event.mardi'
        db.add_column('notes_event', 'mardi',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Event.mercredi'
        db.add_column('notes_event', 'mercredi',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Event.jeudi'
        db.add_column('notes_event', 'jeudi',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Event.vendredi'
        db.add_column('notes_event', 'vendredi',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Event.samedi'
        db.add_column('notes_event', 'samedi',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Event.dimanche'
        db.add_column('notes_event', 'dimanche',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.user'
        db.delete_column('notes_event', 'user_id')

        # Deleting field 'Event.description'
        db.delete_column('notes_event', 'description')

        # Deleting field 'Event.frequency'
        db.delete_column('notes_event', 'frequency')

        # Deleting field 'Event.fin'
        db.delete_column('notes_event', 'fin')

        # Deleting field 'Event.rep'
        db.delete_column('notes_event', 'rep')

        # Deleting field 'Event.activated'
        db.delete_column('notes_event', 'activated')

        # Deleting field 'Event.lundi'
        db.delete_column('notes_event', 'lundi')

        # Deleting field 'Event.mardi'
        db.delete_column('notes_event', 'mardi')

        # Deleting field 'Event.mercredi'
        db.delete_column('notes_event', 'mercredi')

        # Deleting field 'Event.jeudi'
        db.delete_column('notes_event', 'jeudi')

        # Deleting field 'Event.vendredi'
        db.delete_column('notes_event', 'vendredi')

        # Deleting field 'Event.samedi'
        db.delete_column('notes_event', 'samedi')

        # Deleting field 'Event.dimanche'
        db.delete_column('notes_event', 'dimanche')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'notes.calendar': {
            'Meta': {'ordering': "['name']", 'object_name': 'Calendar'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'notes.event': {
            'Meta': {'ordering': "['start', 'end']", 'object_name': 'Event'},
            'activated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'calendar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['notes.Calendar']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dimanche': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'fin': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'frequency': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_cancelled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jeudi': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lundi': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mardi': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mercredi': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rep': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'samedi': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'vendredi': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['notes']