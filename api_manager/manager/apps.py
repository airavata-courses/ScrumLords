import pickle

from django.apps import AppConfig


cities_coordinates = None


class ManagerConfig(AppConfig):
    name = 'manager'

    def ready(self):
        global cities_coordinates

        with open('manager/cities_coordinates.pickle', 'rb') as handle:
            cities_coordinates = pickle.load(handle)
