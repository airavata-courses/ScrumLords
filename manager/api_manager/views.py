import base64
import json
import os

from pb.publish_event import publish_event
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api_manager.apps import cities_coordinates
from api_manager.serializers import SessionSerializer


# PROJECT_ID = os.environ["PUBSUB_PROJECT_ID"]
# DATA_RETRIEVAL = os.environ["DATA_RETRIEVAL_TOPIC"]


@api_view(["POST"])
def start_session_pipeline(request):
    user_id = request.data.get("user_id")
    geo_id = request.data.get("city_id")

    (
        name,
        alternate_names,
        latitude,
        longitude,
        country_code,
        admin_code,
        population,
        elevation,
        timezone,
    ) = cities_coordinates.get(geo_id)

    session_serializer = SessionSerializer(
        data={
            "geo_id": geo_id,
            "name": name,
            "alternate_names": alternate_names,
            "latitude": latitude,
            "longitude": longitude,
            "country_code": country_code,
            "admin_code": admin_code,
            "population": population,
            "elevation": elevation,
            "timezone": timezone,
            "status": "initialized",
            "user_id": user_id,
        }
    )

    # Save session to db
    session_serializer.is_valid(raise_exception=True)
    session_serializer.save()

    # Publish onward to data_retrieval
    # publish_event(
    #     data=session_serializer.data,
    #     project_id=PROJECT_ID,
    #     topic_name=DATA_RETRIEVAL,
    # )

    return Response({"data": session_serializer.data}, status=status.HTTP_200_OK)
