from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    KAFKA_BOOTSTRAP_SERVERS: str
    KAFKA_CLEANED_TEXT_TOPIC: str
    KAFKA_KEYWORDS_TOPIC: str


@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()