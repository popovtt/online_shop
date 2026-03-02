from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    POSTGRESQL_DSN: str

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env")


@lru_cache
def get_config() -> Settings:
    return Settings()  # type: ignore


config = get_config()
