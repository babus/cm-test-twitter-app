# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'TweetData.tweeted_at'
        db.delete_column('twitter_face_tweetdata', 'tweeted_at')

        # Adding field 'TweetData.submitted_on'
        db.add_column('twitter_face_tweetdata', 'submitted_on',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 2, 0, 0)),
                      keep_default=False)


        # Changing field 'TweetData.content'
        db.alter_column('twitter_face_tweetdata', 'content', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'TweetData.tweeted_at'
        raise RuntimeError("Cannot reverse this migration. 'TweetData.tweeted_at' and its values cannot be restored.")
        # Deleting field 'TweetData.submitted_on'
        db.delete_column('twitter_face_tweetdata', 'submitted_on')


        # Changing field 'TweetData.content'
        db.alter_column('twitter_face_tweetdata', 'content', self.gf('django.db.models.fields.CharField')(max_length=110))

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
        'twitter_face.tweetdata': {
            'Meta': {'object_name': 'TweetData'},
            'category': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '255', 'blank': 'True'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'generic_item': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'specific_item_type': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '255', 'blank': 'True'}),
            'submitted_on': ('django.db.models.fields.DateTimeField', [], {}),
            'tweeted_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tweets'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['twitter_face']