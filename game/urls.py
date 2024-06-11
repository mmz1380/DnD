from django.urls import path

from .views import RollDiceAPIView, SubmitTurnAPIView, PlayerCreateView, CharacterCreateView

urlpatterns = [
    path('roll/', RollDiceAPIView.as_view()),
    path('submit/', SubmitTurnAPIView.as_view()),
    path('player/', PlayerCreateView.as_view()),
    path('characters/', CharacterCreateView.as_view())
]
