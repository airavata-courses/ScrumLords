import multiprocessing
import os

bind = "0.0.0.0:8300"
accesslog = "-"

if os.environ["DJANGO_ENV"] == "development":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'model_execution.settings')
else:
    pass

reload = "true"
timeout = 1000
workers = multiprocessing.cpu_count()
