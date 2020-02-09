from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from manager.apps import fs_client


@api_view(["POST"])
def delete_session(request):
    # data = json.loads(
    #     base64.b64decode(request.data["message"]["data"]).decode("utf-8")
    # )
    data = request.data.get("data")
    fs_client.collection("sessions").document(data.get("id")).delete()
    return Response(status=status.HTTP_200_OK)
