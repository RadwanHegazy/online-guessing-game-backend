from django.urls import path
from .views import create, get, check


urlpatterns = [
    path('create/',create.CreateBattleView),
    path('get/<str:battle_id>/',get.GetBattleView),
    path('check/<str:battle_id>/',check.CheckBattle),

]