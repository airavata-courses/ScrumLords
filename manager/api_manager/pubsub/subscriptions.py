import os
import sys

import google
from google.cloud import pubsub_v1

from create_topics import get_pubsub_config

subscriber = pubsub_v1.SubscriberClient()
project_id = os.getenv("PUBSUB_PROJECT_ID", "falana-dhimka")


def create_subscription(project_id, topic_name, subscription_name, endpoint):
    """Create a new pull subscription on the given topic."""
    # [START pubsub_create_pull_subscription]
    try:
        topic_path = subscriber.topic_path(project_id, topic_name)
        subscription_path = subscriber.subscription_path(
            project_id, subscription_name)

        push_config = pubsub_v1.types.PushConfig(push_endpoint=endpoint)

        subscription = subscriber.create_subscription(
            subscription_path, topic_path, push_config, ack_deadline_seconds=600
        )

        print("Push subscription created: {}".format(subscription))
        print("Endpoint for subscription is: {}\n".format(endpoint))
    except google.api_core.exceptions.NotFound as e:
        print("[TOPIC {}]".format(topic_name), str(e), "\n")
    except google.api_core.exceptions.AlreadyExists as e:
        print("[SUBSCRIPTION {}]".format(subscription_name), str(e), "\n")


def delete_subscription(project_id, subscription_name):
    """Deletes an existing Pub/Sub topic."""
    try:
        subscription_path = subscriber.subscription_path(
            project_id, subscription_name)
        subscriber.delete_subscription(subscription_path)
        print("Subscription deleted: {}".format(subscription_path))
    except (
        google.api_core.exceptions.NotFound,
        google.api_core.exceptions.AlreadyExists,
    ) as e:
        print("[SUBSCRIPTION {}]".format(subscription_name), str(e), "\n")


def list_subscriptions_in_topic(project_id, topic_name):
    """Lists all subscriptions for a given topic."""

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)
    print("Topic name: ", topic_name, "\nSubscriptions: ")
    for subscription in publisher.list_topic_subscriptions(topic_path):
        print("\t", subscription)


def list_subscriptions_in_project(project_id):
    """Lists all subscriptions in the current project."""

    project_path = subscriber.project_path(project_id)

    for subscription in subscriber.list_subscriptions(project_path):
        print(subscription.name)


def update_subscription(project_id, subscription_name, endpoint):
    """
    Updates an existing Pub/Sub subscription's push endpoint URL.
    Note that certain properties of a subscription, such as
    its topic, are not modifiable.
    """

    subscription_path = subscriber.subscription_path(
        project_id, subscription_name)

    push_config = pubsub_v1.types.PushConfig(push_endpoint=endpoint)

    subscription = pubsub_v1.types.Subscription(
        name=subscription_path, push_config=push_config
    )

    update_mask = {"paths": {"push_config"}}

    subscriber.update_subscription(subscription, update_mask)
    result = subscriber.get_subscription(subscription_path)

    print("Subscription updated: {}".format(subscription_path))
    print("New endpoint for subscription is: {}".format(result.push_config))


def create_single_subscription(project_id, topic):
    print("\n[TOPIC {}]".format(topic))
    try:
        subscription_name = input("Enter subscription name: ")
        endpoint = input("Enter endpoint: ")
        create_subscription(
            project_id=project_id,
            topic_name=topic,
            subscription_name=subscription_name,
            endpoint=endpoint,
        )
    except (
        google.api_core.exceptions.NotFound,
        google.api_core.exceptions.AlreadyExists,
    ) as e:
        print("[TOPIC {}]".format(topic), str(e), "\n")


if __name__ == "__main__":
    pubsub_config = get_pubsub_config()
    if sys.argv[1] == "list":
        list_subscriptions_in_project(sys.argv[2]) if len(
            sys.argv
        ) > 2 else list_subscriptions_in_project(project_id=project_id)
    elif sys.argv[1] == "create":
        [
            create_single_subscription(project_id=project_id, topic=topic)
            for topic in sys.argv[2:]
        ] if len(sys.argv) > 2 else [
            create_subscription(
                project_id, key, value["subscription_name"], value["endpoint"]
            )
            for key, value in pubsub_config["weather_forecast"].items()
        ]
    elif sys.argv[1] == "update":
        if not len(sys.argv) > 2:
            subscription_name = input("Please provide a subscription name: ")
        else:
            subscription_name = sys.argv[2]
        new_endpoint = input("Enter new endpoint: ")
        update_subscription(
            project_id=project_id,
            subscription_name=subscription_name,
            endpoint=new_endpoint,
        )
    elif sys.argv[1] == "delete":
        [
            delete_subscription(
                project_id=project_id, subscription_name=subscription_name
            )
            for subscription_name in sys.argv[2:]
        ] if len(sys.argv) > 2 else [
            delete_subscription(
                project_id=project_id, subscription_name=value["subscription_name"]
            )
            for key, value in pubsub_config["weather_forecast"].items()
        ]
    elif sys.argv[1] == "list_topic":
        [
            list_subscriptions_in_topic(
                project_id=project_id, topic_name=topic_name)
            for topic_name in sys.argv[2:]
        ] if len(sys.argv) > 2 else [
            list_subscriptions_in_topic(project_id=project_id, topic_name=key)
            for key, value in pubsub_config["weather_forecast"].items()
        ]
    else:
        print("Wrong Input. You can pass create, update, delete, list, list_topic")
