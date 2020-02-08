from collections import defaultdict

from rest_framework import status
from rest_framework.decorators import api_view
import requests
import os
from datetime import datetime, timedelta

from rest_framework.response import Response


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
    # data = json.loads(
    #     base64.b64decode(request.data["message"]["data"]).decode("utf-8")
    # )

    # data has session_id, latitude, longitude, n_days_before and n_days_after
    data = request.data.get("data")

    latitude, longitude, n_days_before, n_days_after, api_key = (
        data.get("latitude"),
        data.get("longitude"),
        data.get("n_days_before"),
        data.get("n_days_after"),
        os.environ["DARK_SKY_API_KEY"],
    )

    current_datetime = datetime.now()
    weather_forecast = defaultdict(dict)

    forecast_today = requests.get(
        url=get_url(api_key=api_key, latitude=latitude, longitude=longitude)
    )

    for days in range(1, n_days_before + 1):
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
        "forecast_today": forecast_today.json(),
        "latitude": latitude,
        "longitude": longitude,
        "session_id": data.get("session_id"),
    }

    # TODO publish to both api_manager, session_manager and post_processing

    return Response({"data": response}, status=status.HTTP_200_OK)
