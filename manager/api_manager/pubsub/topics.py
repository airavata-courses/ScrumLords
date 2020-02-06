import os
import sys

import google
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
env = os.getenv("DJANGO_ENV", "development")
project_id = os.getenv("PUBSUB_PROJECT_ID", "falana-dhimka")

pubsub_config = {
    "weather_forecast": {
        "test_pubsub": {
            "subscription_name": "test_subscription",
            "endpoint": os.environ["TEST_ENDPOINT"],
        },
        "master_document": {
            "subscription_name": "create_master_document_sub",
            "endpoint": os.environ["CREATE_MASTER_DOC_ENDPOINT"],
        },
        "enhancement": {
            "subscription_name": "perform_enhancement_sub",
            "endpoint": os.environ["PERFORM_ENHANCEMENT_ENDPOINT"],
        },
        "conversion": {
            "subscription_name": "perform_conversion_sub",
            "endpoint": os.environ["PERFORM_CONVERSION_ENDPOINT"],
        },
        "upload": {
            "subscription_name": "upload_doc_sub",
            "endpoint": os.environ["UPLOAD_DOCUMENT_ENDPOINT"],
        },
        "combine_document": {
            "subscription_name": "combine_document_sub",
            "endpoint": os.environ["COMBINE_DOCUMENT_ENDPOINT"],
        },
        "text_recognition": {
            "subscription_name": "text_recognition_sub",
            "endpoint": os.environ["OCR_ENDPOINT"],
        },
        "send_error": {
            "subscription_name": "error_handler",
            "endpoint": os.environ["ERROR_HANDLER_ENDPOINT"],
        },
        "job_error": {
            "subscription_name": "job_error_handler",
            "endpoint": os.environ["JOB_ERROR_ENDPOINT"],
        },
        "identification": {
            "subscription_name": "identification_sub",
            "endpoint": os.environ["IDENTIFICATION_ENDPOINT"],
        },
        "create_child_doc": {
            "subscription_name": "create_child_doc_sub",
            "endpoint": os.environ["CREATE_CHILD_DOC_ENDPOINT"],
        },
        "singular_field_prediction": {
            "subscription_name": "singular_field_prediction_sub",
            "endpoint": os.environ["SINGULAR_FIELD_PREDICTION_ENDPOINT"],
        },
        "tabular_field_prediction": {
            "subscription_name": "tabular_field_prediction_sub",
            "endpoint": os.environ["TABULAR_FIELD_PREDICTION_ENDPOINT"],
        },
        "singular_field_standardisation": {
            "subscription_name": "singular_field_standardisation_sub",
            "endpoint": os.environ["SINGULAR_FIELD_STANDARDISATION_ENDPOINT"],
        },
        "tabular_field_standardisation": {
            "subscription_name": "tabular_field_standardisation_sub",
            "endpoint": os.environ["TABULAR_FIELD_STANDARDISATION_ENDPOINT"],
        },
        "rule_update": {
            "subscription_name": "rule_update_sub",
            "endpoint": os.environ["RULE_UPDATION_ENDPOINT"],
        },
    },
    "subscription_names": [
        "test_subscription",
        "create_master_document_sub",
        "perform_enhancement_sub",
        "perform_conversion_sub",
        "upload_doc_sub",
        "combine_document_sub",
        "text_recognition_sub",
        "error_handler_sub",
        "job_error_handler_sub",
        "identification_sub",
        "create_child_doc_sub",
        "singular_field_prediction_sub",
        "tabular_field_prediction_sub",
        "singular_field_standardisation_sub",
        "tabular_field_standardisation_sub",
        "rule_update_sub",
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
        list_topics(sys.argv[2]) if len(
            sys.argv) > 2 else list_topics(project_id)
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
