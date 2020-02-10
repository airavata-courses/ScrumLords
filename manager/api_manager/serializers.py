from rest_framework import serializers

from api_manager.models.session import Session


class SessionSerializer(serializers.ModelSerializer):

    n_days_before = serializers.IntegerField(required=False)
    n_days_after = serializers.IntegerField(required=False)

    class Meta:
        model = Session
        fields = (
            "id",
            "created",
            "modified",
            "visible_id",
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
            "n_days_before",
            "n_days_after",
            "user_id",
        )
