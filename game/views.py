from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

import random

from .enums import DiceType
from .models import Character, Player
from .serializers import CharacterSerializer, PlayerSerializer


class RollDiceAPIView(APIView):
    def post(self, request):
        res = {
            'd4': [],
            'd6': [],
            'd8': [],
            'd10': [],
            'd%': [],
            'd12': [],
            'd20': [],

        }
        for i in range(request.data.get('d4')):
            res['d4'].append(random.randint(1, 4))
        for i in range(request.data.get('d6')):
            res['d6'].append(random.randint(1, 6))
        for i in range(request.data.get('d8')):
            res['d8'].append(random.randint(1, 8))
        for i in range(request.data.get('d10')):
            res['d10'].append(random.randint(1, 10))
        for i in range(request.data.get('d%')):
            res['d%'].append(random.randint(1, 10) * 10)
        for i in range(request.data.get('d12')):
            res['d12'].append(random.randint(1, 12))
        for i in range(request.data.get('d20')):
            res['d20'].append(random.randint(1, 20))
        return Response(res)


class SubmitTurnAPIView(APIView):
    def post(self, request):
        res = []
        for character_id in request.data.keys():
            instance = Character.objects.get(pk=character_id)
            serializer_data = request.data.get(character_id)
            serializer = CharacterSerializer(instance, data=serializer_data, partial=True)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            res.append(serializer.data)
        return Response(res)


class PlayerCreateView(CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class CharacterCreateView(CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
