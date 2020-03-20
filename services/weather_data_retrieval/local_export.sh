#!/usr/bin/env bash

export DJANGO_ENV="development"
export DARK_SKY_API_KEY="1bb07041eef420056f9f17d496b72a89"
export PUBSUB_EMULATOR_HOST="localhost:8085"
export PUBSUB_PROJECT_ID="falana-dhimka"
export MODEL_EXECUTE_TOPIC="model_execute"
export MODEL_EXECUTE_ENDPOINT="http://127.0.0.1:8300/dark/forecast"
export UPDATE_STATUS_TOPIC="update_status"
export UPDATE_STATUS_ENDPOINT="http://127.0.0.1:8000/session/status"
export UPDATE_SESSION_TOPIC="update_session"
export UPDATE_SESSION_ENDPOINT="http://127.0.0.1:8100/session/update"
