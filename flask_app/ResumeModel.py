import os

from redis_om import (JsonModel, Field)
from redis import Redis
from  redis.exceptions import ConnectionError
from uuid import UUID
from dotenv import load_dotenv
load_dotenv()
class Resume(JsonModel):
    name: str = Field(index=True)
    title: str
    contacts: str

    class Meta:

        host = os.getenv('REDIS_HOST') or 'localhost'
        port = os.getenv('REDIS_PORT') or 6379
        password = os.getenv('DB_PASSWORD')
        try:
            database = Redis(host=host, port=int(port), password=password)
        except ConnectionError:
            exit(1)



