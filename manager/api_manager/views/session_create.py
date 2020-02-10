import os

from django.db.models import Q
from pb.publish_event import publish_event
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api_manager.exceptions import record_not_found_error
from api_manager.models.city import City
from api_manager.serializers import SessionSerializer


PROJECT_ID = os.environ["PUBSUB_PROJECT_ID"]
DATA_RETRIEVAL = os.environ["DATA_RETRIEVAL_TOPIC"]
SAVE_SESSION = os.environ["SAVE_SESSION_TOPIC"]


@api_view(["POST"])
def start_session_pipeline(request):
    user_id = request.data.get("user_id")
    geo_id = request.data.get("city_id")

    city = get_object_or_404(City, pk=geo_id)

    # try:
    #     city = City.objects.filter(Q(latitude=latitude) & Q(longitude=longitude)).get()
    # except Exception:
    #     record_not_found_error("City object not found.")

    session_serializer = SessionSerializer(
        data={
            "geo_id": city.id,
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

    print(
        session_serializer.data["n_days_before"],
        session_serializer.data["n_days_after"],
        "\n\n",
    )

    # Publish to data_retrieval topic
    publish_event(
        data={
            "session_id": session_serializer.data["id"],
            "n_days_before": session_serializer.data["n_days_before"],
            "n_days_after": session_serializer.data["n_days_after"],
            "latitude": city.latitude,
            "longitude": city.longitude,
        },
        project_id=PROJECT_ID,
        topic_name=DATA_RETRIEVAL,
    )

    # Publish to save_session topic
    publish_event(
        data=session_serializer.data, project_id=PROJECT_ID, topic_name=SAVE_SESSION
    )

    return Response({"data": session_serializer.data}, status=status.HTTP_200_OK)
