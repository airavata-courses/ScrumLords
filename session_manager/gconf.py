import os

import multiprocessing

bind = "0.0.0.0:8100"
accesslog = "-"

if os.environ["DJANGO_ENV"] == "development":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'session_manager.settings')
else:
    pass

reload = "true"
timeout = 1000
workers = multiprocessing.cpu_count()
