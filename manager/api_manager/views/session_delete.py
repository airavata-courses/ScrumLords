from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api_manager.models.session import Session


@api_view(["DELETE"])
def delete_session(request, session_id):
    session = get_object_or_404(Session, pk=session_id)
    session.delete()

    # TODO publish onto session_manager service

    return Response(status=status.HTTP_200_OK)
