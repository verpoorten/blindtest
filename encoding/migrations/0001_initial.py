# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-18 07:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('open_status', models.CharField(choices=[('CLOSE', 'close'), ('OPEN', 'open')], default='CLOSE', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gameset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encoding.Category')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encoding.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encoding.Gameset')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True)),
                ('gameset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encoding.Gameset')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interpreter', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('audio_file', models.FileField(upload_to='songs/')),
                ('play_time', models.IntegerField(default=5)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encoding.Game')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encoding.Team'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encoding.Song'),
        ),
    ]
