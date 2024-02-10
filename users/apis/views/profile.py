from rest_framework import decorators, status, permissions
from rest_framework.response import Response


@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.IsAuthenticated])
def ProfileView (request) : 
    try : 
        user = request.user
        data = {
            'full_name' : user.full_name,
            'picture' : user.picture.url,
            'points' : user.points
        }
        return Response(data,status=status.HTTP_200_OK)
    except Exception as error :
        return Response({
            'message' : f"an error accoured : {error}"
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)