from django.db import models


class Race(models.TextChoices):
    DRAGONBORN = 'dragonborn'
    DWARF = 'dwarf'
    ELF = 'elf'
    GNOME = 'gnome'
    HALF_ELF = 'half-Elf'
    HALFLING = 'halfling'
    HALF_ORC = 'half-Orc'
    HUMAN = 'human'
    TIEFLING = 'tiefling'
    ORG = 'orc'


class CharacterClass(models.TextChoices):
    BARBARIAN = 'barbarian'
    BARD = 'bard'
    CLERIC = 'cleric'
    DRUID = 'druid'
    FIGHTER = 'fighter'
    MONK = 'monk'
    PALADIN = 'paladin'
    RANGER = 'ranger'
    ROGUE = 'rogue'
    SORCERER = 'sorcerer'
    WARLOCK = 'warlock'
    WIZARD = 'wizard'


class EnvironmentType(models.TextChoices):
    Plain = 'plain'
    Mountain = 'mountain'
    Road = 'road'
    Dungeon = 'dungeon'
