import os

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings
from sqlalchemy import URL

load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str = "Nimble Contacts Service"
    DB_USER: str = os.environ["DB_USER"]
    DB_PASS: str = os.environ["DB_PASS"]
    DB_HOST: str = os.environ["DB_HOST"]
    DB_PORT: str = os.environ["DB_PORT"]
    DB_NAME: str = os.environ["DB_NAME"]

    @property
    def DATABASE_URL(self) -> str:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.DB_USER,
            password=self.DB_PASS,
            host=self.DB_HOST,
            port=self.DB_PORT,
            database=self.DB_NAME,
        ).render_as_string(hide_password=False)


settings = Settings()
