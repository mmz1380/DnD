from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from .enums import Race, CharacterClass, EnvironmentType


class TimeStampMixin:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Player(models.Model, TimeStampMixin):
    user = models.OneToOneField(User, related_name='player', on_delete=models.CASCADE, unique=True)


class Character(models.Model, TimeStampMixin):
    name = models.CharField(_('Name'), max_length=100)
    race = models.CharField(_('Race'), max_length=30, choices=Race.choices)
    character_class = models.CharField(_("Character Class"), max_length=30, choices=CharacterClass.choices)
    strength = models.IntegerField(_("Strength"), default=0)
    dexterity = models.IntegerField(_("Dexterity"), default=0)
    constitution = models.IntegerField(_("Constitution"), default=0)
    intelligence = models.IntegerField(_("Intelligence"), default=0)
    wisdom = models.IntegerField(_("Wisdom"), default=0)
    charisma = models.IntegerField(_("Charisma"), default=0)
    luck = models.IntegerField(_("Luck"), default=1)
    player = models.ForeignKey(Player, related_name='characters', on_delete=models.CASCADE)


class GameMaster(models.Model, TimeStampMixin):
    user = models.OneToOneField(User, related_name='game_master', on_delete=models.CASCADE, unique=True)


class Game(models.Model, TimeStampMixin):
    game_master = models.ForeignKey(GameMaster, related_name='games', on_delete=models.CASCADE)
    players = models.ManyToManyField(Player, related_name='games', through='GamePlayer')
    characters = models.JSONField(_('Character'), null=True)


class GamePlayer(models.Model, TimeStampMixin):
    game = models.ForeignKey(Game, related_name='game_players', on_delete=models.CASCADE)
    player = models.ForeignKey(Player, related_name='game_players', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('game', 'player')


class NPC(models.Model, TimeStampMixin):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), blank=True)


class EnemyType(models.Model, TimeStampMixin):
    name = models.CharField(_('Name'), max_length=100)


class Enemy(models.Model, TimeStampMixin):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), blank=True)
    hp = models.IntegerField(_('HP'))
    min_power = models.IntegerField(_('Min. Power'))
    max_power = models.IntegerField(_('Max. Power'))
    enemy_type = models.ForeignKey(EnemyType, related_name='enemies', on_delete=models.CASCADE)


class Structure(models.Model, TimeStampMixin):
    name = models.CharField(_('Name'), max_length=100)
    area = models.IntegerField(_('Area'))
    environment_type = models.CharField(_('Environment Type'), max_length=20, choices=EnvironmentType.choices)
