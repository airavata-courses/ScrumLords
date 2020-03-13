#!/usr/bin/env bash

source local_export.sh
gunicorn -c gconf.py model_execution.wsgi
