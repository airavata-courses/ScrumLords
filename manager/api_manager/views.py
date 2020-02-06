from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from api_manager.apps import cities_coordinates
from api_manager.serializers import SessionSerializer


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

    session_serializer.is_valid(raise_exception=True)
    session_serializer.save()

    return Response({"data": session_serializer.data}, status=status.HTTP_200_OK)
