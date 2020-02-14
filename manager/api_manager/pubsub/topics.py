import os
import sys

import google
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
env = os.getenv("DJANGO_ENV", "development")
project_id = os.getenv("PUBSUB_PROJECT_ID", "falana-dhimka")

pubsub_config = {
    "weather_forecast": {
        "data_retrieval": {
            "subscription_name": "data_retrieval_sub",
            "endpoint": os.environ["DATA_RETRIEVAL_ENDPOINT"],
        },
        "save_session": {
            "subscription_name": "session_save_sub",
            "endpoint": os.environ["SAVE_SESSION_ENDPOINT"],
        },
        "model_execute": {
            "subscription_name": "model_execute_sub",
            "endpoint": os.environ["MODEL_EXECUTE_ENDPOINT"],
        },
        "update_status": {
            "subscription_name": "update_status_sub",
            "endpoint": os.environ["UPDATE_STATUS_ENDPOINT"],
        },
        "update_session": {
            "subscription_name": "update_session_sub",
            "endpoint": os.environ["UPDATE_SESSION_ENDPOINT"],
        },
        "post_process": {
            "subscription_name": "post_process_sub",
            "endpoint": os.environ["POST_PROCESS_ENDPOINT"],
        },
    },
    "subscription_names": [
        "data_retrieval_sub",
        "save_session_sub",
        "model_execute_sub",
        "update_status_sub",
        "update_session_sub",
        "post_process_sub",
    ],
}


def create_topic(project_id, topic_name):
    """Create a new Pub/Sub topic."""
    try:
        topic_path = publisher.topic_path(project_id, topic_name)
        topic = publisher.create_topic(topic_path)
        print("Topic created: {}".format(topic))
    except (
        google.api_core.exceptions.NotFound,
        google.api_core.exceptions.AlreadyExists,
    ) as e:
        print("[TOPIC {}]".format(topic_name), str(e), "\n")


def list_topics(project_id):
    """Lists all Pub/Sub topics in the given project."""
    project_path = publisher.project_path(project_id)
    for topic in publisher.list_topics(project_path):
        print(topic)


def delete_topic(project_id, topic_name):
    """Deletes an existing Pub/Sub topic."""
    try:
        topic_path = publisher.topic_path(project_id, topic_name)
        publisher.delete_topic(topic_path)
        print("Topic deleted: {}".format(topic_path))
    except (
        google.api_core.exceptions.NotFound,
        google.api_core.exceptions.AlreadyExists,
    ) as e:
        print("[TOPIC {}]".format(topic_name), str(e), "\n")


def get_pubsub_config():
    return pubsub_config


if __name__ == "__main__":
    if sys.argv[1] == "list":
        list_topics(sys.argv[2]) if len(sys.argv) > 2 else list_topics(project_id)
    elif sys.argv[1] == "create":
        [
            create_topic(project_id=project_id, topic_name=topic)
            for topic in sys.argv[2:]
        ] if len(sys.argv) > 2 else [
            create_topic(project_id=project_id, topic_name=topic)
            for topic, _v in pubsub_config["weather_forecast"].items()
        ]
    elif sys.argv[1] == "delete":
        [
            delete_topic(project_id=project_id, topic_name=topic)
            for topic in sys.argv[2:]
        ] if len(sys.argv) > 2 else [
            delete_topic(project_id=project_id, topic_name=topic)
            for topic, _v in pubsub_config["weather_forecast"].items()
        ]
    else:
        print("Wrong Input. You can pass create, delete or list")
