import os
import base64
import datetime
import logging

from redis import asyncio as aioredis

from dotenv import load_dotenv


load_dotenv()


REDIS_URL = str(os.getenv("REDIS_URL"))


async def send_file(filename: str, origin: str, file_data: bytes):
    if not REDIS_URL:
        raise ValueError("Environment variable REDIS_URL is not defined.")
    if not filename:
        raise ValueError("filename must be specified.")
    if not origin:
        raise ValueError("origin must be specified.")
    redis = await aioredis.from_url(REDIS_URL, encoding="utf8", decode_responses=True)
    result = None
    data = base64.encodebytes(file_data).decode("utf8")
    if data:
        filedata = {
            "filename": filename,
            "data": data,
            "origin": origin,
            "filetime_created": str(datetime.datetime.now()),
        }
        result = await redis.xadd(
            "files",
            filedata,
        )
        logging.info("file sent to redis - %s - %s", result, filename)
    await redis.close()
    return result
