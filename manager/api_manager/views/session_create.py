import base64
import json
import os

from pb.publish_event import publish_event
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api_manager.apps import cities_coordinates
from api_manager.models.city import City
from api_manager.serializers import SessionSerializer


# PROJECT_ID = os.environ["PUBSUB_PROJECT_ID"]
# DATA_RETRIEVAL = os.environ["DATA_RETRIEVAL_TOPIC"]


@api_view(["POST"])
def start_session_pipeline(request):
    user_id = request.data.get("user_id")
    geo_id = request.data.get("city_id")

    city = get_object_or_404(City, pk=geo_id)

    session_serializer = SessionSerializer(
        data={
            "geo_id": geo_id,
            "name": city.name,
            "alternate_names": city.alternate_names,
            "latitude": city.latitude,
            "longitude": city.longitude,
            "country_code": city.country_code,
            "admin_code": city.admin_code_1,
            "population": city.population,
            "elevation": city.elevation,
            "timezone": city.timezone,
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
