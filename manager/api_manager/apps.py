import pickle
import firebase_admin
from firebase_admin import firestore, credentials
import os
from django.apps import AppConfig


cities_coordinates = None
fs_client = None


class Firestore:
    def __init__(self):
        cred = credentials.Certificate(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
        firebase_admin.initialize_app(cred)
        self.fs_client = firestore.client()


class ApiManagerConfig(AppConfig):
    name = "api_manager"

    def ready(self):
        global cities_coordinates
        global fs_client

        with open("api_manager/cities_coordinates.pickle", "rb") as handle:
            cities_coordinates = pickle.load(handle)

        fs_obj = Firestore()
        fs_client = fs_obj.fs_client
