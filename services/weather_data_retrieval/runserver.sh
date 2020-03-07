#!/usr/bin/env bash
source local_export.sh
gunicorn -c gconf.py weather_data_retrieval.wsgi
