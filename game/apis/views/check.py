from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from game.apis.serializers import Battle


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.IsAuthenticated])
def CheckBattle (request, battle_id) :
    try : 
        
        try : 
            battle = Battle.objects.get(id=battle_id)
        except Battle.DoesNotExist : 
            return Response({
                'message' : "battle not found"
            },status=status.HTTP_404_NOT_FOUND)
        
        user = request.user
        word = request.data.get('word',None)

        if word is None : 
            return Response({
                'message' : "insert word"
            },status=status.HTTP_400_BAD_REQUEST)

        if word == battle.word : 
            battle.vs.points = battle.vs.points + 10
            battle.vs.save()
            return Response({
                'message' : 'correct word'
            },status=status.HTTP_200_OK)
        
        else:
            battle.created_by.points = battle.created_by.points + 10
            battle.created_by.save()
            return Response({
                'message' : 'wrong word'
            },status=status.HTTP_200_OK)
        


    except Exception as error : 
        return Response({
            'message' : f"an error accoured : {error}"
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)