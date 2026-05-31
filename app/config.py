import os

from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Settings(BaseSettings):
    app_name: str = "MANAGEMENT_API"
    auth_key: str
    
    database_url: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, ".env"),
        env_file_encoding="utf-8"
    )
