#!/usr/bin/env bash
gunicorn -c gconf.py manager.wsgi
