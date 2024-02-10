from django.urls import path
from .views import login, register, profile, leaderboard

urlpatterns = [
    path('login/',login.LoginView),
    path('register/',register.RegisterView),
    path('profile/',profile.ProfileView),
    path('leaderboard/',leaderboard.LeaderBoardView),
]

