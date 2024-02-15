from rest_framework import permissions, status, decorators
from rest_framework.response import Response
from game.models import Battle, Help
from game.apis.serializers import BattleSerializer
from django.core.cache import cache


@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAuthenticated])
def CreateBattleView (request) : 
    try :
        
        data = request.data
        
        user = request.user
        
        help_text_list = data.getlist('help_text')
        
        battle = Battle.objects.create(
            created_by = user,
            word = data.get('word')
        )

        battle.save()

        for i in help_text_list : 
            
            h = Help.objects.create(
                text = i
            )    
            
            h.save()

            battle.help_text.add(h)
            battle.save()
            

        battles = BattleSerializer(Battle.objects.all(),many=True)
        cache.set('battles',battles.data,3600)
      
        return Response(
            {
                'id' : battle.id
            },status=status.HTTP_200_OK
        )

    except Exception as error :
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)