from utils import env_path
from pydantic import BaseSettings


class Settings(BaseSettings):
    sql_user: str
    sql_host: str
    sql_password: str
    sql_db: str
    root_path: str = ''
    celery_broker: str = 'redis://localhost:6379/0'


settings = Settings(env_path)
