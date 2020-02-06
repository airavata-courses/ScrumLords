from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api_manager.models import Session
from api_manager.serializers import SessionSerializer


@api_view(["GET"])
def get_all_sessions(request, user_id):
    response = SessionSerializer(
        Session.objects.filter(user_id=user_id).all(),
        many=True,
    ).data
    return Response({"data": response}, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_session(request, session_id):
    response = SessionSerializer(get_object_or_404(Session, pk=session_id)).data
    return Response({"data": response}, status=status.HTTP_200_OK)
