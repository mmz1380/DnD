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


class DiceType(models.TextChoices):
    D4 = 'd4'
    D6 = 'd6'
    D8 = 'd8'
    D10 = 'd10'
    D12 = 'd12'
    D20 = 'd20'
    D100 = 'd%'
