from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Character, Player, GameMaster, Game, GamePlayer

from authentication.serializers import UserSerializer


class PlayerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    characters = serializers.SerializerMethodField()

    def get_characters(self, obj):
        return CharacterSerializer(obj.characters.all(), many=True).data

    class Meta:
        model = Player
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())

    class Meta:
        model = Character
        fields = (
            'id', 'name', 'race', 'character_class', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom',
            'charisma', 'luck', 'player'
        )


class GameMasterSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = GameMaster
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    game_master = GameMasterSerializer()
    players = PlayerSerializer(many=True)

    def validate(self, data):
        for player_id in data['players']:
            player = Player.objects.get(pk=player_id)
            player_character = data['characters'].get(player.id)
            if isinstance(player_character, int):
                if player_character in player.characters.all():
                    return data
                else:
                    raise serializers.ValidationError('Character does not belong to this Player')
            elif isinstance(player_character, list):
                if len(player_character) != 1:
                    raise serializers.ValidationError(
                        f"You should give only one character; you gave{len(player_character)}")
                else:
                    player_character = player_character[0]
                    if isinstance(player_character, int):
                        if player_character in player.characters.all():
                            return data
                        else:
                            raise serializers.ValidationError('Character does not belong to this Player')
            else:
                raise serializers.ValidationError('Character should be integer and only-and-only one character_id')

    class Meta:
        model = Game
        fields = '__all__'


class GamePlayerSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    game = GameSerializer()

    class Meta:
        model = GamePlayer
        fields = '__all__'
