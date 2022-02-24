from utils import env_path
from fastapi_helpers import DefaultSettings
from typing import Optional


class Settings(DefaultSettings):
    app_name = "changelog_bot"
    db_url: str
    port:Optional[str] = "80"
    version:str = "1.0.0"


settings = Settings(env_path)
