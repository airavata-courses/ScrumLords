import multiprocessing
import os

bind = "0.0.0.0:8200"
accesslog = "-"

if os.environ["DJANGO_ENV"] == "development":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_data_retrieval.settings')
else:
    pass

reload = "true"
timeout = 1000
workers = multiprocessing.cpu_count()
