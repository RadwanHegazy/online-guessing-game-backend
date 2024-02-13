from django.urls import path
from .views import create, get


urlpatterns = [
    path('create/',create.CreateBattleView),
    path('get/<str:battle_id>/',get.GetBattleView),
]