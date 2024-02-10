from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from users.models import User

@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.IsAuthenticated])
def LeaderBoardView (request) : 
    try : 
        users = User.objects.order_by('-points').values('full_name','points')[:5]
        return Response(users,status=status.HTTP_200_OK)
    except Exception as error :
        return Response({
            'message' : f"an error accoured : {error}" 
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)