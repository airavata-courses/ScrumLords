import base64
import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from manager.apps import fs_client
from manager.exceptions import record_not_found_error
from manager.utils import make_keys_to_dot


@api_view(["POST"])
def update_session(request):
    data = json.loads(base64.b64decode(request.data["message"]["data"]).decode("utf-8"))
    doc_ref = fs_client.collection("sessions").document(str(data.pop("session_id")))
    try:
        doc_ref.update(make_keys_to_dot(data))
        return Response(status=status.HTTP_200_OK)
    except KeyError:
        record_not_found_error("Data not yet retrieved for this session.")
    except TypeError:
        record_not_found_error("Session not found.")
