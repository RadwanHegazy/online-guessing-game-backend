from channels.generic.websocket import WebsocketConsumer
from game.models import Battle
from django.core.cache import cache
import threading, json

class SearchBattleConsumer (WebsocketConsumer) : 
    
    def search_for_battle (self) : 

        while True : 
            avaliable_battles = Battle.objects.filter(vs=None).exclude(created_by=self.user)
            

            if avaliable_battles.count() > 0 :
                avaliable_battle = avaliable_battles[0]
                avaliable_battle.vs = self.user
                avaliable_battle.save()
                battle_id = avaliable_battle.id
                break
        
        
        data = json.dumps({'battle_id' : str(battle_id)})
        
        self.send(data)
        self.close()
        

    def connect(self):
        self.user = self.scope['user']

        if self.user.is_anonymous :
            self.close()
            return
        
        print('connection from ', self.user.full_name)
        
        """
            Write the logic for search for a battle 
            and then return the id of the battle
        """
        self.accept()

        t = threading.Thread(target=self.search_for_battle)
        t.start()

        print("Search is starting ...")

        
        

    def disconnect(self, code):
        pass

    def receive(self, text_data):
        print(f'Recieve : {text_data}')
    
    def enter_battle (self, event) : 
        pass