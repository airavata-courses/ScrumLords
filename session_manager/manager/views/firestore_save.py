import base64
import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from manager.apps import fs_client


@api_view(["POST"])
def save_session(request):
    data = json.loads(
        base64.b64decode(request.data["message"]["data"]).decode("utf-8")
    )
    # data = request.data.get("data")
    doc_ref = fs_client.collection("sessions").document(str(data.get("id")))
    doc_ref.set(data)
    return Response(status=status.HTTP_200_OK)
