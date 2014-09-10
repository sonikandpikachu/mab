# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BetSubject'
        db.create_table(u'bets_betsubject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='not_executed', max_length=31)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('long_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('end_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='own_bets', to=orm['users.User'])),
            ('judge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='judged_bets', null=True, to=orm['users.User'])),
            ('is_private', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'bets', ['BetSubject'])

        # Deleting field 'Bet.status'
        db.delete_column(u'bets_bet', 'status')

        # Deleting field 'Bet.judge'
        db.delete_column(u'bets_bet', 'judge_id')

        # Deleting field 'Bet.is_private'
        db.delete_column(u'bets_bet', 'is_private')

        # Deleting field 'Bet.author'
        db.delete_column(u'bets_bet', 'author_id')

        # Deleting field 'Bet.long_description'
        db.delete_column(u'bets_bet', 'long_description')

        # Deleting field 'Bet.end_datetime'
        db.delete_column(u'bets_bet', 'end_datetime')

        # Deleting field 'Bet.short_description'
        db.delete_column(u'bets_bet', 'short_description')

        # Adding field 'Bet.bet_subject'
        db.add_column(u'bets_bet', 'bet_subject',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['bets.BetSubject']),
                      keep_default=False)

        # Adding field 'Bet.user'
        db.add_column(u'bets_bet', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['users.User']),
                      keep_default=False)

        # Adding field 'Bet.description'
        db.add_column(u'bets_bet', 'description',
                      self.gf('django.db.models.fields.TextField')(default=1),
                      keep_default=False)

        # Adding field 'Bet.is_success'
        db.add_column(u'bets_bet', 'is_success',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field con_users on 'Bet'
        db.delete_table(db.shorten_name(u'bets_bet_con_users'))

        # Removing M2M table for field pro_users on 'Bet'
        db.delete_table(db.shorten_name(u'bets_bet_pro_users'))


    def backwards(self, orm):
        # Deleting model 'BetSubject'
        db.delete_table(u'bets_betsubject')

        # Adding field 'Bet.status'
        db.add_column(u'bets_bet', 'status',
                      self.gf('django.db.models.fields.CharField')(default='not_executed', max_length=31),
                      keep_default=False)

        # Adding field 'Bet.judge'
        db.add_column(u'bets_bet', 'judge',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='judged_bets', null=True, to=orm['users.User']),
                      keep_default=False)

        # Adding field 'Bet.is_private'
        db.add_column(u'bets_bet', 'is_private',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Bet.author'
        raise RuntimeError("Cannot reverse this migration. 'Bet.author' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Bet.author'
        db.add_column(u'bets_bet', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='own_bets', to=orm['users.User']),
                      keep_default=False)

        # Adding field 'Bet.long_description'
        db.add_column(u'bets_bet', 'long_description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Bet.end_datetime'
        raise RuntimeError("Cannot reverse this migration. 'Bet.end_datetime' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Bet.end_datetime'
        db.add_column(u'bets_bet', 'end_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Bet.short_description'
        raise RuntimeError("Cannot reverse this migration. 'Bet.short_description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Bet.short_description'
        db.add_column(u'bets_bet', 'short_description',
                      self.gf('django.db.models.fields.CharField')(max_length=127),
                      keep_default=False)

        # Deleting field 'Bet.bet_subject'
        db.delete_column(u'bets_bet', 'bet_subject_id')

        # Deleting field 'Bet.user'
        db.delete_column(u'bets_bet', 'user_id')

        # Deleting field 'Bet.description'
        db.delete_column(u'bets_bet', 'description')

        # Deleting field 'Bet.is_success'
        db.delete_column(u'bets_bet', 'is_success')

        # Adding M2M table for field con_users on 'Bet'
        m2m_table_name = db.shorten_name(u'bets_bet_con_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bet', models.ForeignKey(orm[u'bets.bet'], null=False)),
            ('user', models.ForeignKey(orm[u'users.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['bet_id', 'user_id'])

        # Adding M2M table for field pro_users on 'Bet'
        m2m_table_name = db.shorten_name(u'bets_bet_pro_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bet', models.ForeignKey(orm[u'bets.bet'], null=False)),
            ('user', models.ForeignKey(orm[u'users.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['bet_id', 'user_id'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'bets.bet': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Bet'},
            'bet_subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bets.BetSubject']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_success': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"})
        },
        u'bets.betsubject': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'BetSubject'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'own_bets'", 'to': u"orm['users.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'end_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'judge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'judged_bets'", 'null': 'True', 'to': u"orm['users.User']"}),
            'long_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'not_executed'", 'max_length': '31'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'bets'", 'symmetrical': 'False', 'through': u"orm['bets.Bet']", 'to': u"orm['users.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['bets']