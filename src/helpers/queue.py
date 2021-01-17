import logging
from os import getenv

import faust

logger = logging.getLogger(__name__)

KAFKA_BROKER = getenv("kAFKA_BROKER", "kafka://localhost")
app = faust.App(
    "jobs_executor",
    broker=KAFKA_BROKER,
    key_serializer="json",
    value_serializer="json",
)
SCRAPPING_LINK_TOPIC_KAFKA = app.topic("scrapping_queue")
