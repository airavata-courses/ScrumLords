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
POST_PROCESS = os.environ["POST_PROCESS_TOPIC"]
UPDATE_STATUS = os.environ["UPDATE_STATUS_TOPIC"]
UPDATE_SESSION = os.environ["UPDATE_SESSION_TOPIC"]


def get_url(api_key: str, latitude: str, longitude: str, date: datetime = None) -> str:
    return "https://api.darksky.net/forecast/{0}/{1},{2}".format(
        api_key, latitude, longitude
    ) + (
        ",{0}?exclude=currently,flags".format(str(date.timestamp()).split(".")[0])
        if date
        else ""
    )


@api_view(["POST"])
def forecast_weather(request):
    # data has session_id, latitude, longitude and n_days_after
    data = json.loads(base64.b64decode(request.data["message"]["data"]).decode("utf-8"))

    # data = request.data.get("data")

    latitude, longitude, n_days_after, api_key = (
        data.get("latitude"),
        data.get("longitude"),
        data.get("n_days_after"),
        os.environ["DARK_SKY_API_KEY"],
    )

    current_datetime = datetime.now()
    weather_forecast = defaultdict(dict)

    forecast_today = requests.get(
        url=get_url(api_key=api_key, latitude=latitude, longitude=longitude)
    ).json()

    # Delete problematic and irrelevant firestore field
    del forecast_today["flags"]

    for days in range(1, n_days_after + 1):
        future_datetime = current_datetime + timedelta(days=days)
        dark_sky_api_response = requests.get(
            url=get_url(
                api_key=api_key,
                latitude=latitude,
                longitude=longitude,
                date=future_datetime,
            )
        )
        weather_forecast[days] = dark_sky_api_response.json()

    response = {
        "n_days_after": n_days_after,
        "forecast": weather_forecast,
        "forecast_today": forecast_today,
        "session_id": data.get("session_id"),
    }

    # # Publish to post_process topic
    # publish_event(
    #     data={
    #         key: response[key] for key in ["forecast", "forecast_today", "session_id"]
    #     },
    #     project_id=PROJECT_ID,
    #     topic_name=POST_PROCESS,
    # )

    # Publish to update_status topic
    publish_event(
        data={"status": "model_executed", "session_id": data.get("session_id")},
        project_id=PROJECT_ID,
        topic_name=UPDATE_STATUS,
    )

    # Publish to update_session topic
    publish_event(
        data={
            "status": "model_executed",
            "session_id": data.get("session_id"),
            "forecast": weather_forecast,
            "forecast_today": forecast_today,
        },
        project_id=PROJECT_ID,
        topic_name=UPDATE_SESSION,
    )

    return Response({"data": response}, status=status.HTTP_200_OK)
