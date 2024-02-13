from rest_framework import permissions, status, decorators
from rest_framework.response import Response
from game.models import Battle, Help
from game.apis.serializers import BattleSerializer


@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAuthenticated])
def CreateBattleView (request) : 
    try :
        
        data = request.data.copy()
        user = request.user
        data['created_by'] = user.id

        serializer = BattleSerializer(data=data)

        if serializer.is_valid() : 
            res = serializer.save()
            return Response(res,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    except Exception as error :
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)