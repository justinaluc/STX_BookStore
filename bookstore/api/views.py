from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_api_spec(request):
    """
    gives a rigid specification data about required api project version
    """
    spec = {
        "info": {
            "version": "2022.05.16"
            }
        }
    return Response(spec)
