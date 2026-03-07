from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=f"{BASE_DIR}/.env",
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__"
    )

    db: DatabaseConfig
    access_token: AccessToken = AccessToken()



@lru_cache
def get_config() -> Settings:
    return Settings()  # type: ignore


settings = get_config()
