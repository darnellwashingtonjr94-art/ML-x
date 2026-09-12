from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "ML-x Inference API"
    environment: str = "development"
    model_cache_dir: str = "/tmp/models"
    api_key_secret: str = "change_me_in_production"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
