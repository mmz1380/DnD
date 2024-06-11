# Generated by Django 5.0.6 on 2024-06-11 12:48

import django.db.models.deletion
import game.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='game_masters', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, game.models.TimeStampMixin),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characters', models.JSONField(null=True, verbose_name='Character')),
                ('game_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='game.gamemaster')),
            ],
            bases=(models.Model, game.models.TimeStampMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='players', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, game.models.TimeStampMixin),
        ),
        migrations.CreateModel(
            name='GamePlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_players', to='game.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_players', to='game.player')),
            ],
            bases=(models.Model, game.models.TimeStampMixin),
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(related_name='games', through='game.GamePlayer', to='game.player'),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('race', models.CharField(choices=[('dragonborn', 'Dragonborn'), ('dwarf', 'Dwarf'), ('elf', 'Elf'), ('gnome', 'Gnome'), ('half-Elf', 'Half Elf'), ('halfling', 'Halfling'), ('half-Orc', 'Half Orc'), ('human', 'Human'), ('tiefling', 'Tiefling'), ('orc', 'Org')], max_length=30, verbose_name='Race')),
                ('character_class', models.CharField(choices=[('barbarian', 'Barbarian'), ('bard', 'Bard'), ('cleric', 'Cleric'), ('druid', 'Druid'), ('fighter', 'Fighter'), ('monk', 'Monk'), ('paladin', 'Paladin'), ('ranger', 'Ranger'), ('rogue', 'Rogue'), ('sorcerer', 'Sorcerer'), ('warlock', 'Warlock'), ('wizard', 'Wizard')], max_length=30, verbose_name='Character Class')),
                ('strength', models.IntegerField(default=0, verbose_name='Strength')),
                ('dexterity', models.IntegerField(default=0, verbose_name='Dexterity')),
                ('constitution', models.IntegerField(default=0, verbose_name='Constitution')),
                ('intelligence', models.IntegerField(default=0, verbose_name='Intelligence')),
                ('wisdom', models.IntegerField(default=0, verbose_name='Wisdom')),
                ('charisma', models.IntegerField(default=0, verbose_name='Charisma')),
                ('luck', models.IntegerField(default=1, verbose_name='Luck')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='game.player')),
            ],
            bases=(models.Model, game.models.TimeStampMixin),
        ),
    ]
