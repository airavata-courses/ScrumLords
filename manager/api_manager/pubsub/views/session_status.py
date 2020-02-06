from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api_manager.models import Session


@api_view(["GET"])
def get_session_status(request, session_id):
    session = Session.objects.get(pk=session_id)
    return Response({"data": {"status": session.status}}, status=status.HTTP_200_OK)
