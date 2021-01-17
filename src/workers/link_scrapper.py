import logging
from asyncio import sleep
from random import randint

from src.helpers.queue import SCRAPPING_LINK_TOPIC_KAFKA, app

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@app.agent(SCRAPPING_LINK_TOPIC_KAFKA)
async def execute_job_agent(stream):
    async for event in stream.noack().events():
        await simulate_scrapping(event.value)
        event.ack()


async def simulate_scrapping(link_obj):
    time_to_sleep = randint(10, 30) / 10
    await sleep(time_to_sleep)

    logger.info(f"The link {link_obj['link']} was visited and scrapped!")
