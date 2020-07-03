from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def hello_world(request):
    if request.method == "GET":
        return Response({"message": "Megamind Working", "status": status.HTTP_200_OK})