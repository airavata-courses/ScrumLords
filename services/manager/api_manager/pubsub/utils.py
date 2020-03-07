import os

from google.cloud import pubsub_v1
import logging
import json
import hashlib
from redis import StrictRedis

publisher = pubsub_v1.PublisherClient()
redis_host = os.getenv("REDIS_HOST", "redis://localhost")
redis = StrictRedis.from_url(redis_host)

PROJECT_ID = os.environ["PUBSUB_PROJECT_ID"]
UPDATE_STATUS = os.environ["UPDATE_STATUS_TOPIC"]
UPDATE_SESSION = os.environ["UPDATE_SESSION_TOPIC"]


def publish_event(data, project_id, topic_name):
    topic_path = publisher.topic_path(project_id, topic_name)
    logging.info("{} Topic Path".format(topic_path))

    def callback(message_future):
        # When timeout is unspecified, the exception method waits indefinitely.
        if message_future.exception(timeout=30):
            logging.info(
                "Publishing message on {} threw an Exception {}.".format(
                    topic_name, message_future.exception()
                )
            )
        else:
            logging.info(message_future.result())

    logging.info("Published message IDs:")
    data = json.dumps(data).encode("utf-8")
    message_future = publisher.publish(topic_path, data=data)
    message_future.add_done_callback(callback)
    message_future.result()


def publish_to_error(data, project_id, topic_name):
    topic_path = publisher.topic_path(project_id, topic_name)

    logging.info("%s FOR ERROR_HANDLER_TOPIC TOPIC", topic_path)

    def callback(message_future):
        # When timeout is unspecified, the exception method waits indefinitely.
        if message_future.exception(timeout=10):
            logging.info(
                "Publishing message on %s threw an Exception %s",
                topic_name,
                message_future.exception(),
            )
        else:
            logging.info("publish_to_error id %s", message_future.result())

    data = json.dumps(data).encode("utf-8")
    message_future = publisher.publish(topic_path, data=data)
    message_future.add_done_callback(callback)
    message_future.result()


def handle_error(data, counter):
    retry_limit_exceeded = False

    if counter > 5:
        logging.info("Retry limit exceeded")
        logging.info("data in handle error %s", data)

        # Publish to update_status topic
        publish_event(
            data={"status": "failed", "session_id": data["session_id"]},
            project_id=PROJECT_ID,
            topic_name=UPDATE_STATUS,
        )

        # Publish to update_session topic
        publish_event(
            data={"status": "model_executed", "session_id": data["session_id"],},
            project_id=PROJECT_ID,
            topic_name=UPDATE_SESSION,
        )
        retry_limit_exceeded = True

    return retry_limit_exceeded


def create_key(request, data):
    """
    This helper function creates a unique key for a message
    :param request:
    :param data:
    :return:
    """
    str_data = json.dumps(data)
    sha256 = hashlib.sha256(str_data.encode("utf-8")).hexdigest()
    subscription = request["subscription"].split("/")[-1]
    return "%s_%s_%s" % (subscription, sha256, request["message"]["messageId"])


def get_count(key):
    """
    In case we want to wait some arbitrary time before our message fails
    :param key:
    :return:
    """
    counter = redis.get(key)
    if counter:
        redis.incr(key)
        counter = redis.get(key)
    else:
        counter = 0
        redis.set(key, counter, 3600)
    return int(counter)


def handle_pubsub_retry(request, data):
    key = create_key(request, data)
    counter = get_count(key)
    return handle_error(data, counter)
