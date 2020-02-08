from collections import defaultdict

from rest_framework import status
from rest_framework.decorators import api_view
import requests
import os
from datetime import datetime, timedelta

from rest_framework.response import Response


@api_view(["POST"])
def retrieve_historical_data(request):
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
    weather_history = defaultdict(dict)

    for days in reversed(range(1, n_days_before + 1)):
        previous_datetime = current_datetime - timedelta(days=days)
        url = "https://api.darksky.net/forecast/{0}/{1},{2},{3}?exclude=currently,flags".format(
            api_key, latitude, longitude, str(previous_datetime.timestamp()).split(".")[0]
        )
        dark_sky_api_response = requests.get(url=url)
        weather_history[days] = dark_sky_api_response.json()

    response = {
        "n_days_before": n_days_before,
        "n_days_after": n_days_after,
        "data_retrieved": weather_history,
        "latitude": latitude,
        "longitude": longitude,
        "session_id": data.get("session_id"),
    }

    # TODO publish to both api_manager, session_manager and model_execution

    return Response({"data": response}, status=status.HTTP_200_OK)
