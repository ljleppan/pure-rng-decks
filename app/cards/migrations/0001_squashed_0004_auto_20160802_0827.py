# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-02 09:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('cards', '0001_initial'), ('cards', '0002_auto_20160731_1223'), ('cards', '0003_auto_20160802_0802'), ('cards', '0004_auto_20160802_0827')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardId', models.CharField(max_length=16, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('cost', models.SmallIntegerField()),
                ('value', models.FloatField()),
                ('attack', models.SmallIntegerField()),
                ('health', models.SmallIntegerField()),
                ('text', models.CharField(max_length=124)),
            ],
        ),
        migrations.CreateModel(
            name='CardMechanic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_value', models.SmallIntegerField()),
                ('max_value', models.SmallIntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Card')),
            ],
        ),
        migrations.CreateModel(
            name='CardSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CardType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('value', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Rarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='cardmechanic',
            name='mechanic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Mechanic'),
        ),
        migrations.AddField(
            model_name='card',
            name='cardSet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.CardSet'),
        ),
        migrations.AddField(
            model_name='card',
            name='cardType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.CardType'),
        ),
        migrations.AddField(
            model_name='card',
            name='card_mechanics',
            field=models.ManyToManyField(through='cards.CardMechanic', to='cards.Mechanic'),
        ),
        migrations.AddField(
            model_name='card',
            name='character_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.CharacterClass'),
        ),
        migrations.AddField(
            model_name='card',
            name='faction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Faction'),
        ),
        migrations.AddField(
            model_name='card',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Race'),
        ),
        migrations.AddField(
            model_name='card',
            name='rarity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Rarity'),
        ),
        migrations.RenameField(
            model_name='cardmechanic',
            old_name='max_value',
            new_name='effect_size',
        ),
        migrations.RemoveField(
            model_name='cardmechanic',
            name='min_value',
        ),
        migrations.AlterUniqueTogether(
            name='cardmechanic',
            unique_together=set([('card', 'mechanic')]),
        ),
        migrations.RenameField(
            model_name='card',
            old_name='value',
            new_name='complex_value',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='cost',
            new_name='mana',
        ),
    ]
