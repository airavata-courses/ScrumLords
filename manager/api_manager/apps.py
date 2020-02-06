import pickle

from django.apps import AppConfig

cities_coordinates = None


class ApiManagerConfig(AppConfig):
    name = "api_manager"

    def ready(self):
        global cities_coordinates

        with open("api_manager/cities_coordinates.pickle", "rb") as handle:
            cities_coordinates = pickle.load(handle)
