from typing import Collection, Iterable
from django.db import models
from users.models import User
from uuid import uuid4

class Battle (models.Model) : 
    id = models.UUIDField(primary_key=True,db_index=True,editable=False,default=uuid4)
    created_by = models.ForeignKey(User,related_name='user_game',on_delete=models.CASCADE)
    vs = models.ForeignKey(User,related_name='vs_game',on_delete=models.SET_NULL,null=True,blank=True)
    word = models.CharField(max_length=20)
    help_text = models.ManyToManyField("game.Help",related_name='help_text_battle')

    # def save(self, **kwargs) -> None:

        # if self.created_by == self.vs : 
        #     raise ValueError({
        #         'message' : 'created_by user is equals to verses user !'
        #     },)
        
        # return super().save(**kwargs)

    def __str__(self) : 
        return f'{self.id} - {self.created_by.full_name}'


class Help (models.Model) : 
    text = models.TextField()

    def __str__(self) : 
        return self.text
