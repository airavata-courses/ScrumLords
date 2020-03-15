#!/usr/bin/env bash

source local_export.sh
gunicorn -c gconf.py manager.wsgi
