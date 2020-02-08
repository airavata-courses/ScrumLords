from rest_framework.decorators import api_view


@api_view(["POST"])
def retrieve_historical_data(request):
    # data = json.loads(
    #     base64.b64decode(request.data["message"]["data"]).decode("utf-8")
    # )

    # data has session_id, latitude, longitude, and n_days
    data = request.data.get("data")
    pass
