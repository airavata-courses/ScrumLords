from rest_framework import serializers

from api_manager.models import Session


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = (
            "id",
            "geo_id",
            "name",
            "alternate_names",
            "latitude",
            "longitude",
            "country_code",
            "admin_code",
            "population",
            "elevation",
            "timezone",
            "status",
            "user_id",
        )
