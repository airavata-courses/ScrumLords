import base64
import json
from collections import defaultdict

from pb.publish_event import publish_event
from rest_framework import status
from rest_framework.decorators import api_view
import requests
import os
from datetime import datetime, timedelta

from rest_framework.response import Response

PROJECT_ID = os.environ["PUBSUB_PROJECT_ID"]
MODEL_EXECUTE = os.environ["MODEL_EXECUTE_TOPIC"]
UPDATE_STATUS = os.environ["UPDATE_STATUS_TOPIC"]
UPDATE_SESSION = os.environ["UPDATE_SESSION_TOPIC"]


@api_view(["POST"])
def retrieve_historical_data(request):
    # data has session_id, latitude, longitude, n_days_before and n_days_after
    data = json.loads(base64.b64decode(request.data["message"]["data"]).decode("utf-8"))

    # data = request.data.get("data")
    latitude, longitude, n_days_before, n_days_after, api_key = (
        data.get("latitude"),
        data.get("longitude"),
        data.get("n_days_before"),
        data.get("n_days_after"),
        os.environ["DARK_SKY_API_KEY"],
    )

    current_datetime = datetime.now()
    weather_history = defaultdict(dict)

    for days in reversed(range(1, n_days_before + 1)):
        previous_datetime = current_datetime - timedelta(days=days)
        url = "https://api.darksky.net/forecast/{0}/{1},{2},{3}?exclude=currently,flags".format(
            api_key,
            latitude,
            longitude,
            str(previous_datetime.timestamp()).split(".")[0],
        )
        dark_sky_api_response = requests.get(url=url)
        weather_history[days] = dark_sky_api_response.json()

    response = {
        "n_days_after": n_days_after,
        "data_retrieved": weather_history,
        "latitude": latitude,
        "longitude": longitude,
        "session_id": data.get("session_id"),
    }

    # Publish to model_execute topic
    publish_event(
        data={
            key: response[key]
            for key in ["n_days_after", "latitude", "longitude", "session_id"]
        },
        project_id=PROJECT_ID,
        topic_name=MODEL_EXECUTE,
    )

    # Publish to update_status topic
    publish_event(
        data={"status": "retrieved", "session_id": data.get("session_id")},
        project_id=PROJECT_ID,
        topic_name=UPDATE_STATUS,
    )

    # Publish to update_session topic
    publish_event(
        data={
            "status": "retrieved",
            "session_id": data.get("session_id"),
            "data_retrieved": response["data_retrieved"],
        },
        project_id=PROJECT_ID,
        topic_name=UPDATE_SESSION,
    )

    return Response(status=status.HTTP_200_OK)
