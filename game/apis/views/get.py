from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from game.apis.serializers import Battle, BattleSerializer


@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.IsAuthenticated])
def GetBattleView (request, battle_id) :
    try : 
        
        try : 
            battle = Battle.objects.get(id=battle_id)
        except Battle.DoesNotExist : 
            return Response({
                'message' : "battle not found"
            },status=status.HTTP_404_NOT_FOUND)
        
        user = request.user

        if user != battle.created_by or user != battle.vs : 
            return Response({
                'message' : "you don't belong to this battle"
            },status=status.HTTP_400_BAD_REQUEST)
        
        if battle.created_by == None or battle.vs == None : 
            return Response({
                'message' : "battle not completed yet"
            },status=status.HTTP_400_BAD_REQUEST)
        
        serializer = BattleSerializer(battle)

        return Response(serializer.data,status=status.HTTP_200_OK)

    except Exception as error : 
        return Response({
            'message' : f"an error accoured : {error}"
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)