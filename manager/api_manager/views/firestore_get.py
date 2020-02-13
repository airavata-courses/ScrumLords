from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api_manager.apps import fs_client

from api_manager.exceptions import record_not_found_error


@api_view(["GET"])
def get_retrieved_data(request, session_id):
    doc_ref = fs_client.collection("sessions").document(session_id)
    try:
        data = doc_ref.get().to_dict()
        return Response({"data": data["data_retrieved"]}, status=status.HTTP_200_OK)
    except KeyError:
        record_not_found_error("Data not yet retrieved for this session.")
    except TypeError:
        record_not_found_error("Session not found.")


@api_view(["GET"])
def get_forecast_data(request, session_id):
    doc_ref = fs_client.collection("sessions").document(session_id)
    try:
        data = doc_ref.get().to_dict()
        return Response({"data": data["forecast"]}, status=status.HTTP_200_OK)
    except KeyError:
        record_not_found_error("No forecast data available for this session.")
    except TypeError:
        record_not_found_error("Session not found.")
