from django.contrib import admin
from .models import Battle, Help


class BattlePanel (admin.ModelAdmin) : 
    list_display = ['created_by','vs','id']


admin.site.register(Battle,BattlePanel)
admin.site.register(Help)
